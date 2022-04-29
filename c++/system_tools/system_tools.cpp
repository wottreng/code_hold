//
// Created by dev on 2022-04-29.
//

#include "system_tools.h"

#include <filesystem>

// note: no trailing slash for dir
std::string system_tools::return_cwd(){
    std::string cwd;
    cwd = std::filesystem::current_path();
    return cwd;
};


