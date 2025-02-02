from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    y = data.get("messages")
    list=[]
    
    for i in y:
        for j in i.values():
            if j=='join_group_by_request' or j=='join_group_by_link' or j=='migrate_to_supergroup' or j== 'migrate_from_group' or j=='invite_members':

                a=i.get("actor_id")
                if a not in list:
                    list.append(a)
            

    return list

data=read_data('data/result.json')
print(find_all_users_id(data))


