class MyCircularDeque:

    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.queue = [-1 for i in range(k)]
        self.max_size = k
        self.current_size = 0
        self.front = 0
        self.last = 0

    def insertFront(self, value: 'int') -> 'bool':
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            if self.isEmpty():
                pass
            else:
                self.front = (self.front - 1) % self.max_size
            self.queue[self.front] = value
            self.current_size += 1
            return True
        else:
            return False

    def insertLast(self, value: 'int') -> 'bool':
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if not self.isFull():
            if self.isEmpty():
                pass
            else:
                self.last += 1
                self.last = self.last % self.max_size
            self.queue[self.last] = value
            self.current_size += 1
            return True
        else:
            return False

    def deleteFront(self) -> 'bool':
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.queue[self.front] = -1
            self.front += 1
            self.front = self.front & self.max_size
            self.current_size -= 1
            if self.isEmpty():
                self.last = self.front
            return True
        else:
            return False

    def deleteLast(self) -> 'bool':
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.isEmpty():
            self.queue[self.last] = -1
            self.last = (self.last - 1)%self.max_size
            self.current_size -= 1
            if self.isEmpty():
                self.front = self.last
            return True
        else:
            return False

    def getFront(self) -> 'int':
        """
        Get the front item from the deque.
        """
        if not self.isEmpty():
            print(self.front)
            return self.queue[self.front]
        else:
            return -1

    def getRear(self) -> 'int':
        """
        Get the last item from the deque.
        """
        if not self.isEmpty():
            return self.queue[self.last]
        else:
            return -1

    def isEmpty(self) -> 'bool':
        """
        Checks whether the circular deque is empty or not.
        """
        if self.current_size == 0:
            return True
        else:
            return False

    def isFull(self) -> 'bool':
        """
        Checks whether the circular deque is full or not.
        """
        if self.current_size == self.max_size:
            return True
        else:
            return False

# Your MyCircularDeque object will be instantiated and called as such:
def test_0():
    obj = MyCircularDeque(3)
    obj.insertLast(1)
    obj.insertLast(2)
    obj.insertFront(3)
    obj.insertFront(4)
    obj.getRear()
    obj.isFull()
    obj.deleteLast()
    obj.insertFront(4)
    obj.getFront()

if __name__ == "__main__":
    # https://leetcode.com/submissions/detail/210235009/
    test_0()
