# Mini Project 5

This repository contains the code and resources for Mini Project 5. The project focuses on extracting, transforming, and loading (ETL) operations using Python.

## Overview

- **Extract**: Download data from a given URL.
- **Transform & Load**: Read the downloaded CSV data, transform it, and load it into an SQLite database.
- **Query**: Query the SQLite database and perform various operations.

## Requirements

- Python 3.x
- SQLite
- Additional Python libraries as listed in `requirements.txt`.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yabeizeng1121/Mini_Project5.git
   cd Mini_Project5
   ```

2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the main script to perform ETL operations:
   ```bash
   python main.py
   ```

## Usage

- To extract data, run:
  ```bash
  make extract
  ```

- To transform and load data into the SQLite database, run:
  ```bash
  make transform_load
  ```

- To query the database, simply run the `main.py` script or use the functions provided in the `query.py` module.

## Testing

To run tests, execute:
```bash
make test
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)

---

You can add this content to a `README.md` file in the root directory of your repository. Adjustments can be made based on any additional information or specific details you'd like to include. If you have any other sections or details you'd like to add, please let me know!
