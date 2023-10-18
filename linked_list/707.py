class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1
        cur = self.head.next
        while index:
            index -= 1
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.next = self.head.next
        self.head.next = node
        self.size += 1


    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < 0:
            self.addAtHead(val)
            return
        elif index == self.size:
            self.addAtTail(val)
            return
        elif index > self.size:
            return
        node = Node(val)
        pre = self.head
        while index:
            index -= 1
            pre = pre.next
        node.next = pre.next
        pre.next = node
        self.size += 1


    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        pre = self.head
        while index:
            pre = pre.next
            index -= 1
        pre.next = pre.next.next
        self.size -= 1


list = MyLinkedList()
list.addAtHead(1)
# list.addAtTail(2)
list.addAtTail(3)
list.addAtIndex(1, 2)
print("get", list.get(0))
print("get", list.get(1))
print("get", list.get(2))
print("get", list.get(3))
print("del", list.deleteAtIndex(1))
print("get", list.get(1))
