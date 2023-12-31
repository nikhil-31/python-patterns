
# Iterative 


def is_vowel(charater):
    
    charater = charater.lower()
    vowels = "aeiou"

    if charater in vowels:
        return 1
    else:
        return 0    


def count_vowels_iterative(string):

    count = 0

    for i in range(len(string)):
        if is_vowel(string[i]):
            count += 1
    return count

# Driver code 
string = "Educative"
print(count_vowels_iterative(string)) 

def count_vowels_recursively(string, n):
    if n == 0:
        return 0
    
    if n == 1:
        return is_vowel(string[0])
    
    return count_vowels_recursively(string, n - 1) + is_vowel(string[n - 1])

# # Driver code 
string = "Educative"
print(count_vowels_recursively(string, len(string))) 







