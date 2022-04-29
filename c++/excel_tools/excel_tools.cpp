//
// Created by dev on 2022-04-29.
//

#include "excel_tools.h"

#include <string>
#include <iostream>
#include <fstream>

// filename needs .csv in name, data_string seperated by commas
bool excel_tools::write_string_to_csv_file(const std::string& data_string,const std::string& path,const std::string& file_name){
    if (data_string.length() > 0) {
        std::string full_path = path + "/" + file_name;
        std::fstream csv_file(full_path);
        csv_file << (data_string) << std::endl;
        csv_file.close();
        return true;
    } else {
        return false;
    }
};

std::string excel_tools::read_string_from_csv_file(const std::string& path, const std::string& file_name){
    std::string full_path = path + "/" + file_name;
    std::fstream csv_file(full_path);

    if (csv_file.fail()) {
        throw std::runtime_error("Failed to open file");
    }

    std::string data;
    std::string buffer;

    if (csv_file.is_open())
    {
        while ( getline (csv_file,buffer) )
        {
            data += buffer + '\n';
        }
        csv_file.close();
    }

    return data;


};

