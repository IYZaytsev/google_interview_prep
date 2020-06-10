import collections

# Given a string S and a set of words D, 
# find the longest word in D that is a subsequence of S.

#S = "abpplee"
#D = {"able", "ale", "apple", "bale", "kangaroo"}

S = "ffaakjdnadpigddd"
D = {"shit", "fuck", "pig"}
longest_seq = ""

# go over all words in dictionary
# first on found will be the longest since it is a sorted dictionary
for word in sorted(D, key=lambda w: len(w), reverse=True):
    num_let = len(word)
    pos = 0
    if longest_seq != "":
        print(longest_seq)
        break 
    # breaks out if word contains character that don't exist 
    # in the string
    for letter in word:
        if letter not in S:
            break
        for index in range(0, len(S)):
            if (S[index] == letter and (pos == 0)and num_let != 0):
                pos = index
                num_let = num_let - 1
            if (S[index] == letter and pos != index and num_let != 0):
                pos = index
                num_let = num_let - 1
            if (num_let == 0):
                longest_seq = word
                break

    