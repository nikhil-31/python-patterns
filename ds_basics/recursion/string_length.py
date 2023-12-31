

def iterative_str_length(input_str):

    input_str_length = 0

    for i in range(len(input_str)):
        input_str_length += 1

    return input_str_length


def recursive_str_length(input_str):
    if input_str == '':
        return 0
    
    return 1 + recursive_str_length(input_str[1:])

input_str = "LucidProgramming"

print(iterative_str_length(input_str))
print(recursive_str_length(input_str))




