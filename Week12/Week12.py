# 2025-05-26

# deque : 양방향 큐
# append, popleft

from collections import deque

d = deque([17, 55, 123])
d.append(7)
d.appendleft(100)
for _ in range(len(d)):
    print(d.popleft())