#Return an array that contains
#the sorted values from the input 
#array with duplicates removed.

#sort([]) → []
#sort([1]) → [1]
#sort([1, 1]) → [1]
#sort([1, 1, 4, 10, 4]) → [1, 4, 10]

a = [1, 1, 4, 10, 4]
def sort(nums):
    s = set(nums)
    s = list(s)
    s.sort()
    print(s)

sort(a)