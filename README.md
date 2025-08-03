# linkedlistlib

A Python package that provides implementations of four types of linked lists:

- ✅ Singly Linked List (SLL)
- ✅ Doubly Linked List (DLL)
- ✅ Circular Singly Linked List (CLL)
- ✅ Circular Doubly Linked List (DCLL)

This package is ideal for learning, prototyping, or using linked list data structures in projects where dynamic memory manipulation is required.

---

## 📦 Installation

Coming soon on PyPI. Once released:

```bash
pip install linkedlistlib
```

Or for development:

```bash
git clone https://github.com/Aswath220/linkedlistlib
cd linkedlistlib
pip install .
```

---

## 🧠 Features

- Insert at beginning/end
- Append at custom position
- Delete by index or value
- Reverse the list
- Find elements by value
- Generate sequential nodes
- Show list length or a value at a position
- Fully circular and doubly-linked behavior supported

---

## 📂 Package Structure

```
linkedlistlib/
├── linkedlist/
│   ├── SLL.py       # Single Linked List
│   ├── DLL.py       # Doubly Linked List
│   ├── CLL.py       # Circular Single Linked List
│   ├── DCLL.py      # Circular Doubly Linked List
│   ├── node.py      # Node classes (SLLNode, DLLNode)
│   └── __init__.py  # Package entry point
└── tests/           # Unit tests (pytest)
```

---

## 🚀 Usage Examples

### 🔹 Singly Linked List

```python
from linkedlistlib import SingleLinkedList

sll = SingleLinkedList()
sll.insert_at_beginning(10)
sll.insert_at_end(20)
sll.display()
```

### 🔹 Doubly Linked List

```python
from linkedlistlib import DoubleLinkedList

dll = DoubleLinkedList()
dll.generate(5)
dll.reverse()
dll.display()
```

### 🔹 Circular Linked List

```python
from linkedlistlib import CircularLinkedList

cll = CircularLinkedList()
cll.insert_at_end(1)
cll.insert_at_end(2)
cll.display()
cll.reverse()
cll.display()
```

### 🔹 Circular Doubly Linked List

```python
from linkedlistlib import CircularDoubleLinkedList

dcll = CircularDoubleLinkedList()
dcll.insert_at_beginning(5)
dcll.insert_at_end(15)
dcll.display()
```

---

## ✅ License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 👤 Author

Developed by **Aswath**🫡🫡

Check out my GitHub: [https://github.com/Aswath220](https://github.com/Aswath220)
