def singleNumber(self, nums):
    # using XOR, bit manipulation
    result = 0
    for num in nums:
        result ^= num
    return result


'''
Solution 1.
# using set()

def singleNumber(self, nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            num_set.remove(num)
        else:
            num_set.add(num)
    return num_set.pop()

'''
