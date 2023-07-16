import json

def get_data(filename:str) -> dict:
    """
    You are given a filename. Read the JSON data from the file and return the dictionary.

    Args:
        filename(str): file name
    Returns:
        dict: JSON data
    """
    f = open(filename).read()
    return json.loads(f)
filename = open("randomuser_data.json","r").read()
print(get_data(filename))