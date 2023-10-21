use clap::{App, Arg};

fn extract() {
}

fn transform_and_load() {
}

fn general_query(query: &str) {
}

fn main() {
    let matches = App::new("Data Processing Tool")
        .version("1.0")
        .author("Your Name")
        .about("Processes data and executes queries.")
        .arg(
            Arg::with_name("extract")
                .short("e")
                .long("extract")
                .help("Extracts data"),
        )
        .arg(
            Arg::with_name("transform_load")
                .short("tl")
                .long("transform-load")
                .help("Transforms and loads data"),
        )
        .arg(
            Arg::with_name("query")
                .short("q")
                .long("query")
                .value_name("QUERY")
                .help("Executes a general query")
                .takes_value(true),
        )
        .get_matches();

    if matches.is_present("extract") {
        extract();
    } else if matches.is_present("transform_load") {
        transform_and_load();
    } else if let Some(query) = matches.value_of("query") {
        general_query(query);
    }
}
