//
// Created by dev on 2022-04-28.
//

#ifndef FILE_TOOLS_H
#define FILE_TOOLS_H

#include <string>
class file_tools_h {
public:
    static bool write_string_to_file(std::string data_string, std::string path, std::string file_name);
    static std::string read_string_from_file(std::string path, std::string file_name);

private:

};
#endif //FILE_TOOLS_H
