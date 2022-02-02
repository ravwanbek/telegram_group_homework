from os import remove
from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    y = data.get("messages")
    list=[]
    
    for i in y:
        for j in i.values():
            if j==users_id:
                a=i.get("type")
                list.append(a)
    
    msg_list=[]
    for g in list:
        if g=='message':
            msg_list.append(g)
    
    return len(msg_list)

    
data=read_data('data/result.json')
users_idd=find_all_users_id(data)
users_id=str(users_idd[10])
print(find_user_message_count(data,users_id))
