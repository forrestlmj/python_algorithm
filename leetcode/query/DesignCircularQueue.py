class MyCircularQueue:

    def __init__(self, k: 'int'):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        环形列表实现的时候,最好维持一个size

        """
        self.queue = [None for i in range(k)]
        self.head = 0
        self.tail = 0
        self.max_size = k
        self.current_size = 0

    def enQueue(self, value: 'int') -> 'bool':
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if not self.isFull():
            self.tail += 1
            self.tail = self.tail % self.tail
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
            self.head += 1
            self.head = self.head & self.head
            self.queue[self.head] = None
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

    def Rear(self) -> 'int':
        """
        Get the last item from the queue.
        """
        if not self.isEmpty():
            return self.queue(self.tail)

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
param_1 = obj.enQueue(1)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()