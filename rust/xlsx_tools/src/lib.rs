/*
excel tools
written by Mark Wottreng
 */
use xlsxwriter::*;

// creates a workbook buffer
pub fn create_workbook(workbook_name: &str) -> std::io::Result<(Workbook)>{
    // "debug_data.xlsx"
    println!("[+] creating workbook: {}",workbook_name);
    Ok(Workbook::new(workbook_name))
}

// save workbook buffer to a file
pub fn close_workbook(workbook_obj: xlsxwriter::Workbook) -> std::io::Result<()> {
    println!("[-->] Saving xlsx workbook ...");
    workbook_obj.close().unwrap();
    Ok(())
}

// write data matrix based on catalyst nodes ie. node header is added to data
pub fn write_node_data_vector_to_new_sheet(workbook_obj: &xlsxwriter::Workbook, sheet_name:String, data_matrix:Vec<Vec<f64>>) -> std::io::Result<()>{
    let verbose:bool=false;
    // create worksheet
    let sheet_name_str = &sheet_name[..];
    let mut worksheet = workbook_obj.add_worksheet(Some(sheet_name_str)).unwrap();
    //
    let mut row_counter = 1;
    let mut col_counter = 1;
    let mut time_counter:f64 = 0.0;  // -------  ASSUMPTIONS: 10hz data
    // add data labels: ASSUMPTIONS: time and node count
    worksheet.write_string(0,0,"time", None).unwrap();
    let length_of_row_data:u32 = data_matrix[0].len() as u32;
    for i in 0..length_of_row_data{
        let node_name_string = format!("node_{}",i);
        worksheet.write_string(0,col_counter,&node_name_string[..], None).unwrap();
        col_counter += 1;
    }
    // iterate over vector and write data to worksheet
    for row in data_matrix {
        // write time variable to column `0` for each row
        worksheet.write_number(row_counter, 0, time_counter, None).unwrap();
        time_counter += 0.1;
        // write data in subsequent columns
        col_counter = 1;
        for col in row {
            let data_cell: f64 = col;
            if verbose{
                println!("row: {}, col: {}, data: {}", row_counter, col_counter, data_cell);
            }
            worksheet.write_number(row_counter, col_counter, data_cell, None).unwrap();
            col_counter = col_counter + 1;
        }
        row_counter = row_counter + 1;
    }
    Ok(())
}

// write data matrix to workbook with custom headers
pub fn write_data_matrix_to_new_sheet(workbook_obj: &xlsxwriter::Workbook, sheet_name:String, headers:&[&str],data_matrix:Vec<Vec<f64>>) -> std::io::Result<()>{
    let verbose:bool=false;
    // create worksheet
    let sheet_name_str = &sheet_name[..];
    let mut worksheet = workbook_obj.add_worksheet(Some(sheet_name_str)).unwrap();
    //
    let mut row_counter = 1;
    let mut col_counter = 1;
    let mut time_counter:f64 = 0.0;  // -------  ASSUMPTIONS: 10hz data
    // add data labels/headers: time and headers
    worksheet.write_string(0,0,"time", None).unwrap();
    let length_of_headers = headers.len();
    for i in 0..length_of_headers{
        //let node_name_string = format!("node_{}",i);
        let header_str:&str = &headers[i];
        worksheet.write_string(0,col_counter,header_str, None).unwrap();
        col_counter += 1;
    }
    // iterate over vector and write data to worksheet
    for row in data_matrix {
        // write time variable to column `0` for each row
        worksheet.write_number(row_counter, 0, time_counter, None).unwrap();
        time_counter += 0.1;
        // write data in subsequent columns
        col_counter = 1;
        for col in row {
            let data_cell: f64 = col;
            if verbose{
                println!("row: {}, col: {}, data: {}", row_counter, col_counter, data_cell);
            }
            worksheet.write_number(row_counter, col_counter, data_cell, None).unwrap();
            col_counter = col_counter + 1;
        }
        row_counter = row_counter + 1;
    }
    Ok(())
}

