package multithreading

/*
notes: go coroutines are not true os threads. they all compete for cpu time.
*/

import (
	"fmt"
	"sync"
)

func Mt_testing() {
	fmt.Println("[*] start multithreading testing")
	//
	var wg sync.WaitGroup
	//
	for i := 1; i <= 20; i++ {
		wg.Add(1)
		go test_func(&wg, i)
	}
	fmt.Println("waiting for all threads")
	wg.Wait()
	//
	if true {
		fmt.Println("[-->] success ✓ \n")
	} else {
		fmt.Println("[!] get cwd error")
	}
}

// test func for multithreading
func test_func(wg *sync.WaitGroup, a_input int) bool {
	defer wg.Done()
	//
	var a_value int64 = 0
	var i int64
	for i = 1; i < 2000000000; i++ {
		a_value += i
	}
	fmt.Println("finished", a_input)
	return true
}
