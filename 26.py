def removeDuplicates(self, nums: List[int]) -> int:
    sortedNum = sorted(set(nums))
    for i in range(len(sortedNum)):
        nums[i] = sortedNum[i]

    return len(sortedNum)

# use extra memory for set() -> not good for interview

'''
Solution 1.
def removeDuplicates(self, nums: List[int]) -> int:
    write_index = 1

    for read_index in range(1, len(nums)):
        if nums[read_index] != nums[write_index - 1]:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index
'''



