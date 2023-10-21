use std::fs;
use std::io::Write;

const LOG_FILE: &str = "query_log.md";

fn log_query(query: &str, result: &str) -> Result<(), Box<dyn std::error::Error>> {
    let mut file = fs::OpenOptions::new().append(true).open(LOG_FILE)?;
    writeln!(file, "```sql\n{}\n```\n", query)?;
    writeln!(file, "```response from databricks\n{}\n```\n", result)?;
    Ok(())
}

fn general_query(query: &str) -> Result<String, Box<dyn std::error::Error>> {

    let result = "Sample result";  

    log_query(query, result)?;

    Ok(result.to_string())
}

fn main() {
    let query = "YOUR SQL QUERY HERE";  
    match general_query(query) {
        Ok(result) => println!("Result: {}", result),
        Err(e) => println!("Error: {}", e),
    }
}
