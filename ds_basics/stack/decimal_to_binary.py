
from stack import Stack


def decimal_to_binary(input_decimal):
    stack = Stack()
    binary = list()
    
    while input_decimal > 0:
        remainder = input_decimal % 2
        input_decimal = input_decimal // 2
        stack.push(remainder)


    while not stack.is_empty():
        binary.append(str(stack.pop()))


    return int("".join(binary))


print(decimal_to_binary(242))