
#[tokio::main]
async fn get_json_data() -> Result<(), Box<dyn std::error::Error>> {
    // Build the client using the builder pattern
    let client = reqwest::Client::builder().build()?;

    // Perform the actual execution of the network request
    let res = client
        .get("https://httpbin.org/ip")
        .send()
        .await?;

    // return response as text
    let ip = res.text().await?;
    println!("{:?}", ip);
    // --
    // use serde to turn string into json struct
    use serde::{Serialize, Deserialize};
    #[derive(Serialize, Deserialize)]
    struct RespJson {
        origin: String
    }
    let parsed_json: RespJson = serde_json::from_str(&ip)?;
    println!("{:?}", parsed_json.origin);
    Ok(())
}

fn main(){
    let rez = get_json_data().unwrap();
    println!("request status: {:?}", rez);
}

