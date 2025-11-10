class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)

        return not stack

# Time: O(n)
# Space: O(n) in worst case

'''
Solution 1.
def isValid(self, s):
    parentheses_pair = {"(": ")", "[": "]", "{": "}"}
    stack = []

    for ch in s:
        if ch in parentheses_pair:
            stack.append(ch)
        elif ch in parentheses_pair.values():
            if not stack or parentheses_pair[stack[-1]] != ch:
                return False
            stack.pop()
        else:
            return False

    return not stack


Solution 2.

def isValid(self, s):

    stack = []
    pair = {'(': ')', '{': '}', '[': ']'}

    for char in s:
        if char in pair:
            stack.append(pair[char])
        else:
            if not stack or stack.pop() != char:
                return False

    return not stack



'''
