


def remove(string):


    if not string:
        return ""
    
    if string[0] == "\t" or string[0] == " ":
      return remove(string[1:])
    else:
      return string[0] + remove(string[1:])
    

print(remove("Hello\tWorld"))