function [score]= modelrateforoptimizer(COtp,HCtp,NOtp,trange)
%fuction to score model data to modal data
% bagdata is 3x3 matrix: co,hc,no and 3 bag values each
% modaldata is recorded modal data for CO,HC,NO (n,3) matrix
% COtp,HCtp,NOtp are nx2 matrix of cumulative tailpipe values: modal,model


timestep=trange(1,3); %data recorded in 1 or 10hz
%find lenght of inputs
b=length(COtp);

%bring user data into model rating code for weights 
[bagdata,weight,bagstart,coldstart] = UserInput();

%define bag end times
if weight(1,5) == 0 %FTP
        coldstart = fix(coldstart/timestep);
        bag1end = fix(bagstart(2)/timestep);
        bag2end = fix(bagstart(3)/timestep);
        bag3end = b ;
else %WLTC
        coldstart = fix(coldstart/timestep);
        bag1end = fix(bagstart(2)/timestep);
        bag2end = fix(bagstart(3)/timestep);
        bag3end = fix(bagstart(4)/timestep);
        bag4end = b;
end

%define vectors to store accuracy ratings per time step
COacc = zeros(b,1);
HCacc = zeros(b,1);
NOacc = zeros(b,1);

    %where the magic happens...
    
    for n = 1:b
        %compare **MODAL VS MODEL** data: find difference in point values
        COacc(n,1) = 100*(abs(COtp(n,2)-COtp(n,1))/(COtp(n,1)+.00001));
        HCacc(n,1) = 100*(abs(HCtp(n,2)-HCtp(n,1))/(HCtp(n,1)+.00001));
        NOacc(n,1) = 100*(abs(NOtp(n,2)-NOtp(n,1))/(NOtp(n,1)+.00001));
        
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


         
    %calc **BAG** accuracy for each constituent
        CObagacc(1,1)=100*(abs(COtp(bag1end,2)-bagdata(1,1))/bagdata(1,1));
        CObagacc(2,1)=100*(abs(COtp(bag2end,2)-bagdata(1,2))/bagdata(1,2));
        CObagacc(3,1)=100*(abs(COtp(bag3end,2)-bagdata(1,3))/bagdata(1,3));
        
        
        HCbagacc(1,1)=100*(abs(HCtp(bag1end,2)-bagdata(2,1))/bagdata(2,1));
        HCbagacc(2,1)=100*(abs(HCtp(bag2end,2)-bagdata(2,2))/bagdata(2,2));
        HCbagacc(3,1)=100*(abs(HCtp(bag3end,2)-bagdata(2,3))/bagdata(2,3));
        
        
        NObagacc(1,1)=100*(abs(NOtp(bag1end,2)-bagdata(3,1))/bagdata(3,1));
        NObagacc(2,1)=100*(abs(NOtp(bag2end,2)-bagdata(3,2))/bagdata(3,2));
        NObagacc(3,1)=100*(abs(NOtp(bag3end,2)-bagdata(3,3))/bagdata(3,3));
         
      if weight(1,5) > 0 %more than 3 phases: WLTC
          CObagacc(4,1)=100*(abs(COtp(bag4end,2)-bagdata(1,4))/bagdata(1,4));
          HCbagacc(4,1)=100*(abs(HCtp(bag4end,2)-bagdata(2,4))/bagdata(2,4));
          NObagacc(4,1)=100*(abs(NOtp(bag4end,2)-bagdata(3,4))/bagdata(3,4));
      else
          CObagacc(4,1)=0;
          HCbagacc(4,1)=0;
          NObagacc(4,1)=0;
      end
      
    
    
    
    %**CALC AVERAGE MODAL VS MODEL**line match value per phase
    
    
    aveCOcold = mean(COacc(1:coldstart));
    aveCOacc1 = mean(COacc(1:bag1end));
    aveCOacc2 = mean(COacc(bag1end:bag2end));
    aveCOacc3 = mean(COacc(bag2end:bag3end));
    
    aveHCcold = mean(HCacc(1:coldstart));
    aveHCacc1 = mean(HCacc(1:bag1end));
    aveHCacc2 = mean(HCacc(bag1end:bag2end));
    aveHCacc3 = mean(HCacc(bag2end:bag3end));
    
    aveNOcold = mean(NOacc(1:coldstart));
    aveNOacc1 = mean(NOacc(1:bag1end));
    aveNOacc2 = mean(NOacc(bag1end:bag2end));
    aveNOacc3 = mean(NOacc(bag2end:bag3end));
    
    if weight(1,5) > 0 %more than 3 phases: WLTC
        aveCOacc4 = mean(COacc(bag3end:bag4end));
        aveHCacc4 = mean(HCacc(bag3end:bag4end));
        aveNOacc4 = mean(NOacc(bag3end:bag4end));
    else
        aveCOacc4=0;
        aveHCacc4=0;
        aveNOacc4=0;
    end
       
    %**FINAL SCORE using weighted scores defined in UserInput function
    
    COscore = weight(1,1)*aveCOcold+ weight(1,2)*aveCOacc1+ weight(1,3)*aveCOacc2+ weight(1,4)*aveCOacc3+ weight(1,5)*aveCOacc4...
        + weight(1,6)*CObagacc(1,1)+ weight(1,7)*CObagacc(2,1)+ weight(1,8)*CObagacc(3,1)+ weight(1,9)*CObagacc(4,1);
    
    HCscore = weight(2,1)*aveHCcold+ weight(2,2)*aveHCacc1+ weight(2,3)*aveHCacc2+ weight(2,4)*aveHCacc3+ weight(2,5)*aveHCacc4...
        + weight(2,6)*HCbagacc(1,1)+ weight(2,7)*HCbagacc(2,1)+ weight(2,8)*HCbagacc(3,1)+ weight(2,9)*HCbagacc(4,1);
    
    NOscore = weight(3,1)*aveNOcold+ weight(3,2)*aveNOacc1+ weight(3,3)*aveNOacc2+ weight(3,4)*aveNOacc3+ weight(3,5)*aveNOacc4...
        + weight(3,6)*NObagacc(1,1)+ weight(3,7)*NObagacc(2,1)+ weight(3,8)*NObagacc(3,1)+ weight(3,9)*NObagacc(4,1);
    
   score = COscore + HCscore + NOscore;
   %score is 0 to n; closer to 0 the better the 'match'
end
    


