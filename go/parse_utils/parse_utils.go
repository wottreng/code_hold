package main

import "strings"

func main() {
	res := Parse_for_string("the bright brown cow jumped over the fence", "cow")
	println("found in string: ", res)
	index_loc := Parse_for_index("the bright brown cow jumped over the fence", "cow")
	println("index: ", index_loc)
	var_value := Parse_for_value("the bright brown = 34.3, 9788 cow = 5, jumped = 8, over the fence", "brown")
	println("value: ", var_value)

}

// function to check if a string is present in another string
func Parse_for_string(str, substr string) string {
	if strings.Contains(str, substr) {
		return "true"
	}
	return "false"
}

// function to find index of a string in another string
func Parse_for_index(str, substr string) int {
	return strings.Index(str, substr)
}

// function to return the value of a variable in a string
func Parse_for_value(str, substr string) string {
	variable_index := strings.Index(str, substr)
	new_sub_string := str[variable_index+len(substr) : variable_index+len(substr)+10]
	substring_vector := strings.Split(new_sub_string, "")
	// iterate through the vector and find the value
	acceptable_values := []string{"0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
	found_value := ""
	values_found_flag := false
	for i := 0; i < len(substring_vector); i++ {
		values_found_flag = false
		for j := 0; j < len(acceptable_values); j++ {
			if acceptable_values[j] == substring_vector[i] {
				found_value = found_value + substring_vector[i]
				values_found_flag = true
			}
		}
		if values_found_flag == false && len(found_value) > 0 {
			break
		}
	}
	return found_value
}
