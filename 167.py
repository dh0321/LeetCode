class Solution(object):
    # two pointers
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            sum = numbers[left] + numbers[right]
            
            if sum == target:
                return [left + 1, right + 1]
            elif sum < target:
                left += 1
            else:
                right -= 1

'''
Solution 1.
# binary search
def twoSum(self, numbers, target):
    for i in range(len(numbers)):
        complement = target - numbers[i]
        left, right = i + 1, len(numbers) - 1

        # Standard binary search
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]  # 1-based indexing
            elif numbers[mid] < complement:
                left = mid + 1
            else:
                right = mid - 1

'''
