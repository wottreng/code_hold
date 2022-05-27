% TLDR: find location of variable in string using hash indexing
% OBJECTIVE: capture values of interest within substring that have changed variable name from normal
% ASSUMPTIONS:
% ERROR HANDLING: return empty array if no matches found
% TODO: refine objectives to aleviate false positive outputs
function position_of_variable_in_input_string = case_insensitive_hash_search(input_string, variable_substring)
    variable_substring_as_char_array = split(variable_substring, "");
% build hash of possible matches
    for i=2:(length(variable_substring_as_char_array)-2)
       hash_match_strings{i-1} = append(variable_substring_as_char_array(i), variable_substring_as_char_array(i+1));
    end
% iterate through hash and find all matches in input_string
    position = [];
    for i = 1:length(hash_match_strings)
        current_position = strfind(input_string, hash_match_strings{i});
        if length(current_position) > 0
            for x=1:length(current_position)
                position(end+1) = current_position(x);
            end
        end
    end
% calculate meadian value for all matches then find all possible matches close to median value
    possible_location = [];
    median_position_value = median(position);
    for i=1:length(position)
       if abs(median_position_value - position(i)) < 10
            possible_location(end+1) = position(i);
       end
    end
% calculate average value of possible locations and return value
    average_location_value = round(mean(possible_location));
    if average_location_value > 0
       position_of_variable_in_input_string = average_location_value;
    else
        position_of_variable_in_input_string = [];
    end
end