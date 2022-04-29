cmake_minimum_required(VERSION 3.21)
project(file_tools)

set(CMAKE_CXX_STANDARD 20)

add_executable(file_tools test.cpp file_tools/file_tools.cpp file_tools/file_tools.h )
