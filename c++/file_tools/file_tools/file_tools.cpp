//
// Created by dev on 2022-04-28.
//

#include "file_tools.h"

#include <iostream>
#include <string>
#include <fstream>

using namespace std;


bool file_tools_h::write_string_to_file(std::string data_string, std::string path, std::string file_name) {
    if (data_string.length() > 0) {
        string full_path = path + "/" + file_name;
        std::ofstream file(full_path);
        file << (data_string + "\n");
        file.close();
        return true;
    } else {
        return false;
    }
}

std::string file_tools_h::read_string_from_file(std::string path, std::string file_name){
    string full_path = path + "/" + file_name;
    std::ifstream output_stream(full_path);

    if (output_stream.fail()) {
        throw std::runtime_error("Failed to open file");
    }

    std::string data;
    std::string buffer;

    if (output_stream.is_open())
    {
        while ( getline (output_stream,buffer) )
        {
            data += buffer + '\n';
        }
        output_stream.close();
    }

    return data;
}
