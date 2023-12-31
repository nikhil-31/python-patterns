

integer = 123

binary = format(integer, 'b')
print(binary)



positive = 123
binary = bin(positive)
print(binary)

# Returns: '0b1111011'

def int_to_binary(integer):

    binary_string = ''
    while integer > 0:

        digit = integer % 2
        binary_string += str(digit)
        integer = integer // 2

    return binary_string[::-1]

print(int_to_binary(123))