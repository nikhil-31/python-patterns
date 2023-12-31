from stack import Stack


def reverse_string(input_string):
    stack = Stack()
    reverse = ""

    for i in range(len(input_string)):
        char = input_string[i]
        stack.push(char)


    while not stack.is_empty():
        reverse += stack.pop()
    
    return reverse


print(reverse_string("loluhjg"))