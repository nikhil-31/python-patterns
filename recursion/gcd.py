

def gcd(test_variable_1, test_variable_2):

    if test_variable_1 == test_variable_2:
        return test_variable_1
    
    if test_variable_1 > test_variable_2:
        return gcd(test_variable_1 - test_variable_2, test_variable_2)
    else:
        return gcd(test_variable_1, test_variable_2 - test_variable_1)

number1 = 6
number2 = 9
print(gcd(number1, number2))