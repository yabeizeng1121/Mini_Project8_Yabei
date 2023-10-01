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

## Results Preview
![08656825e304ab7a3c3c217a4dd1f22](https://github.com/nogibjj/Mini_Project5_Yabei_New/assets/143656459/b0596f73-cc4a-4c0e-97f4-4910a0fe2f43)
![148ab7de7d724fd90f491a1a67f9f00](https://github.com/nogibjj/Mini_Project5_Yabei_New/assets/143656459/63194df8-567c-44ab-8b13-156db3bd87cd)
![259df8d8d44e9a8ef66399f6f084403](https://github.com/nogibjj/Mini_Project5_Yabei_New/assets/143656459/88f7111e-0201-4dcc-b804-2aecaea7a83c)
![ef195efeb89e1cb56eade39a0d81e29](https://github.com/nogibjj/Mini_Project5_Yabei_New/assets/143656459/7477bafb-a6c4-44e4-94f2-35c3c20b55bb)
![ff84b1627c3ddcb95e91619a4af6dbb](https://github.com/nogibjj/Mini_Project5_Yabei_New/assets/143656459/f7ac6671-ee3e-49d9-b66b-d7e431cae4fa)


## Reference
https://github.com/nogibjj/sqlite-lab
