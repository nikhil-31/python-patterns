
def decimal_to_binary(test_variable):

    if test_variable <= 1:
        return str(test_variable)
    
    else:
        return decimal_to_binary(test_variable // 2) + decimal_to_binary(test_variable % 2)


test_variable = 11
print(decimal_to_binary(11))