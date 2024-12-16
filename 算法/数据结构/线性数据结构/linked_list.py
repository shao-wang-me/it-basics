class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def validIndex(self, index: int):
        return 0 <= index < self.length

    def getNode(self, index: int):
        if not self.validIndex(index): return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if self.validIndex(index):
            return self.getNode(index).val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.head = Node(val, self.head)
        elif index == self.length:
            tail = self.getNode(self.length - 1)
            tail.next = Node(val, None)
        elif self.validIndex(index):
            lastNode = self.getNode(index - 1)
            if lastNode:
                node = lastNode.next
                lastNode.next = Node(val, node)
        else:
            return
        self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if self.validIndex(index):
            if index == 0:
                self.head = self.head.next
            else:
                lastNode = self.getNode(index - 1)
                lastNode.next = lastNode.next.next
            self.length -= 1


class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(1)  # 1
    obj.addAtTail(3)  # 1 3
    obj.addAtIndex(1, 2)  # 1 2 3
    print(obj.head.val, obj.head.next.val, obj.head.next.next.val)
    print(obj.get(1))  # 2
    obj.deleteAtIndex(1)  # 1 3
    print(obj.head.val, obj.head.next.val)
    print(obj.get(1))  # 3

    print('---------')

    obj = MyLinkedList()
    obj.addAtIndex(0, 1)  # 1
    obj.addAtIndex(1, 3)  # 1 3
    obj.addAtIndex(1, 2)  # 1 2 3
    obj.addAtIndex(0, 4)  # 4 1 2 3
    print(obj.head.val, obj.head.next.val, obj.head.next.next.val, obj.head.next.next.next.val)
    print(obj.get(1))  # 1
    obj.deleteAtIndex(1)  # 4 2 3
    print(obj.head.val, obj.head.next.val, obj.head.next.next.val)
    print(obj.validIndex(0))
    obj.deleteAtIndex(0)  # 2 3
    print(obj.head.val, obj.head.next.val)
    print(obj.get(1))  # 3
