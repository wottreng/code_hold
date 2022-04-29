//
// Created by dev on 2022-04-29.
//

#ifndef FILE_TOOLS_EXCEL_TOOLS_H
#define FILE_TOOLS_EXCEL_TOOLS_H

#include <string>

class excel_tools {
public:
    static bool write_string_to_csv_file(const std::string& data_string,const std::string& path,const std::string& file_name);
    static std::string read_string_from_csv_file(const std::string& path, const std::string& file_name);
private:

};


#endif //FILE_TOOLS_EXCEL_TOOLS_H
