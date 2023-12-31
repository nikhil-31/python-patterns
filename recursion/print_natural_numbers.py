
# Direct recursion - It occurs when a function calls itself
# This results in a 1 step recursive call where a function calls itself inside its own function body



def print_natural_numbers(lower, upper):

    if lower > upper:
        return
    print(lower)
    print_natural_numbers(lower + 1, upper)


print_natural_numbers(100, 200)


# Indirect recursion - When a function calls another function until the original function is called again
def printNaturalNumbers(lowerRange, upperRange):
    if lowerRange <= upperRange:
       print(lowerRange)
       lowerRange += 1
       helperFunction(lowerRange, upperRange)
    else:
       return

def helperFunction(lowerRange, upperRange) :
  if lowerRange <= upperRange :
    print(lowerRange)
    lowerRange += 1
    printNaturalNumbers(lowerRange, upperRange)
  else :
      return

# Driver Program 
n = 5
printNaturalNumbers(1, n)
