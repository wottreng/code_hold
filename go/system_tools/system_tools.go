package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("[*] start system_tools testing")
	//
	cwd := Return_cwd_as_string()
	if len(cwd) > 0 {
		fmt.Println("[-->] get cwd success ✓ \n", cwd)
	} else {
		fmt.Println("[!] get cwd error")
	}
	//
	println("does tmp exist: ", Check_if_directory_exists("/tmp"))
	//
	println("does /tmp/test_file exist: ", Check_if_file_exists("/tmp/test_file"))
}

// note: cwd has no trailing slash
func Return_cwd_as_string() string {
	var cwd string
	cwd, err := os.Getwd()
	if err != nil {
		fmt.Println("[-->] system error: ", err)
		return ""
	}
	return cwd
}

// check if a file exists
func Check_if_file_exists(file_path string) bool {
	if _, err := os.Stat(file_path); err == nil {
		return true
	} else {
		return false
	}
}

// check if a directory exists
func Check_if_directory_exists(directory_path string) bool {
	if _, err := os.Stat(directory_path); err == nil {
		return true
	} else {
		return false
	}
}
