#include <iostream>
#include "file_tools/file_tools.h"
#include "system_tools/system_tools.h"
#include "excel_tools/excel_tools.h"

//
void test_writing_to_csv_file(){
    std::string data =  "test, hello, 123";
    std::string absolute_path = "/tmp";
    std::string filename = "testing.csv";
    bool completed = excel_tools::write_string_to_csv_file(data, absolute_path, filename);
    if (completed){
        std::cout << "[-->] csv writing successful ✅ \n";
    } else {
        std::cout << "[!] csv writing error ❌ \n";
    }
}
//
void test_reading_csv_file(){
    std::string data;
    std::string absolute_path = "/tmp";
    std::string filename = "testing.csv";
    data = excel_tools::read_string_from_csv_file(absolute_path, filename);
    if (data.length() > 0){
        //std::cout << "csv data: " + data + "\n";
        std::cout << "[-->] file reading successful ✅ \n";
    }else {
        std::cout << "[!] file reading error ❌ \n";
    }
}
//
void test_get_current_working_dir(){
    std::string cwd = system_tools::return_cwd();
    if (cwd.length() > 0){
        //std::cout << cwd + "\n";
        std::cout << "[-->] get cwd successful ✅ \n";
    } else{
        std::cout << "[!] get cwd error ❌ \n";
    }
}
//
void test_file_writing_function(){
    std::string data =  "test hello 123";
    std::string absolute_path = "/tmp";
    std::string filename = "testing.txt";
    bool completed = file_tools_h::write_string_to_file(data, absolute_path, filename);
    if (completed){
        std::cout << "[-->] file writing successful ✅ \n";
    } else {
        std::cout << "[!] file writing error ❌ \n";
    }
}
//
void test_file_reading_function(){
    std::string data;
    std::string absolute_path = "/tmp";
    std::string filename = "testing.txt";
    data = file_tools_h::read_string_from_file(absolute_path, filename);
    if (data.length() > 0){
        //std::cout << "file data: " + data + "\n";
        std::cout << "[-->] file reading successful ✅ \n";
    }else {
        std::cout << "[!] file reading error ❌ \n";
    }
}
// -----------
int main() {
    std::cout << "[*] start system_tools testing \n";
    test_get_current_working_dir();
    //
    std::cout << "[*] start file_tools testing \n";
    test_file_writing_function();
    test_file_reading_function();
    //
    std::cout << "[*] start excel_tools testing \n";
    test_writing_to_csv_file();
    test_reading_csv_file();
    //
    return 0;
}

