/*
concurrency example
 */
use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    println!("[*] start concurrency example");
    //
    let (tx,rx) = mpsc::channel();
    let tx2 = tx.clone();

    let data0 = vec![1,2,3,4];
    let data1 = vec![6,7,8,9,10];

    thread::spawn(move ||   {
        let vals = data0;

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }

    });

    thread::spawn(move ||   {
        let vals2 = data1;

        for val in vals2 {
            tx2.send(val).unwrap();
            //thread::sleep(Duration::from_secs(1));
        }

    });

    for received in rx {
        //let received = rx.recv().unwrap();
        println!("got: {:?}", received);
    }

}
