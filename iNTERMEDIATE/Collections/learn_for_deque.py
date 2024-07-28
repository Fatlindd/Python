"""
    deque (deck) is a double-ended queue provided by the 'collections' module in Python. It is designed for
    efficient insertion and removal of elements from both ends. While Python lists are optimized for fast
    fixed-length operations, 'deque' is optimized for fast appends and pops from both ends.

    When to Use deque
        1. Efficient Appends and Pops: When you need to efficiently append or pop elements from both the front and
        the back of the queue.
        2. Queue Implementation: When implementing FIFO (First In, First Out) queues.
        3. Stack Implementation: When implementing LIFO (Last In, First Out) stacks.
        4. Sliding Window: When processing data in a sliding window manner.
"""

# ------------------------------------------------------------------------------------------------------------

from collections import deque

# Basic Example
# Create a deque
dq = deque()

dq.append('a')
dq.append('b')
dq.append('c')

# print(dq.pop())  # Output: 'c'
# print(dq.pop())  # Output: 'b'
# print(dq.pop())  # Output: 'a'

# ------------------------------------------------------------------------------------------------------------

# Example 1: Implementing a Queue
queue = deque()

# Enqueue elements
queue.append('first')
queue.append('second')
queue.append('third')

# Dequeue elements
# print(queue.popleft())  # Output: 'first'
# print(queue.popleft())  # Output: 'second'
# print(queue.popleft())  # Output: 'third'

# ------------------------------------------------------------------------------------------------------------

# Example 2: Implementing a Stack
stack = deque()

stack.append('first')
stack.append('second')
stack.append('third')

# Pop elements from the stack
# print(stack.pop())  # Output: 'third'
# print(stack.pop())  # Output: 'second'
# print(stack.pop())  # Output: 'first'

# ------------------------------------------------------------------------------------------------------------

# Example 3: Rotating a Deque
dq_ = deque([1, 2, 3, 4, 5])

# Rotate right by 2
dq_.rotate(2)
print(dq_)  # Output: deque([4, 5, 1, 2, 3])

# Rotate left by 3 (equivalent to rotating right by -3)
dq_.rotate(-3)
print(dq_)  # Output: deque([2, 3, 4, 5, 1])

# ------------------------------------------------------------------------------------------------------------
