function [score]= modelrateforoptimizerv2(COoutNew,HCoutNew,NOoutNew,trange,userInput)
%fuction to score model data to modal data
% bagdata is 3x3 matrix: co,hc,no and 3 bag values each
% modaldata is recorded modal data for CO,HC,NO (n,3) matrix
% COtp,HCtp,NOtp are nx2 matrix of cumulative tailpipe values: modal,model

timestep=trange(1,3); %data recorded in 1 or 10hz
%find lenght of inputs
b=length(COoutNew);
%%
%bring user data into model rating code for weights---------
bags = userInput.bags;%number of phases/bags
coldstart = userInput.coldstart; %cold start end time
bagstart = userInput.bagstart; %bag start times
bagdata = userInput.bagdata; %bag data from test pdf
weight = userInput.weight; %emissions scoring weights
 
%% add bag data together 
%CO
bagdata(1,2) = bagdata(1,1)+ bagdata(1,2);%bag2
bagdata(1,3) = bagdata(1,2)+ bagdata(1,3);%bag3
bagdata(1,4) = bagdata(1,3)+ bagdata(1,4);%bag4
%HC
bagdata(2,2) = bagdata(2,1)+ bagdata(2,2);%bag2
bagdata(2,3) = bagdata(2,2)+ bagdata(2,3);%bag3
bagdata(2,4) = bagdata(2,3)+ bagdata(2,4);%bag4
%NO
bagdata(3,2) = bagdata(3,1)+ bagdata(3,2);%bag2
bagdata(3,3) = bagdata(3,2)+ bagdata(3,3);%bag3
bagdata(3,4) = bagdata(3,3)+ bagdata(3,4);%bag4
%--------------------------------------------------
%% MODEL MATCH MAGIC 
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%****DO NOT MODIFY BELOW THIS LINE****%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% if running NEDC or FTP then this will null bag 4 scores
if bags <4
   weight(1,5) = 0;  %CO phase 4 model match accuracy
   weight(1,9) = 0;  %CO bag 4 accuracy
   weight(2,5) = 0;  %HC phase 4 model match accuracy
   weight(2,9) = 0;  %HC bag 4 accuracy
   weight(3,5) = 0;  %NO phase 4 model match accuracy
   weight(3,9) = 0;  %NO bag 4 accuracy
   bagstart(4) = 0;  %bag 4 start
   bagdata(1,4) = 0; %CO bag 4 number
   bagdata(2,4) = 0; %HC bag 4 number
   bagdata(3,4) = 0; %NO bag 4 number
end

%% if running NEDC then this will null bag 3 scores
if bags <3
   weight(1,4) = 0;  %CO phase 3 model match accuracy
   weight(1,8) = 0;  %CO bag 3 accuracy
   weight(2,4) = 0;  %HC phase 3 model match accuracy
   weight(2,8) = 0;  %HC bag 3 accuracy
   weight(3,4) = 0;  %NO phase 3 model match accuracy
   weight(3,8) = 0;  %NO bag 3 accuracy
   bagstart(3) = 0;  %bag 3 start
   bagdata(1,3) = 0; %CO bag 3 number
   bagdata(2,3) = 0; %HC bag 3 number
   bagdata(3,3) = 0; %NO bag 3 number
end
%--------------------------------------------------new code***
%%
%-----------------------------------------------------------
%Weight factors are to correct for large difference in constituents
%i.e. CO is from 0 to 150mg and NO is from 0 to 20 mg
if bagstart(4)~= 0 %WLTC
COweightfactor = 1;
HCweightfactor = bagdata(1,4)/bagdata(2,4);
NOweightfactor = bagdata(1,4)/bagdata(3,4);
elseif bagstart(3) ~=0 %FTP
COweightfactor = 1;
HCweightfactor = bagdata(1,3)/bagdata(2,3);
NOweightfactor = bagdata(1,3)/bagdata(3,3);  
else %NEDC
COweightfactor = 1;
HCweightfactor = bagdata(1,2)/bagdata(2,2);
NOweightfactor = bagdata(1,2)/bagdata(3,2); 
end
%------------------------------------------------------------
%%
%define bag end times
if bagstart(3) == 0 % NEDC
       coldstart = fix(coldstart/timestep);
        bag1end = fix(bagstart(2)/timestep);
        bag2end = b;
        
elseif bagstart(4) ==0 %FTP
        coldstart = fix(coldstart/timestep);
        bag1end = fix(bagstart(2)/timestep);
        bag2end = fix(bagstart(3)/timestep);
        bag3end = b ; 
else    %WLTC
        coldstart = fix(coldstart/timestep);
        bag1end = fix(bagstart(2)/timestep);
        bag2end = fix(bagstart(3)/timestep);
        bag3end = fix(bagstart(4)/timestep);
        bag4end = b;
