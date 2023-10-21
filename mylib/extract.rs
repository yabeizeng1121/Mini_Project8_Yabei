use std::fs;
use reqwest;
use csv;

const URL1: &str = "https://github.com/nogibjj/mini_project6_yabei/blob/main/data/data/performer-scores.csv?raw=true";
const URL2: &str = "https://github.com/nogibjj/mini_project6_yabei/blob/main/data/data/show-data.csv?raw=true";
const FILE_PATH1: &str = "data/performer-scores.csv";
const FILE_PATH2: &str = "data/show-data.csv";
const DIRECTORY: &str = "data";

fn extract() -> Result<(String, String), Box<dyn std::error::Error>> {
    if !fs::metadata(DIRECTORY).is_ok() {
        fs::create_dir_all(DIRECTORY)?;
    }

    let content1 = reqwest::blocking::get(URL1)?.bytes()?;
    fs::write(FILE_PATH1, content1)?;

    let content2 = reqwest::blocking::get(URL2)?.bytes()?;
    fs::write(FILE_PATH2, content2)?;

    let mut rdr = csv::Reader::from_path(FILE_PATH2)?;
    let mut wtr = csv::Writer::from_path(FILE_PATH2)?;
    for (i, result) in rdr.records().enumerate() {
        if i >= 121 {
            break;
        }
        let record = result?;
        wtr.write_record(&record)?;
    }

    Ok((FILE_PATH1.to_string(), FILE_PATH2.to_string()))
}

fn main() {
    match extract() {
        Ok((path1, path2)) => println!("Files saved to {} and {}", path1, path2),
        Err(e) => println!("Error: {}", e),
    }
}
