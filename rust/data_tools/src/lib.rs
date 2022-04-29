/*
data parsing tools
written by Mark Wottreng
 */

/*
-takes in a text block(string) of numbers and returns a matrix vector of float values
-this function is used for reading data out of text file that matlab outputs
 */
pub fn take_text_block_and_parse(content: String) -> Vec<Vec<f64>> {
    let filtered_content = content.replace(" ", "");
    let all_data_vector_strings: Vec<&str> = filtered_content.split("\r\n").collect();
    let number_of_data_rows = all_data_vector_strings.len();
    let mut all_data_float_vec = Vec::new();
    for i in 0..number_of_data_rows {
        let data_row_floats: Vec<f64> = all_data_vector_strings[i].split(",").flat_map(|x| x.parse()).collect();
        all_data_float_vec.push(data_row_floats);
    }
    //println!("first line: {:?}",&all_data_float_vec[0]);
    //println!("second line: {:?}",&all_data_float_vec[1]);
    return all_data_float_vec;
}
