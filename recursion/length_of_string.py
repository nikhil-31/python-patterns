

def len_of_string(string):

    if string == "":
        return 0
    
    return 1 + len_of_string(string[1:])

# Driver Code 
testVariable = "Educative"
print (len_of_string(testVariable)) 





