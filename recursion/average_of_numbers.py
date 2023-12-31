

def average(test_variable, current_index=0):

    if current_index == (len(test_variable) - 1):
        return test_variable[current_index]
    
    if current_index == 0:
        return (test_variable[current_index] + average(test_variable, current_index + 1)) / len(test_variable)
    
    return (test_variable[current_index] + average(test_variable, current_index + 1))

arr = [10, 2, 3, 4, 8, 0] 
print(average(arr)) 


