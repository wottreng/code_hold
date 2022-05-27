package main

import (
	"file_tools"
	"fmt"
)

func main() {
	//mt.Mt_testing()
	a := 5
	b := &a // pointer to mem addr
	fmt.Println("test ", *&a)
	fmt.Println(*b)
	//
	file_tools.Ft_testing()
}
