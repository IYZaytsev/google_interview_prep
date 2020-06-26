#Given a string, return the sum of the numbers appearing in the string, 
#ignoring all other characters. A number is a series of 1 or more digit chars in a row. 
#(Note: Character.isDigit(char) tests if a char is one of the chars '0', '1', .. '9'. 
#Integer.parseInt(string) converts a string to an int.)
#sumNumbers("abc123xyz") → 123
#sumNumbers("aa11b33") → 44
#sumNumbers("7 11") → 18

def sumNumbers(str):
    temp_string = ""
    nums = []
    for char in str:
        if char.isdigit():
            temp_string += char
        if not char.isdigit() and temp_string.isdigit():
            nums.append(int(temp_string))
            temp_string = ""
    #handling case when number is the last seqence in the string
    if temp_string.isdigit():
        nums.append(int(temp_string))
    sum = 0
    for num in nums:
        sum += num
    return sum

print(sumNumbers("abc123xyz"))