/*
matlab related functions
written by Mark Wottreng
 */

// execute matlab code script to output data structure into text files in `data_files` directory
// BUG report -> matlab wont run headless in directory with spaces in path name
pub fn save_debug_catalyst_file(working_directory: &String) {
    let cmd1 = "matlab_code"; // name of matlab .m file
    // check if space in directory and exit if so... MATLAB BUG
    if working_directory.contains(char::is_whitespace) {
        let msg = format!("[!] working directory has spaces in name! \n  This causes MATLAB to crash!\n  remove all spaces from working_directory and try again. Thanks MATLAB... \n --> working directory: {}\n", working_directory);
        system_tools::output_error_to_prompt_and_exit(&msg[..]);
    }
    // format matlab cmd
    let mat_cmd = format!("matlab -sd \"{}\" -batch \"{}\"", working_directory, cmd1);
    //println!("mat cmd: {}",mat_cmd);
    // run matlab headless via COM
    let resp = system_tools::os_cmd(mat_cmd, false).unwrap();
    if resp.len() > 0 {
        println!("{}", resp); // output errors to cmd prompt
    }
}

// return matlab code string for writing into a file
// this is used for extracting .mat files into text files
pub fn return_matlab_code(debug_file_name: &str) -> String {
    let cmd =
        format!("%pwd;
    %dir(pwd);
    filename = '{}';
    load(filename);
    filename_split = split(filename,'.');
    struct_name = filename_split(1);
    fields = fieldnames(eval(char(struct_name)));
    for i=1 : numel(fields)
        %disp(fields(i))
        txt_file_name = strcat('data_files\\',char(struct_name),'-',char(fields(i)),'.txt');
        %disp(txt_file_name);
        writematrix(eval(char(struct_name)).(fields{{i}}), txt_file_name);
    end
    % ", debug_file_name);
    return cmd;
}
