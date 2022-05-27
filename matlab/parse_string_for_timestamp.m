% -----------------------------
% PURPOSE: given an input string, find the timestamp in format: hh:mm:ss.ms
% METHOD: uses regex to parse string and find time with proper format
% -----------------------------
function time_stamp = parse_string_for_timestamp(input_string)
    timeExpressionFormat = '\d+:+\d+:+\d+\.?+\d*'; % Get time vector in format ##:##:##.##
    time_stamp = regexp(input_string,timeExpressionFormat,'match');
    if isempty(time_stamp)
        disp('Invalid time format. Expected ##:##:##.##');
        time_stamp = ""
    end
end