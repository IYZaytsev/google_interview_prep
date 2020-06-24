import collections

# Given a string S and a set of words D, 
# find the longest word in D that is a subsequence of S.

#S = "abpplee"
#D = {"able", "ale", "apple", "bale", "kangaroo"}

S = "abppplee"
D = {"able", "ale", "apple", "bale", "kangaroo"}

#S = "aaaspigsss"
#D = {"pink", "aa", "pig"}
longest_seq = ""

letter_positions = collections.defaultdict(list)
for index, letter in enumerate(S):
    letter_positions[letter].append(index)

# go over all words in dictionary
# first on found will be the longest since it is a sorted dictionary
found_word = ""
for word in sorted(D, key=lambda w: len(w), reverse=True):
    pos = 0
    count = 0
    if found_word != "":
        print(f"longest word is {found_word}")
        break

    for letter in word:
        if letter not in letter_positions:
            break
        possible_positions = letter_positions[letter]
        for index in possible_positions:
            if index >= pos:
                pos = index
                count += 1
                break
        if count == len(word):
            found_word = word
            break
        
             
    

    