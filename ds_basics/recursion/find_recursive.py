

def find_uppercase_iterative(input_self):
    for i in range(len(input_self)):
        if input_self[i].isupper():
            return input_self[i]
    
    return False


def find_uppercase_recursive(input_self, idx = 0):

    if input_self[idx].isupper():
        return input_self[idx]
    
    if idx == len(input_self) - 1:
        return "No uppercase char found"
    
    return find_uppercase_recursive(input_self, idx + 1)


input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"

print(find_uppercase_iterative(input_str_1))
print(find_uppercase_iterative(input_str_2))
print(find_uppercase_iterative(input_str_3))

print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))
