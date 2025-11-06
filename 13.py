class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        sum = 0
        pre_value = 0

        for char in reversed(s):
            curr = roman[char]
            if curr < pre_value:
                sum -= curr
            else:
                sum += curr
            pre_value = curr

        return sum


'''
Solution 1.

def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    roman = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    sum = 0
    for i in range(len(s)-1):
        curr = s[i]
        next = s[i+1]

        if roman[curr] < roman[next]:
            sum -= roman[curr]
        else:
            sum += roman[curr]

    sum += roman[s[-1]]
    return sum


Solution 2.

roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

sum = 0
s = s.replace("IV", "IIII").replace("IX", "VIIII")
s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

for char in s:
    sum += roman[char]

return sum


'''
