import collections



#Consider the leftmost and righmost appearances of some value in an array. 
# We'll say that the "span" is the number of elements between the two inclusive. 
# A single value has a span of 1. Returns the largest span found in the given array. 
# (Efficiency is not a priority.)


#maxSpan([1, 2, 1, 1, 3]) → 4
#maxSpan([1, 4, 2, 1, 4, 1, 4]) → 6
#maxSpan([1, 4, 2, 1, 4, 4, 4]) → 6


# testing data
#nums = [1, 4, 2, 1, 4, 1, 4]
nums = [1, 4, 2, 1, 4, 1, 4]
#nums = []
#nums = [1]
#nums = [1,2,3,1]
#nums = [3, 9, 9]

def max_span(nums):
    num_positions = collections.defaultdict(list)
    if (len(nums) == 0):
        return 0
    if (len(nums) == 1):
        return 1
    #preprocess nums into a hashmap with lists of indexes
    for i in range(len(nums)):
        num_positions[nums[i]].append(i)

    # O(n log n) time complexity worst, O(n) best case all ready sorted list
    # O(N) space complexity, temp array of pointers :<
    largest_span = 0
    for index in sorted(num_positions.items(), key=lambda w: len(w), reverse=True):
        if(len(index[1]) == 1):
            continue
        else:
            span = (index[1][len(index[1])-1] - index[1][0]) + 1
            if largest_span < span:
                largest_span = span

    return largest_span

print(max_span(nums))