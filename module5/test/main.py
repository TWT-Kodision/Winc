def get_none():
    return None

def flatten_dict(dictionary):
    item_list = []
    for item in dictionary.values():
        item_list.append(item)
    return item_list


