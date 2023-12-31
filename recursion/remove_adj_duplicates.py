


def remove_adj_duplicates(string):

    if not string:
        return ""
    
    elif len(string) == 1:
        return string
    
    elif string[0] == string[1]:
        return remove_adj_duplicates(string[1:])
    
    else:
        return string[0] + remove_adj_duplicates(string[1:])
    
print(remove_adj_duplicates('Hellloo'))