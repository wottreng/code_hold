#[macro_use] extern crate rocket;

//#[cfg(test)] mod test_api;

//use rocket::{State, Config};
//use rocket::fairing::AdHoc;
//use rocket::serde::Deserialize;
//

//
//mod json;
//mod msgpack;
//mod uuid;
mod my_api;

#[launch]
fn rocket() -> _ {
    rocket::build()
        .attach(my_api::stage())
}

