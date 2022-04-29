#include <iostream>
#include "file_tools/file_tools.h"

void test_file_writing_function(){
    std::string data =  "test hello 123";
    std::string absolute_path = "/tmp";
    std::string filename = "testing.txt";
    file_tools_h ft;
    bool completed = ft.write_string_to_file(data, absolute_path, filename);
    if (completed){
        std::cout << "[-->] file writing successful ✅ \n";
    } else {
        std::cout << "[!] file writing error ❌ \n";
    }
}

void test_file_reading_function(){
    std::string data;
    std::string absolute_path = "/tmp";
    std::string filename = "testing.txt";
    file_tools_h ft;
    data = ft.read_string_from_file(absolute_path, filename);
    if (data.length() > 0){
        std::cout << data + "\n";
        std::cout << "[-->] file reading successful ✅ \n";
    }else {
        std::cout << "[!] file reading error ❌ \n";
    }
}


int main() {
    std::cout << "[*] start file_tools testing" << std::endl;
    //
    test_file_writing_function();
    //
    test_file_reading_function();
    //
    return 0;
}

