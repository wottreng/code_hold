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

    thread::spawn(move ||   {
        let vals = vec![1,2,3,4,5];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }

    });

    thread::spawn(move ||   {
        let vals = vec![6,7,8,9,10];

        for val in vals {
            tx2.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }

    });

    for received in rx {
        //let received = rx.recv().unwrap();
        println!("got: {:?}", received);
    }

}
