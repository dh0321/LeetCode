from collections import deque

class MyStack(object):

    def __init__(self):
        self.que = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que.append(x)
        for _ in range(len(self.que) - 1):
            self.que.append(self.que.popleft())

    def pop(self):
        """
        :rtype: int
        """
        return self.que.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.que[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.que

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

'''
Solution 1.
from collections import deque

class MyStack(object):

    def __init__(self):
        self.que1 = deque()
        self.que2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        while len(self.que1) > 1:
            self.que2.append(self.que1.popleft())
        res = self.que1.popleft()
        self.que2, self.que1 = self.que1, self.que2

        return res

    def top(self):
        """
        :rtype: int
        """
        while len(self.que1) > 1:
            self.que2.append(self.que1.popleft())
        res = self.que1.popleft()
        self.que2.append(res)
        self.que2, self.que1 = self.que1, self.que2

        return res

    def empty(self):
        """
        :rtype: bool
        """
        return not self.que1
        

'''