end
%%
%define vectors to store accuracy ratings per time step
COacc = zeros(b,1);
HCacc = zeros(b,1);
NOacc = zeros(b,1);
    %where the magic happens...
    
    for n = 1:b
        %compare **MODAL VS MODEL** data: find difference in point values
        COacc(n,1) = 100*(abs(COoutNew(n,4)-COoutNew(n,2)));
        HCacc(n,1) = 100*(abs(HCoutNew(n,4)-HCoutNew(n,2)));
        NOacc(n,1) = 100*(abs(NOoutNew(n,4)-NOoutNew(n,2)));
        
        if COacc(n,1)==inf
            COacc(n,1)=0;
        end
        if HCacc(n,1)==inf
            HCacc(n,1)=0;
        end
        if NOacc(n,1)==inf
            NOacc(n,1)=0;
        end
    end  
    %%
    %calc **BAG** accuracy for each constituent
        CObagacc(1,1)=100*(abs(COoutNew(bag1end,4)-bagdata(1,1)));
        CObagacc(2,1)=100*(abs(COoutNew(bag2end,4)-bagdata(1,2)));
                   
        HCbagacc(1,1)=100*(abs(HCoutNew(bag1end,4)-bagdata(2,1)));
        HCbagacc(2,1)=100*(abs(HCoutNew(bag2end,4)-bagdata(2,2)));
        
        NObagacc(1,1)=100*(abs(NOoutNew(bag1end,4)-bagdata(3,1)));
        NObagacc(2,1)=100*(abs(NOoutNew(bag2end,4)-bagdata(3,2)));
          
      if bagstart(4) ~= 0 %WLTC
          CObagacc(4,1)=100*(abs(COoutNew(bag4end,4)-bagdata(1,4)));
          HCbagacc(4,1)=100*(abs(HCoutNew(bag4end,4)-bagdata(2,4)));
          NObagacc(4,1)=100*(abs(NOoutNew(bag4end,4)-bagdata(3,4)));
          CObagacc(3,1)=100*(abs(COoutNew(bag3end,4)-bagdata(1,3)));
          HCbagacc(3,1)=100*(abs(HCoutNew(bag3end,4)-bagdata(2,3)));
          NObagacc(3,1)=100*(abs(NOoutNew(bag3end,4)-bagdata(3,3)));
      elseif bagstart(3) ~= 0 %FTP
          CObagacc(3,1)=100*(abs(COoutNew(bag3end,4)-bagdata(1,3)));
          HCbagacc(3,1)=100*(abs(HCoutNew(bag3end,4)-bagdata(2,3)));
          NObagacc(3,1)=100*(abs(NOoutNew(bag3end,4)-bagdata(3,3)));
          CObagacc(4,1)=0;
          HCbagacc(4,1)=0;
          NObagacc(4,1)=0;
      else %NEDC; null bag 3&4 values
          CObagacc(4,1)=0;
          HCbagacc(4,1)=0;
          NObagacc(4,1)=0;
          CObagacc(3,1)=0;
          HCbagacc(3,1)=0;
          NObagacc(3,1)=0;
      end
 %%    
    %**CALC AVERAGE MODAL VS MODEL**line match value per phase
    aveCOcold = mean(COacc(1:coldstart));
    aveCOacc1 = mean(COacc(1:bag1end));
    aveCOacc2 = mean(COacc(bag1end:bag2end));
       
    aveHCcold = mean(HCacc(1:coldstart));
    aveHCacc1 = mean(HCacc(1:bag1end));
    aveHCacc2 = mean(HCacc(bag1end:bag2end));
        
    aveNOcold = mean(NOacc(1:coldstart));
    aveNOacc1 = mean(NOacc(1:bag1end));
    aveNOacc2 = mean(NOacc(bag1end:bag2end));
       
    if bagstart(4)~= 0 % WLTC
        aveCOacc4 = mean(COacc(bag3end:bag4end));
        aveHCacc4 = mean(HCacc(bag3end:bag4end));
        aveNOacc4 = mean(NOacc(bag3end:bag4end));
        aveCOacc3 = mean(COacc(bag2end:bag3end));
        aveHCacc3 = mean(HCacc(bag2end:bag3end));
        aveNOacc3 = mean(NOacc(bag2end:bag3end));
    elseif bagstart(3)~= 0 %FTP
        aveCOacc3 = mean(COacc(bag2end:bag3end));
        aveHCacc3 = mean(HCacc(bag2end:bag3end));
        aveNOacc3 = mean(NOacc(bag2end:bag3end));
        aveCOacc4=0;
        aveHCacc4=0;
        aveNOacc4=0;
    else %NEDC; null out bag 3&4
        aveCOacc3=0;
        aveHCacc3=0;
        aveNOacc3=0;
        aveCOacc4=0;
        aveHCacc4=0;
        aveNOacc4=0;
    end  
   %%
    
    %**FINAL SCORE using weighted scores defined in UserInput function
    
    COscore = COweightfactor*(weight(1,1)*aveCOcold+ weight(1,2)*aveCOacc1+ weight(1,3)*aveCOacc2+ weight(1,4)*aveCOacc3+ weight(1,5)*aveCOacc4...
        + weight(1,6)*CObagacc(1,1)+ weight(1,7)*CObagacc(2,1)+ weight(1,8)*CObagacc(3,1)+ weight(1,9)*CObagacc(4,1));
    
    HCscore = HCweightfactor*(weight(2,1)*aveHCcold+ weight(2,2)*aveHCacc1+ weight(2,3)*aveHCacc2+ weight(2,4)*aveHCacc3+ weight(2,5)*aveHCacc4...
        + weight(2,6)*HCbagacc(1,1)+ weight(2,7)*HCbagacc(2,1)+ weight(2,8)*HCbagacc(3,1)+ weight(2,9)*HCbagacc(4,1));
    
    NOscore = NOweightfactor*(weight(3,1)*aveNOcold+ weight(3,2)*aveNOacc1+ weight(3,3)*aveNOacc2+ weight(3,4)*aveNOacc3+ weight(3,5)*aveNOacc4...
        + weight(3,6)*NObagacc(1,1)+ weight(3,7)*NObagacc(2,1)+ weight(3,8)*NObagacc(3,1)+ weight(3,9)*NObagacc(4,1));
    
   score = COscore + HCscore + NOscore;
   %score is 0 to n; closer to 0 the better the 'match'
end
    


