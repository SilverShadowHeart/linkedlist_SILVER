class SLLNode:
    """Node for a singly linked list."""
    __slots__ = ['data', 'next']

    def __init__(self, data):
        self.data = data
        self.next = None

class DLLNode:
    """Node for a doubly linked list."""
    __slots__ = ['prev', 'data', 'next']

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None