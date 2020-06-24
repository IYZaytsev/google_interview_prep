
#Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):

    returnstring = ""
    for index, letter in enumerate(str):
        for i in range(0, index + 1):
            if (i > len(str)-1):
                break
            else:
                returnstring += str[i]
    return returnstring

def better_string_splosion(str):
    result = ""
    # on each iteration, add the substring of the char 0..i
    for i in range(len(str)):
        result += str[:i+1]
    return result
    
print(string_splosion("Code"))
print(better_string_splosion("Code"))