from .node import DLLNode

class DoubleLinkedList:
    """A doubly linked list with head and tail pointers."""
    __slots__ = ['head', 'tail', 'size']

    def __init__(self):
        """Initialize an empty doubly linked list."""
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        """Return True if the list is empty."""
        return self.head is None

    def insert_at_beginning(self, data):
        """Insert a node with the given data at the beginning.

        Args:
            data: The data to insert.
        """
        new_node = DLLNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        """Insert a node with the given data at the end.

        Args:
            data: The data to insert.
        """
        new_node = DLLNode(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert_at_position(self, data, position):
        """Insert a node with the given data at the specified 0-based position.

        Args:
            data: The data to insert.
            position: The 0-based index where the node should be inserted.

        Raises:
            ValueError: If position is negative or beyond list length.
        """
        if position < 0 or position > self.size:
            raise ValueError("Invalid position")
        if position == 0:
            self.insert_at_beginning(data)
            return
        if position == self.size:
            self.insert_at_end(data)
            return

        new_node = DLLNode(data)
        cur = self.head
        for _ in range(position):
            cur = cur.next
        new_node.prev = cur.prev
        new_node.next = cur
        cur.prev.next = new_node
        cur.prev = new_node
        if cur == self.head:
            self.head = new_node
        self.size += 1

    def delete(self, position):
        """Delete the node at the specified 0-based position.

        Args:
            position: The 0-based index of the node to delete.

        Raises:
            ValueError: If the list is empty or position is invalid.
        """
        if not self.head:
            raise ValueError("Empty list")
        if position < 0 or position >= self.size:
            raise ValueError("Invalid position")
        if position == 0:
            self.del_at_start()
            return
        if position == self.size - 1:
            self.del_at_end()
            return

        cur = self.head
        for _ in range(position):
            cur = cur.next
        cur.prev.next = cur.next
        if cur.next:
            cur.next.prev = cur.prev
        self.size -= 1

    def remove(self, data):
        """Remove the first node with the given data.

        Args:
            data: The data to remove.

        Raises:
            ValueError: If the list is empty or data is not found.
        """
        if not self.head:
            raise ValueError("Empty list")

        cur = self.head
        while cur:
            if cur.data == data:
                if cur == self.head:
                    self.del_at_start()
                elif cur == self.tail:
                    self.del_at_end()
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    self.size -= 1
                return
            cur = cur.next
        raise ValueError("Data not found")

    def del_at_start(self):
        """Delete the node at the beginning.

        Raises:
            ValueError: If the list is empty.
        """
        if not self.head:
            raise ValueError("Empty list")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1

    def del_at_end(self):
        """Delete the node at the end.

        Raises:
            ValueError: If the list is empty.
        """
        if not self.head:
            raise ValueError("Empty list")
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.size -= 1

    def update(self, position, data):
        """Update the data of the node at the specified 0-based position.

        Args:
            position: The 0-based index of the node to update.
            data: The new data value.

        Raises:
            ValueError: If the list is empty or position is invalid.
        """
        if not self.head:
            raise ValueError("Empty list")
        if position < 0 or position >= self.size:
            raise ValueError("Invalid position")

        cur = self.head
        for _ in range(position):
            cur = cur.next
        cur.data = data

    def reverse(self):
        """Reverse the linked list in place."""
        if not self.head or self.head == self.tail:
            return
        cur = self.head
        while cur:
            cur.next, cur.prev = cur.prev, cur.next
            cur = cur.prev
        self.head, self.tail = self.tail, self.head

    def show_val(self, position):
        """Return the data at the specified 0-based position.

        Args:
            position: The 0-based index of the node.

        Returns:
            The data at the specified position.

        Raises:
            ValueError: If the list is empty or position is invalid.
        """
        if not self.head:
            raise ValueError("Empty list")
        if position < 0 or position >= self.size:
            ValueError("Invalid position")

        cur = self.head
        for _ in range(position):
            cur = cur.next
        return cur.data

    def show_len(self):
        """Return the number of nodes in the list.

        Returns:
            The size of the list.
        """
        return self.size

    def find(self, data):
        """Return the 0-based position of the first node with the given data.

        Args:
            data: The data to find.

        Returns:
            The 0-based index of the data, or -1 if not found.

        Raises:
            ValueError: If the list is empty.
        """
        if not self.head:
            raise ValueError("Empty list")

        cur = self.head
        idx = 0
        while cur:
            if cur.data == data:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def generate(self, n):
        """Generate a list with values from 1 to n at positions 0 to n-1.

        Args:
            n: The number of nodes to generate.

        Raises:
            ValueError: If n is negative.
        """
        if n < 0:
            raise ValueError("Invalid size")
        for i in range(1, n + 1):
            self.insert_at_position(i, i)

    def display(self):
        """Return a string representation of the list.

        Returns:
            A string representing the list.
        """
        if not self.head:
            return "Empty list"
        result = []
        cur = self.head
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        return " <-> ".join(result) + " <-> None"

    def __iter__(self):
        """Yield the data of each node in the list."""
        cur = self.head
        while cur:
            yield cur.data
            cur = cur.next