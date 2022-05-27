% -------------------------
% PURPOSE: parse a string for the value of a variable
% INPUT: any string of characters, variable name string, number of return values = 1 or 2, boolean value for if negative values are possible
% OUTPUT: single double or array of double
% ASSUMPTIONS:
%   - variable value comes after variable name
%   - if returning 2 values then these values are seperated by a comma
% ERROR HANDLING: if value not found: returns `NaN`
% TODO: for double value variables: split on `:`?
% -------------------------
function output_value = parse_string_for_values(input_string, variable_substring, number_of_return_values, negative_values_possible)
% return substring to be parsed/filtered
    unfiltered_substring = build_substring(input_string, variable_substring, number_of_return_values);
% filter substring by removing non integer characters ------
    if unfiltered_substring ~= "" % if variable substring is found in input_string
% 1 return value --
        if number_of_return_values == 1
            output_value = remove_all_characters_that_are_not_numbers(unfiltered_substring,negative_values_possible);
% 2 return values --
        else
            split_unfiltered_substring = split(unfiltered_substring, ",");
            output_value = [];
            for i=1:2
                output_value(i) = remove_all_characters_that_are_not_numbers(split_unfiltered_substring(i), negative_values_possible);
            end
        end
%
    else %error handling: return NaN if variable_substring is not found
        output_value = NaN; % if substring could not be found then return NaN
    end
end

% ================  SUPPORTING FUNCTIONS ======================

% TLDR: remove all characters that are not numbers and return double value
% INPUT: any string of characters
% OUTPUT: matlab double a.k.a. float
% ASSUMPTIONS: value of interest is within length of input string
% ERROR HANDLING: handle case where a dash (-) is used before number but is not negative value
function return_value = remove_all_characters_that_are_not_numbers(input_string, negative_values_possible)
    input_char_array = split(input_string,""); % turn input_string into and iterable char array
    output_string = "";
    if negative_values_possible
        acceptable_values = "0123456789.-"; % acceptable values: integers, negative sign, decimal point
    else
        acceptable_values = "0123456789.";
    end
%    break_values = ",}";
    VALUES_FOUND_FLAG = false; % when acceptable values are found this triggers
    for i= 1:length(input_char_array)
        if strfind(acceptable_values, input_char_array(i)) > 0 % if char is an acceptable value then add to ouput
           output_string = output_string + input_char_array(i);
           VALUES_FOUND_FLAG = true;
        elseif length(output_string) > 0 && VALUES_FOUND_FLAG == true % if values stop being found then break out of loop
            break; % change_log: this was added to parse `stage` numbers
%        elseif strfind(break_values, input_char_array(i)) > 0 % break on characters: , } (back stop) %% change_log: this is no longer trigger due to FLAG use
%            break; % (signals end of value)
        end
    end
%    output_string
    return_value = str2double(output_string);
end

% --------------

% TLDR: chunk input_string into digestable sub_string to be filtered
% OBJECTIVE: capture values of interest within substring
% ASSUMPTIONS: value of interest lies within substring X amount of characters after index of variable name
% ERROR HANDLING: stop index cannot be beyond length of input string
function sub_string = build_substring(input_string, variable_substring, number_of_return_values)
    length_of_input_string = strlength(input_string);
    length_of_variable_substring = strlength(variable_substring);
% find position of variable within input_string
   position_of_variable_in_input_string = try_different_parsing_strategies(input_string, variable_substring);
% build substring to be fed into filter
    if length(position_of_variable_in_input_string) > 0 % if the variable was found in the input string
        start_index = position_of_variable_in_input_string + length_of_variable_substring;
        if number_of_return_values == 1
           additional_characters = 15;  % is 15 enough ?
        else % multiple return values
            additional_characters = 25; % is 25 enough ?
        end
        stop_index = start_index + additional_characters;
        % error handling: dont index outside of length of input_string
        if stop_index > length_of_input_string
           stop_index = length_of_input_string;
        end
    %
        sub_string = input_string(start_index : stop_index); % create substring to be fed into filter
    else
       sub_string = "";
    end
end

% TLDR: try different strategies to find variable in string
% OBJECTIVE: return position of variable within input string
% ASSUMPTIONS:
% ERROR HANDLING: return empty value if not found
function position_of_variable_in_input_string = try_different_parsing_strategies(input_string, variable_substring)
%   try direct match of variable name to input string
    position_of_variable_in_input_string = strfind(input_string, variable_substring); % try to find it directly
    if length(position_of_variable_in_input_string) > 0 % if found
        return
    end
%    try matching lowercase variable name
    position_of_variable_in_input_string = strfind(input_string, lower(variable_substring)); % try to find its lowercase twin
    if length(position_of_variable_in_input_string) > 0 % if found
        return
    end
%    try matching variable when everything is lowercase
    position_of_variable_in_input_string = strfind(lower(input_string), lower(variable_substring)); % try to find its lowercase twin
    if length(position_of_variable_in_input_string) > 0 % if found
        return
    end
%   position not found. try hash search as last resort
%    position_of_variable_in_input_string = case_insensitive_hash_search(input_string, variable_substring);
end
