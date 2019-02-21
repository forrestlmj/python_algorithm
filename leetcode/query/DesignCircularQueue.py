class MyCircularQueue:

    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        环形列表实现的时候,最好维持一个size

        """
        self.queue = [None for i in range(k)]
        self.head = -1
        self.tail = -1
        self.max_size = k
        self.current_size = 0

    def enQueue(self, value: 'int') -> 'bool':
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if not self.isFull():
            if self.tail == -1:
                self.tail = self.head = 0
            else:
                self.tail += 1
                self.tail = self.tail % self.max_size
            self.queue[self.tail] = value
            self.current_size += 1
            return True
        else:
            return False
    def deQueue(self) -> 'bool':
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if not self.isEmpty():
            if self.head == self.tail:
                self.head = self.tail = -1
            else:
                self.head += 1
                self.head = self.head % self.max_size
            # self.queue[self.head] = None
            self.current_size -= 1
            return True
        else:
            return False
    def Front(self) -> 'int':
        """
        Get the front item from the queue.
        """
        if not self.isEmpty():
            return self.queue[self.head]
        else:
            return -1
    def Rear(self) -> 'int':
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            return self.queue[self.tail]
        else:
            return -1
    def isEmpty(self) -> 'bool':
        """
        Checks whether the circular queue is empty or not.
        """
        return self.current_size == 0

    def isFull(self) -> 'bool':
        """
        Checks whether the circular queue is full or not.
        """
        return self.current_size == self.max_size

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
# param_1 = obj.enQueue(3)
# param_2 = obj.deQueue(1)
# param_3 = obj.Front(2)
# param_4 = obj.Rear(3)
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
def test_0():
    obj = MyCircularQueue(3)
    print(obj.enQueue(1))
    print(obj.enQueue(2))
    print(obj.enQueue(3))
    print(obj.enQueue(4))
    print(obj.Rear())
    print(obj.isFull())
    print(obj.deQueue())
    print(obj.enQueue(4))
    print(obj.Rear())
def test_1():
    obj=MyCircularQueue(6)
    assert obj.enQueue(6) == True
    assert obj.Rear() == 6
    assert obj.Rear() == 6
    assert obj.deQueue() == True
    assert obj.enQueue(5) == True
    assert obj.Rear() == 5
    assert obj.deQueue() == True
    assert obj.Front() == -1
    assert obj.deQueue() == False
    assert obj.deQueue() == False
    assert obj.deQueue() == False

if __name__ == "__main__":
    test_1()

    test_0()
