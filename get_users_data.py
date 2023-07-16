import get_data

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
    dt = {}
    lst_data = []
    for n in range(len(data['results'])):
        dt['first_name'] = data['results'][n]['name']['first']
        dt['last_name'] = data['results'][n]['name']['last']
        dt['phone_number'] = data['results'][n]['phone']
        dictionary = dt.copy()
        lst_data.append(dictionary)
    return lst_data


data = get_data.get_data('randomuser_data.json')
print(get_users_data(data))