#Write a simple interpreter which understands "+", "-", and "*" operations.
#Apply the operations in order using command/arg pairs starting with the
#initial value of `value`. If you encounter an unknown command, return -1. 
#interpret(1, ["+"], [1]) → 2 
#interpret(4, ["-"], [2]) → 2
#interpret(1, ["+", "*"], [1, 3]) → 6

def combine(value1, command, value2):
    if command == "+":
        return value1 + value2
    if command == "-":
        return value1 - value2
    if command == "*":
        return value1 * value2


def interpret(value, commands, args):
    total = 0
    for index, command in enumerate(commands):
        if command != "+" and command != "*" and command != "-":
            return -1
        if index == 0:
            total = combine(value, command, args[0])
        else:
            total = combine(total, command, args[index])
    return total

print(interpret(1, ['+'], [1]))
print(interpret(4, ['-'], [2]))
print(interpret(1, ['+', '*'], [1, 3]))