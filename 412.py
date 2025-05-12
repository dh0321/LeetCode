class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        fizzBuzzList = []
        element = ""

        for i in range(1, n+1):
            if i%3 == 0:
                element = "FizzBuzz" if i % 5 == 0 else "Fizz"
            elif i%5 ==0:
                element = "Buzz"
            else:
                element = str(i)
            fizzBuzzList.append(element)

        return fizzBuzzList

'''
Solution1.
class Solution(object):
    def fizzBuzz(self, n):
        result = []
        
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
                
        return result

'''
