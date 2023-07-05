
"""
CHECK IF THE NUMBER IS A PRIME NUMBER
"""
def is_prime_number(num):
    if num == 1:
        return 1
    
    for i in range(2, num):   
        if num % i == 0:
            flag = True
            break
        else:
            flag = False
    
    if flag:
        print(f"{num} : is not a prime number")
    else:
        print(f"{num} : is a prime number")

# is_prime_number(5)

"""
PRIME NUMBERS IN A RANGE 
"""
def is_prime_number_range(lower, upper):
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)


is_prime_number_range(100, 1000)







