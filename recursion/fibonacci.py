

def fibonacci_itr(input_number):
    fb0 = 0
    fb1 = 1

    for i in range(0, input_number):
        temp = fb0 + fb1

        fb0 = fb1
        fb1 = temp

    return fb0

# Driver Code
testVariable = 7
print(fibonacci_itr(testVariable))




def fibonacci(input_number):

    if input_number <= 1:
        return input_number
    
    return(fibonacci(input_number - 1) + fibonacci(input_number - 2 ))


testVariable = 7
print(fibonacci(testVariable))