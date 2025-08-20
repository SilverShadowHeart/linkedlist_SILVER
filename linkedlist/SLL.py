from .node import SLLNode

class SingleLinkedList:
    __slots__ = ['head', 'tail']

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_beginning(self, data):
        new_node = SLLNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = SLLNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_position(self, data, position):  # renamed from append
        new_node = SLLNode(data)
        if position <= 0 or not self.head:
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
            return

        cur = self.head
        idx = 1
        while cur.next and idx < position - 1:
            cur = cur.next
            idx += 1

        new_node.next = cur.next
        cur.next = new_node

        if new_node.next is None:  # update tail if inserted at end
            self.tail = new_node

    def delete(self, pos):  # delete at index (0-based)
        if not self.head:
            print("empty list")
            return
        if pos == 0:
            self.del_at_start()
            return

        cur = self.head
        prev = None
        idx = 0
        while cur and idx < pos:
            prev = cur
            cur = cur.next
            idx += 1

        if not cur:
            print("invalid position")
            return

        prev.next = cur.next
        if cur == self.tail:
            self.tail = prev

    def remove(self, data):
        if not self.head:
            print("empty list")
            return

        if self.head.data == data:
            self.del_at_start()
            return

        prev = self.head
        cur = self.head.next

        while cur:
            if cur.data == data:
                prev.next = cur.next
                if cur == self.tail:
                    self.tail = prev
                return
            prev = cur
            cur = cur.next

        print("value not found")

    def del_at_start(self):
        if not self.head:
            print("empty list")
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        self.head = self.head.next

    def del_at_end(self):
        if not self.head:
            print("empty list")
            return
        if self.head == self.tail:
            self.head = self.tail = None
            return
        cur = self.head
        while cur.next != self.tail:
            cur = cur.next
        cur.next = None
        self.tail = cur

    def update(self, position, data):
        cur = self.head
        idx = 0
        while cur and idx < position:
            cur = cur.next
            idx += 1
        if not cur:
            print("invalid position")
            return
        cur.data = data

    def reverse(self):
        prev = None
        cur = self.head
        self.tail = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next
