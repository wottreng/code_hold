/*
system level tools
written by Mark Wottreng
 */
use std::fs;
//
pub fn return_file_contents_in_folder(path: &String, verbose: bool) -> Result<Vec<String>, std::io::Error>{
    let mut files_vec: Vec<String> = Vec::new();
    // read directory
    let paths = fs::read_dir(path).unwrap();

    for path in paths {
        let full_path_string = path.unwrap().path().into_os_string().into_string().unwrap();
        let file_name = full_path_string.split('\\').last().unwrap().to_string();
        if verbose {
            println!("path: {}", &full_path_string);
            println!("file_name: {:?}", &file_name);
        }
        files_vec.push(file_name);
    }
    Ok(files_vec)
}

// used to tell user what the error is before closing the cmd prompt
pub fn output_error_to_prompt_and_exit(error_str: &str){
    use std::{thread, time};
    use std::process;
    // write debug report to file
    let debug_file_name = "debug_report.txt".to_string();
    let curent_date_time = chrono::offset::Local::now();
    let error_report = format!("{}\n\n{}\n\n--> send to Mark Wottreng if you need assistance",curent_date_time, error_str);
    file_tools::write_string_to_file(&error_report, &return_current_dir_as_string(), &debug_file_name, 'w', false);
    //
    println!("\n<---------------->\n{}<---------------->\n\n [-->] contant Mark Wottreng if you need assistance",error_str);
    let sleep_time = time::Duration::from_secs(20);
    thread::sleep(sleep_time);
    process::exit(0x0);
    //panic!("Error");
}

// call windows command line functions/commands
pub fn os_cmd_windows(cmd: String, verbose: bool) -> Result<String, std::io::Error> {
    use std::process::Command;
    //let verbose: bool = false;
    //let cmd_str: &str = &cmd[..];
    let output = Command::new("cmd")
        .arg("/C")
        .arg(cmd)
        .output()
        .expect("failed to execute COM process");
    //
    if verbose{
        println!("status: {}", output.status);
        println!("stdout: {}", String::from_utf8_lossy(&output.stdout));
        println!("stderr: {}", String::from_utf8_lossy(&output.stderr));
    }
    let std_out = String::from_utf8_lossy(&output.stdout).to_string();
    let std_err= String::from_utf8_lossy(&output.stderr).to_string();
    if !output.status.success() {
        output_error_to_prompt_and_exit(&std_err[..]);
    }
    Ok(std_out)
}


// call command line functions/commands in Linux
fn os_cmd_linux(cmd: String) -> String {
    use std::process::Command;
    let verbose: bool = true;
    let output = Command::new("bash")
        .arg("-c")
        .arg(cmd)
        .output()
        .expect("failed to execute process");
    //
    if verbose {
        println!("status: {}", output.status);
        println!("stdout: {}", String::from_utf8_lossy(&output.stdout));
        println!("stderr: {}", String::from_utf8_lossy(&output.stderr));
    }
    assert!(output.status.success());
    let std_out = String::from_utf8_lossy(&output.stdout).to_string();
    return std_out;
}

// not used but useful for debugging
pub fn admin_data() {
    use whoami::{username, platform, distro, desktop_env};
    println!("user: {}", username());
    println!("platform: {}", platform());
    println!("distro: {}", distro());
    println!("desktop_env: {}", desktop_env());
}

// return current working directory path as a string
pub fn return_current_dir_as_string()->String{
    use std::env;
    let current_dir_buff = env::current_dir().unwrap();
    let current_dir_string: String = current_dir_buff.into_os_string().into_string().unwrap();
    return current_dir_string;
}
