package file_tools

import (
	"fmt"
	"log"
	"os"
)

func Ft_testing() {
	fmt.Println("[*] start file_tools testing")
	//
	data := "test 123"
	path := "/tmp"
	file_name := "go_test.txt"
	status := Write_string_to_file(data, path, file_name)
	if status == true {
		fmt.Println("[-->] writing complete ✓")
	} else {
		fmt.Println("[-->] writing error")
	}
	//
	data_string := read_string_from_file(path, file_name)
	if len(data_string) > 0 {
		//fmt.Println("file data: " + data_string)
		fmt.Println("[-->] reading complete ✓")
	} else {
		fmt.Println("[-->] reading error")
	}
}

func read_string_from_file(path string, file_name string) string {
	var string_data string
	absolute_path := path + "/" + file_name
	byte_data, err := os.ReadFile(absolute_path)
	if err != nil {
		fmt.Println("[-->] File reading error", err)
		return ""
	}
	string_data = string(byte_data)
	//fmt.Println("Contents of file:", string_data)
	return string_data
}

func Write_string_to_file(data_string string, path string, file_name string) bool {
	absolute_path := path + "/" + file_name
	file, err := os.Create(absolute_path)

	if err != nil {
		log.Fatal(err)
	}

	defer func(file *os.File) {
		err := file.Close()
		if err != nil {
			log.Fatal(err)
		}
	}(file)

	_, err2 := file.WriteString(data_string + "\n")

	if err2 != nil {
		log.Fatal(err2)
	}

	//fmt.Println("done")
	return true
}

// function for writing data to file
func Write_data_to_file(data []byte, path string, file_name string) bool {
	absolute_path := path + "/" + file_name
	file, err := os.Create(absolute_path)

	if err != nil {
		log.Fatal(err)
	}

	defer func(file *os.File) {
		err := file.Close()
		if err != nil {
			log.Fatal(err)
		}
	}(file)

	_, err2 := file.Write(data)

	if err2 != nil {
		log.Fatal(err2)
	}

	//fmt.Println("done")
	return true
}
