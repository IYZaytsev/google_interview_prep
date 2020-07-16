import time
#Given a non-empty array, 
#return true if there is a place 
#to split the array so that the sum of the 
#numbers on one side is equal to the sum 
#of the numbers on the other side.


#canBalance([1, 1, 1, 2, 1]) → true
#canBalance([2, 1, 1, 2, 1]) → false
#canBalance([10, 10]) → true
a = [1, 1, 1, 2, 1]
b = [2, 1, 1, 2, 1]
c = [10, 10]
d = [20, 40]
e = [10, 5, 5]
f = [10,10,10,10]
g = [30,20,1,1]
def canBalance(nums):
    l_sum = 0
    r_sum = 0
    # We don't want an unused point in the middle, so we start out of bounds and move in.
    l_index = -1
    r_index = len(nums)
    
    while True:
        if l_sum <= r_sum:
            l_index += 1
            l_sum += nums[l_index]
        elif r_sum < l_sum:
            r_index -= 1
            r_sum += nums[r_index]
        # The two halves have met in the middle, time to adjust until we find the middle.
        if l_index == r_index - 1:
            # From now on, l_index is the real index, but store previous ones in r_index and prev_index.
            prev_prev_index = -1
            while True:
                if l_sum == r_sum:
                    return True
                
                if l_index == prev_prev_index:
                    # We've been here before, so we must have moved back, so we can't split.
                    return False
                
                if l_sum < r_sum:
                    l_sum += nums[l_index]
                    r_sum -= nums[l_index]
                    prev_prev_index = r_index
                    r_index = l_index
                    l_index += 1
                else: # r_sum < l_sum
                    l_sum -= nums[l_index]
                    r_sum += nums[l_index]
                    prev_prev_index = r_index
                    r_index = l_index
                    l_index -= 1
start_time = time.perf_counter()
print(canBalance(a))
print(canBalance(b))
print(canBalance(c))
print(canBalance(d))
print(canBalance(e))
print(canBalance(f))
print(canBalance(g))
print(canBalance([1, 0, 1]))
end_time = time.perf_counter()
total_runtime = end_time - start_time
print(total_runtime * 100)
