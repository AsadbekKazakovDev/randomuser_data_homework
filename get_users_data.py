import get_data
import json
from pprint import pprint
def get_users_data(data:dict) -> list:
    """
    Take the data of the first name, last name and phone number. Return the list.
    
    The list items are as follows:
        {"first_name": "Dominic", "last_name":"Warholm", "phone_number": "27707465"}

    Args:
        data(dict): data
    Returns:
        list: users data list
    """
    lst = []
    for user in data["results"]:
        data = {
            "first_name":user["name"]["first"],
            "last_name":user["name"]["last"],
            "phone_number":user["phone"]
        }
    lst.append(data)
    return lst

data_json = open("randomuser_data.json","r").read()
data = json.loads(data_json)
pprint(get_users_data(data))