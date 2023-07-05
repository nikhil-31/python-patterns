

# Pythonic way of creating palindrome 
def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("palindromeemordnilap"))


## Palindrome using recursion
def is_palindrome_2(word):
    if len(word) <= 1:
        return True
    else:
        return word[0] == word[-1] and is_palindrome_2(word[1: -1]) 

print(is_palindrome_2("palindromeemordnilap"))