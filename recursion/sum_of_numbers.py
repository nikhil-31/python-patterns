

def sum_of_no_in_str(string):

    if string == "":
        return 0
    
    return int(string[0]) + sum_of_no_in_str(string[1:])


print(sum_of_no_in_str("345"))


