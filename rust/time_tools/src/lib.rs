/*
time tools
written by Mark Wottreng
 */

use std::time::{SystemTime, UNIX_EPOCH};

// format ex.: 2022-05-03 13:41:37
pub fn return_date_time_now() -> String{
    let date_time_whole = chrono::offset::Local::now().to_string();
    let decimal_index = date_time_whole.find('.');
    if decimal_index > Some(0) {
        let mut date_time_string = String::new();
        let char_vec: Vec<char> = date_time_whole.chars().collect();
        for i in 0..decimal_index.unwrap() {
            date_time_string += &char_vec[i].to_string();
        }
        return date_time_string
    } else {
        return date_time_whole // format: 2022-05-03 13:41:37.013890581 -04:00
    }
}

// format ex.: 2022-05-03
pub fn return_date_now() -> String{
    let date_whole = chrono::offset::Local::today().to_string();
    let decimal_index = date_whole.find(':');
    if decimal_index > Some(0) {
        let mut date_string = String::new();
        let char_vec: Vec<char> = date_whole.chars().collect();
        for i in 0..(decimal_index.unwrap()-3) {
            date_string += &char_vec[i].to_string();
        }
        return date_string
    } else {
        return date_whole
    }
}

// return seconds from epoch. format ex.: 1651600833
pub fn return_epoch_time() -> String {
    let since_the_epoch = SystemTime::now()
        .duration_since(UNIX_EPOCH).unwrap();
    //println!("{:?}", since_the_epoch);
    let whole_epoch_string = format!("{:?}",since_the_epoch); // format: 1651600833.830837923s
    let decimal_index = whole_epoch_string.find('.');
    if decimal_index > Some(0){
        let char_vec: Vec<char> = whole_epoch_string.chars().collect();
        let mut epoch_string = String::new();
        for i in 0..decimal_index.unwrap(){
            epoch_string += &char_vec[i].to_string();
        }
        return epoch_string // format: 1651600833
    }else {
        return whole_epoch_string // format: 1651600833.830837923s
    }
}

//
pub fn see_outputs(){
    let date_time = return_date_time_now();
    println!("date and time: {}",date_time);
    //
    let epoch_time = return_epoch_time();
    println!("epoch: {}",epoch_time);
    //
    let date = return_date_now();
    println!("date: {}",date);
}

// ======== TESTS ===================
#[cfg(test)]
mod time_tools_tests {
    use crate::{return_date_time_now, return_epoch_time, return_date_now};

    #[test]
    fn date_time() {
        let date_time = return_date_time_now();
        if date_time.len() == 19{
            assert!(true);
        } else {
            panic!("date_time is wrong length");
        }
    }
    //
    #[test]
    fn date() {
        let date = return_date_now();
        if date.len() == 10{
            assert!(true);
        } else {
            panic!("date is wrong length");
        }
    }
    //
    #[test]
    fn epoch(){
        let epoch_time = return_epoch_time();
        if epoch_time.len() == 10{
            assert!(true);
        } else {
            panic!("epoch_time is wrong length");
        }
    }
}
