import requests

def extract(
    url="https://raw.githubusercontent.com/yabeizeng1121/Mini_Project5/main/cars.csv", 
    file_path="cars.csv"
):
    """Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path



