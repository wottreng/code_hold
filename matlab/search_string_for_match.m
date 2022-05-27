%% ----------------------------------------
% PURPOSE: use different strategies to find match string in input string
% INPUT: input string, string to match
% OUTPUT: boolean value based on match being found
% written by: Mark Wottreng
%% ----------------------------------------
function match_found = search_string_for_match(input_string, match_string)
    match_found = false;
    if contains(input_string, match_string)
        match_found = true;
    elseif contains(lower(input_string), match_string)
        match_found = true;
    elseif contains(lower(input_string), lower(match_string))
        match_found = true;
    end
end
