% --- output test results to txt file  ---

%bring in values from model output workspace
COarray = evalin('base','COoutNew');
NOarray = evalin('base','NOoutNew');
HCarray = evalin('base','HCoutNew');

%create a x row by 4 column matrix
all_data = zeros(length(COarray),4); % row, column
all_data(:,1) = COarray(:,1); %time
all_data(:,2) = COarray(:,4); %model CO output
all_data(:,3) = HCarray(:,4); %model HC output
all_data(:,4) = NOarray(:,4); %model NOx output
% disp(all_data);

%write data to txt file
fileID = fopen('model_data.txt','w');
fprintf(fileID,'Time CO HC NOx\n');
for row = 1:length(COarray)
    data = all_data(row,:);
    if row < length(COarray)
        fprintf(fileID,'%2.1f %2.7f %2.7f %2.7f\n',data);
    else
        fprintf(fileID,'%2.1f %2.7f %2.7f %2.7f',data);
    end
end
fclose(fileID);
