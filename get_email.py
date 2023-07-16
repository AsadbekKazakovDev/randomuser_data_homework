import get_data
import json
from pprint import pprint
def get_email(data:dict) -> list:
    """
    Take the email of the users and return the list.

    Args:
        data(dict): data
    Returns:
        list: users email
    """
    emails = []
    for user in data["results"]:
        emails.append(user["email"])
    return emails
data_json = open("randomuser_data.json","r").read()
data = json.loads(data_json)
print(get_email(data))
        