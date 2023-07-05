"""
Texting on a phone (the ones before smartphone :) )
This question should ideally be asked of a Senior engineer
If you recall, the physical keyboard of a non-smart phone would be something like this:
| 1        | 2 (abc) | 3 (def)  |
| 4 (ghi)  | 5 (jkl) | 6 (mno)  |
| 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
|     *    | 0 ( )   |     #    |


In this, if a person pressed the key “2” once, the screen would print “a”.
On pressing “2” twice, the screen would show “b” and “c” on pressing thrice.
For pressing “1”, the screen would print nothing, while pressing “0” would
print one space (“ “) character.
Now, given this, write a method – key_print — which accepts a sequence of
key-strokes and outputs the text that would be printed on the screen.

Input:
keyPrint("12345")
Output:
'adgj'


Input:
keyPrint("2022")
Output:
'a b'

Input:
keyPrint("4433555555666")
Output:
'hello'

Follow-up questions:
- write 2 test-cases to assert that the method is working as expected.
"""

def sms_with_keypad(key_input):
    """
    This converts an sms into a string
    """

    def get_keypad_map(key_str, counter):
        keypad_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        print(f'Key input {key_input}')
        if key_str in keypad_map:
            alphabets = keypad_map[key_str]
            text = alphabets[counter]
            print(f"All alphabets {alphabets} and text {text} and counter {counter}")


    prev_key = ""
    prev_key_counter = 0
    i = 0
    while i < len(key_input):
        current_key = key_input[i]
        if prev_key == current_key:
            prev_key_counter += 1
        else:
            print(f"prev key {prev_key} prev key counter {prev_key_counter}")
            get_keypad_map(prev_key, prev_key_counter)
            prev_key_counter = 0
            prev_key = current_key

        if len(key_input) != 0:
            pass
        
        i += 1

sms_with_keypad("222333")
