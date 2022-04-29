%script to get values at defined chosenTime in test
chosenTime = 400; %deciseconds 10hz
%bring in values from sim output
COarray = evalin('base','COoutNew');
NOarray = evalin('base','NOoutNew');
HCarray = evalin('base','HCoutNew');
%NOarray
x = NOarray(chosenTime,1); %chosenTime
y = NOarray(chosenTime,2)*1000; %test output
z= NOarray(chosenTime,4)*1000; %calculated value
disp(['chosenTime: ', num2str(x),'sec, NOarray output mg/mi: test: ',num2str(y),' model: ',num2str(z)]);
%COarray
x = COarray(chosenTime,1); %chosenTime
y = COarray(chosenTime,2)*1000; %test output
z = COarray(chosenTime,4)*1000; %calculated value
disp(['chosenTime: ', num2str(x),'sec, COarray output mg/mi: test: ',num2str(y),' model: ',num2str(z)]);
%HCarray
x = HCarray(chosenTime,1); %chosenTime
y = HCarray(chosenTime,2)*1000; %test output
z = HCarray(chosenTime,4)*1000; %calculated value
disp(['chosenTime: ', num2str(x),'sec, HCarray output mg/mi: test: ',num2str(y),' model: ',num2str(z)]);
