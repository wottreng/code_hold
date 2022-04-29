package main

import (
	"fmt"
	"time"
)

// credit:
// https://github.com/jakewright/tutorials/tree/master/go/02-go-concurrency

func main() {
	go count("sheep")
	fmt.Println("Hello, World!")
	time.Sleep(time.Second * 5)
}

func count(thing string) {
	for i := 1; i <= 5; i++ {
		fmt.Println(i, thing)
		time.Sleep(time.Second * 1)
	}
}
