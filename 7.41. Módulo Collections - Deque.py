"""
Collections - Deque

List of high performance
"""
from collections import  deque

deq = deque('geek')
print(deq)  # deque(['g', 'e', 'e', 'k'])

# Add elements at deque
deq.append('y')
print(deq)  # deque(['g', 'e', 'e', 'k', 'y']) => add at end

deq.appendleft('k')
print(deq)  # deque(['k', 'g', 'e', 'e', 'k', 'y'])  => add at start

deq.pop()
print(deq)  # deque(['k', 'g', 'e', 'e', 'k']) => remove at end

deq.popleft()
print(deq)  # deque(['g', 'e', 'e', 'k']) => remove at start
