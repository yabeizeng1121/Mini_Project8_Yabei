import os
import requests
import pandas as pd

def extract(
    url="https://github.com/nogibjj/mini_project6_yabei/blob/main/dem_candidates.csv?raw=true",
    url2="https://github.com/nogibjj/mini_project6_yabei/blob/main/rep_candidates.csv?raw=true",
    file_path="data/dem_candidates.csv",
    file_path2="data/rep_candidates.csv",
    directory="data",
):
    """Extract a url to a file path"""
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Download and save the first CSV file
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    
    # Download and save the second CSV file
    with requests.get(url2) as r:
        with open(file_path2, "wb") as f:
            f.write(r.content)
    
    # Read the second CSV file and save a subset of it
    df = pd.read_csv(file_path2)
    df_subset = df.head(121)
    df_subset.to_csv(file_path2, index=False)
    
    return file_path, file_path2

# extract()




