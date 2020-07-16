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
    l_index = 0
    r_index = len(nums) - 1
    if len(nums) == 2:
        return nums[0] == nums[1]
    while True:
        if l_sum <= r_sum and l_index != r_index:
            l_sum += nums[l_index]
            l_index += 1
        if r_sum < l_sum and l_index != r_index:
            r_sum += nums[r_index]
            r_index -= 1
        # means they are almost balanced or no balance can be found
        if l_index == r_index:
            if l_sum < r_sum or nums[l_index] == 0:
                l_sum += nums[l_index]
                l_index += 1
                break
            if r_sum < l_sum:
                r_sum += nums[r_index]
                r_index -= 1
                break
            if r_sum == l_sum:
                return False
        
    return l_sum == r_sum      
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