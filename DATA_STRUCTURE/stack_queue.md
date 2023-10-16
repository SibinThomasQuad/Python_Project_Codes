Certainly, I've added comments to explain each function and provided comments throughout the code to help you understand how the stack and queue implementations work:

**Stack:**

```python
class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.items = []

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Remove and return the top item from the stack
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Return None if the stack is empty

    def peek(self):
        # Return the top item without removing it
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Return None if the stack is empty

    def size(self):
        # Return the number of items in the stack
        return len(self.items)
```

**Queue:**

```python
class Queue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.items = []

    def is_empty(self):
        # Check if the queue is empty
        return len(self.items) == 0

    def enqueue(self, item):
        # Add an item to the back of the queue
        self.items.insert(0, item)  # Add to the front of the list

    def dequeue(self):
        # Remove and return the front item from the queue
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Return None if the queue is empty

    def size(self):
        # Return the number of items in the queue
        return len(self.items)
```

The comments in the code provide explanations for each function and what it does. These comments should help you understand how the stack and queue implementations work in Python.
