package main

import (
	"fmt"
	"os"
)

func main() {
	fmt.Println("[*] start system_tools testing")
	//
	cwd := return_cwd_as_string()
	if len(cwd) > 0 {
		fmt.Println("[-->] get cwd success ✓ \n", cwd)
	} else {
		fmt.Println("[!] get cwd error")
	}
}

// cwd has no trailing slash
func return_cwd_as_string() string {
	var cwd string
	cwd, err := os.Getwd()
	if err != nil {
		fmt.Println("[-->] system error: ", err)
		return ""
	}
	return cwd
}
