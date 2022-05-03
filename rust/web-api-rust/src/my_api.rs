use std::borrow::Cow;
use rocket::State;
use rocket::tokio::sync::Mutex;
use rocket::serde::json::{Json, Value, json};
use rocket::serde::{Serialize, Deserialize};

// The type to represent the ID of a message.
type Id = usize;

// We're going to store all of the messages here. No need for a DB.
type MessageList = Mutex<Vec<String>>;
type Messages<'r> = &'r State<MessageList>;

#[derive(Serialize, Deserialize)]
#[serde(crate = "rocket::serde")]
struct Message1<'r> {
    id: Option<Id>,
    message: Cow<'r, str>
}

//
#[post("/", format = "json", data = "<xxx>")]
async fn api0(xxx: Json<Message1<'_>>) -> Value {
    json!({ "status": "ok", "id": xxx.id, "message": xxx.message})
}

//
#[post("/debug", data = "<xxx>")]
async fn debug(xxx: String) -> String {
    //println!("data: {}",xxx);
    let cam_mac = "12:34:56:78:ab:12";
    if xxx.find(cam_mac) > Some(0) {
        //write to file
        let data_string: String = chrono::offset::Local::now().to_string();
        let path = String::from("/tmp");
        let file_name = String::from("alert.txt");
        file_tools::write_string_to_file(&data_string, &path, &file_name, 'a', false);
        //
    }
    return "ok".to_string()
}

//
#[get("/<id>", format = "json")]
async fn get0(id:String) -> String {

    format!("test id: {}",id)
}

#[catch(404)]
fn not_found1() -> Value {
    json!({
        "status": "error",
        "reason": "Resource was not found."
    })
}

pub fn stage() -> rocket::fairing::AdHoc {
    rocket::fairing::AdHoc::on_ignite("my_json!", |rocket| async {
        rocket.mount("/api", routes![api0, get0, debug])
            .register("/api", catchers![not_found1])
            .manage(MessageList::new(vec![]))
    })
}
// --------------- TESTS -------------------------------
#[cfg(test)]
use rocket::local::blocking::Client;
use rocket::http::{Status, ContentType, Accept};

//
#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[serde(crate = "rocket::serde")]
struct Message {
    id: Option<usize>,
    message: String
}

impl Message {
    fn new(message: impl Into<String>) -> Self {
        Message { message: message.into(), id: None }
    }

    fn with_id(mut self, id: usize) -> Self {
        self.id = Some(id);
        self
    }
}
//
#[test]
fn api_get_req(){
    let client = Client::tracked(super::rocket()).unwrap();
    let res = client.get("/api/0").header(ContentType::JSON).dispatch();
    assert_eq!(res.status(), Status::Ok);
}
#[test]
fn api_post_req(){
    let client = Client::tracked(super::rocket()).unwrap();
    let message = format!("Hello, 2c:a5:9c:f7:d0:09! alert!");
    let res = client.post("/api/debug").body(&message).dispatch();
    assert_eq!(res.status(), Status::Ok);
}
#[test]
fn api_post_req1(){
    let id = 1;
    let message = Message::new(format!("Hello, JSON {}!", id));
    let client = Client::tracked(super::rocket()).unwrap();
    let res = client.post("/api").json(&message).dispatch();
    assert_eq!(res.status(), Status::Ok);
}


