

def palin(s):
    s = ''.join([i for i in s if i.isalnum()]).replace(" ", "").lower()
    return s == s[::-1]
    


def palindrome(palindrome_string):
    i = 0
    j = len(palindrome_string) - 1


    while i < j:
        while not palindrome_string[i].isalnum() and i < j:
            i += 1

        while not palindrome_string[j].isalnum() and i < j:
            j -= 1

        if palindrome_string[i].lower() != palindrome_string[j].lower():
            return False
        i += 1
        j -= 1
    return True


s = "Was it a cat I saw?"
print(palindrome(s))

print(palin(s))