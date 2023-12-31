


def duplicates(string):

    stack = []

    for char in string:
        
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)



string = "aallssbbb"

print(duplicates(string))



