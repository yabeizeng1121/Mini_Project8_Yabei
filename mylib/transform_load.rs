use std::fs;
use csv;

fn load() -> Result<(), Box<dyn std::error::Error>> {
    let mut rdr1 = csv::Reader::from_path("data/performer-scores.csv")?;
    let mut data1: Vec<Vec<String>> = Vec::new();
    for result in rdr1.records() {
        let record = result?;
        data1.push(record.iter().map(|s| s.to_string()).collect());
    }

    let mut rdr2 = csv::Reader::from_path("data/show-data.csv")?;
    let mut data2: Vec<Vec<String>> = Vec::new();
    for result in rdr2.records() {
        let record = result?;
        data2.push(record.iter().map(|s| s.to_string()).collect());
    }



    Ok(())
}

fn main() {
    if let Err(err) = load() {
        println!("Error: {}", err);
    }
}
