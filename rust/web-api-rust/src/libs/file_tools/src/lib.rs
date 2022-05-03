/*
file tools
written by Mark Wottreng
 */

use std::fs; // standard file library

// check if file exists
pub fn check_for_file(path: &String, filename: &String) -> bool {
    use std::path::Path;
    let file_path = format!("{}/{}", path, filename);
    //println!("{}",file_path);
    return Path::new(&file_path).exists();
}

// check if folder exists
pub fn check_for_folder(full_path: &String) -> bool {
    use std::path::Path;
    //let file_path = format!("{}/{}", path, filename);
    //println!("{}",file_path);
    return Path::new(full_path).exists();
}

// copy file into another location
pub fn copy_file_to_directory(file_path: &String, folder_path: &String) -> std::io::Result<()> {
    fs::copy(file_path, folder_path)?;
    Ok(())
}

// create folder
pub fn create_folder(full_folder_path: &String) -> std::io::Result<()> {
    let folder_name = full_folder_path.split("/").last().unwrap();
    println!("[*] checking for `{}` folder in directory",&folder_name);
    if check_for_folder(full_folder_path){
        println!("[!] `{}` folder exists [!]\n[-] Deleting `{}` folder", &folder_name, &folder_name);
        delete_folder(&full_folder_path).unwrap();
    }
    println!("[+] creating folder: `{}`", folder_name);
    fs::create_dir(full_folder_path)?;
    Ok(())
}

// delete folder and all its content
pub fn delete_folder(full_folder_path: &String) -> std::io::Result<()> {
    fs::remove_dir_all(full_folder_path)?;
    Ok(())
}

//
pub fn delete_file(full_folder_path: &String) -> std::io::Result<()> {
    fs::remove_file(full_folder_path)?;
    Ok(())
}

//
pub fn write_string_to_file(new_data: &String, path: &String, filename: &String, method: char, verbose: bool) {
    //
    let file_path = format!("{}/{}", path, filename); //.replace(&['\"'], "");
    //
    if verbose {
        println!("filename: {}", filename);
        println!("path: {}", &path);
        println!("file_path: {}", file_path);
    }
    //
    if method == 'a'{
        let mut current_data: String = String::new();
        // check if exists
        if check_for_file(&path, &filename){
            println!("file exists");
            current_data = read_string_from_file(path, filename, false);
            println!("here: {}",current_data);
        }
        println!("old data: {}\n new data: {}",current_data, new_data);
        let all_data_plus_newline = format!("{}{}\n",current_data,new_data);
        fs::write(&file_path, all_data_plus_newline).unwrap();
    }
    //
    if method == 'w'{
        // write to file --
        let data_plus_newline = format!("{}\n",new_data);
        fs::write(&file_path, data_plus_newline).unwrap();
    }
}

//
pub fn read_string_from_file(path: &String, filename: &String, verbose: bool) -> String {
    //
    let file_path = format!("{}/{}", path, filename); //.replace(&['\"'], "");
    if verbose {
        println!("path: {:#?}", &path);
        println!("filename: {:?}", filename);
        println!("file_path: {:#?}", file_path);
    }
    // read file ---
    let contents = fs::read_to_string(&file_path).unwrap();
    if verbose { println!("{}", contents); }
    return contents;
}