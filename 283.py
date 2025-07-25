def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero] = nums[i]
            non_zero += 1

    for i in range(non_zero, len(nums)):
        nums[i] = 0

    return nums

'''
Solution 1.
def moveZeroes(self, nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    non_zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero], nums[i] = nums[i], nums[non_zero]
            non_zero += 1
    
    print(nums)
    return nums

'''

        
