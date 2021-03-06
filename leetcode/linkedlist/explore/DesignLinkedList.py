class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = list()
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= len(self.list):
            return -1
        else:
            return self.list[index]

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.list.insert(0,val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.list.append(val)
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list,
        the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if 0 <= index < len(self.list) and self.list != []:
            self.list.insert(index, val)
        elif index >= len(self.list) and self.list != []:
            self.list.append(val)
        elif index < 0:
            self.list.insert(0, val)
        elif self.list == [] and index != 0:
            self.list = []
        else:
            self.list.append(val)

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index>=len(self.list):
            return
        else:
            del self.list[index]

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)