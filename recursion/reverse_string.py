
# Iterative 

def reverse_str_iter(input_string):

    result = ""
    string_length = len(input_string) - 1

    while string_length >= 0:
        result += input_string[string_length]
        string_length -= 1
    return result

# Driver Code
targetVariable = "Educative"
print(reverse_str_iter(targetVariable))


# Recursive
def reverse_str_recursive(input_string):
    if len(input_string) == 0:
        return input_string
    
    return reverse_str_recursive(input_string[1:]) + input_string[0]
    

targetVariable = "Educative"
print(reverse_str_recursive(targetVariable))
