
import get_data
import json

def get_count_users(data: dict) -> int:
    """
    You are given dictionary. Find the number of users.

    Args:
        data(dict): data
    Returns:
        int: number of users
    """
    sum = 0
    for user in data['results']:
        sum+=1
    return sum

data_json = open('randomuser_data.json','r').read()
data = json.loads(data_json)
print(get_count_users(data))
    
