build:
	cargo build

test:
	cargo test

format:
	cargo fmt

lint:
	cargo clippy

all: build lint test format

extract:
	cargo run -- extract

transform_load: 
	cargo run -- transform-load

query:
	cargo run -- general_query "YOUR QUERY HERE"
