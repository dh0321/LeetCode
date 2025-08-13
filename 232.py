class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        temp = []
        while len(self.stack) > 1:
            temp.append(self.stack.pop())
        res = self.stack.pop()
        while temp:
            self.stack.append(temp.pop())

        return res

    def peek(self):
        """
        :rtype: int
        """
        temp = []
        while len(self.stack) > 1:
            temp.append(self.stack.pop())
        res = self.stack[-1]
        print(self.stack)
        while temp:
            self.stack.append(temp.pop())
        print(self.stack)
        return res


    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

'''
Solution 1.
class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.in_stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        self.move()
        return self.out_stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.out_stack[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return not self.in_stack and not self.out_stack

    def move(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


'''

