"""
Convert
"""

def roman_to_numbers(roman_str: str):
    """
    Convert a roman string to integers
    """
    roman_to_number_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    total = 0
    length_of_roman_str = len(roman_str) - 1

    for index, char in enumerate(roman_str):
        if (length_of_roman_str >= (index + 1)) and \
                (roman_to_number_map[char] < roman_to_number_map[roman_str[index + 1]]):
            total = total - roman_to_number_map[char]
        else:
            total = total + roman_to_number_map[char]
    return total

print(roman_to_numbers(roman_str="XXI"))
