# clean the data in the dictionary


# function takes a list of dictionaries


def remove_empty(list_of_dict):
    # this code avoids "Runtime Error dictionary changed size during iteration"
    # filter out key/value pairs with empty values and populate a list with these edited dictionaries
    clean_list = []
    for a_dict in list_of_dict:
        clean_list.append({k: v for k, v in a_dict.items() if v != ''})
    return clean_list

