function  MultiCore_RunModv2FTP(ModelName,time,Iter_vars,feedin,tpin,trange)

%   In order to use 'Add to Path' my functions and be in model match foler
%   as current directory 
%user inputs:
 % bagdata = [  .2093,.2245,.2784; %CO bag data 1,2,3
              .014,.0141,.0154;  %HC bag data 1,2,3
              .0056,.0082,.0093;  %NO bag data 1,2,3
            ];




%Load model and initialize parallel workers.
tic
load_system(ModelName);
pool = gcp; %Use default number of parallel workers.

spmd
    %Setup tempdir and cd into it (to prevent strange files from appearing,
    %etc.).
    currDir = pwd;
    addpath(currDir);
    
    tmpDir = tempname;
    mkdir(tmpDir);
    cd(tmpDir);
    assignin('base', 'WorkFolder', tmpDir);
    
    %Copy all of the necessary read/write files into the temp directory.
    filelist = dir(currDir);
    
    for n = 1:length(filelist)
        if filelist(n).isdir == 0
            [~, ~, ext] = fileparts([currDir, '\', filelist(n).name]);
            if ~strcmp(ext, '.slx')
                copyfile([currDir, '\', filelist(n).name], tmpDir);
            end
        end
    end
    
    %Load the model on the worker.
    load_system(ModelName);
end

%Initialize emissions results data structures.
ncases = length(Iter_vars(:, 1));
Result(ncases) = struct;
mmscore = zeros(ncases,9); %Mark: create matrix for model match scores

%%
%Run each model
parfor mem=1:ncases
    assignin('base', 'feedin', feedin);
    assignin('base', 'tpin', tpin);
    assignin('base', 'trange', trange);
    assignin('base', 'time', time);
    
    [CO, HC, NO] = SingleRun(ModelName,Iter_vars(mem,:),trange);
    Result(mem).COtp = CO;
    Result(mem).HCtp = HC;
    Result(mem).NOtp = NO;
    
    %% ***Mark's scoring code---------------------------------------
    [score] = modelrateV4(CO,HC,NO,bagdata)
    mmscore(mem,:) = score;
    
    
end

%Switch all of the workers back to their original folder.
spmd
    cd(currDir);
    rmdir(tmpDir, 's');
    rmpath(currDir);
    close_system(ModelName, 0);
end

etime = toc;
fprintf('Elapsed time = %.2f seconds.\n', etime);

%%
%Prepare the results for plotting.
a = length(Result(1).COtp(:, 1));
b = length(Result); %number of tests 

COtp = zeros(a, b);
HCtp = zeros(a, b);
NOtp = zeros(a, b);

for n = 1:length(Result)
    COtp(:, n) = Result(n).COtp(:, 2);
    HCtp(:, n) = Result(n).HCtp(:, 2);
    NOtp(:, n) = Result(n).NOtp(:, 2);
    
end

COtest = Result(1).COtp(:, 1);
HCtest = Result(1).HCtp(:, 1);
NOtest = Result(1).NOtp(:, 1);

if length(time) > length(COtp(:, n))
    COtp = [zeros(1,b); COtp];
    HCtp = [zeros(1,b); HCtp];
    NOtp = [zeros(1,b); NOtp];
    
    COtest = [0; COtest];
    HCtest = [0; HCtest];
    NOtest = [0; NOtest];
end

%%
%Plot the results
fig = figure;
h = [0 0 0];

h(1) = subplot(3, 1, 1);
p(1,1) = plot(time, COtest);
hold on
for n = 1:ncases
    p(n+1,1) = plot(time, COtp(:, n));
end

xlabel('Time (s)');
ylabel('TP CO (g/mi)');

h(2) = subplot(3, 1, 2);
p(1,2) = plot(time, HCtest);
hold on
for n = 1:ncases
    p(n+1,2) = plot(time, HCtp(:, n));
end

xlabel('Time (s)');
ylabel('TP HC (g/mi)');

h(3) = subplot(3, 1, 3);
p(1,3) = plot(time, NOtest);
hold on
for n = 1:ncases
    p(n+1,3) = plot(time, NOtp(:, n));
end

xlabel('Time (s)');
ylabel('TP NOx (g/mi)');

set(p(1,:), 'DisplayName', 'Test');
set(p(1,:), 'LineWidth', 3.5);


%% marks code to add score to data names------------
%this part creates the base name for tests
for n = 2:length(p(:,1))
      basenam = ['[', num2str(Iter_vars(n-1, 1)), ',', num2str(Iter_vars(n-1, 2)),...
        ',', num2str(Iter_vars(n-1, 3)), ',', num2str(Iter_vars(n-1, 4)),...
        ',', num2str(Iter_vars(n-1, 5)), ',', num2str(Iter_vars(n-1, 6)),...
        ']'];
    
    set(p(n,:), 'DisplayName', basenam);
    set(p(n,:), 'LineWidth', 2.0);
% this part adds scores to test names
    a=n-1;
    %CO score to name
    nam = [basenam,' CO score: ', num2str(mmscore(a,3))];
    set(p(n,1), 'DisplayName', nam)
    set(p(n,1), 'LineWidth', 2.0);
    %HC score to name
    nam = [basenam,' HC score: ', num2str(mmscore(a,6))];
    set(p(n,2), 'DisplayName', nam)
    set(p(n,2), 'LineWidth', 2.0);
    %NO score to name
    nam = [basenam,' NO score: ', num2str(mmscore(a,9))];
    set(p(n,3), 'DisplayName', nam)
    set(p(n,3), 'LineWidth', 2.0);
end
%%
%marks code to set score button
testscore = uicontrol('Parent',fig,...
               'Style','togglebutton',... %style of button
               'String','**SCORE**',... %button name
               'BackgroundColor',[1 .2 .2],...%button color RGB
               'Position',[100 5 120 30],... %button position
               'Callback', @scorecode); %when pressed go to function scorecode
 %%          
plotbrowser on
linkaxes(h, 'x');
    function scorecode(src,event)        
        testnum = inputdlg('which test do you want to score?',...
            'Test Score',...
            [1 40]);% size of pop-up box
         testnum = str2double(testnum);%convert string to double/number
         modelrateV5(mmscore,testnum);%scoring code
    end
end
