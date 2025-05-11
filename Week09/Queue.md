# 큐란?
선입선출(First in First out), 먼저 들어간 요소가 먼저 나오는 구조.

## 큐의 개념
큐(Queue) 자료구조는 스택과 다르게 입구와 출구가 따로 있는 형태. 

## 구조와 용어
- enQueue(인큐) : 큐에 데이터를 삽입하는 작동
- deQueue(데큐) : 데이터를 추출하는 작동
- front(머리) : 저장된 데이터 중 첫 번째 데이터
- rear(꼬리) : 저장된 데이터 중 마지막 데이터

## 큐 생성
배열 크기를 지정한 후 해당 크기의 빈 큐 생성
```python
queue = [None, None, None, None, None]
front = rear = -1
```

## 데이터 삽입 : enQueue

```python
queue = [None, None, None, None, None]
front = rear = -1

rear += 1 # index[0]부터 차례대로 데이터 삽입 
queue[rear] = "일번"
rear += 1
queue[rear] = "이번"
rear += 1
queue[rear] = "삼번"

print("---Queue State---")
print('[Exit] <--', end = ' ')
for i in range(0, len(queue), 1): # 0(start)부터 4(stop)까지 1(step)씩 증가
  print(queue[i],end = ' ')
print('<-- [Entrance]')
# [Exit] <-- 일번 이번 삼번 None None <-- [Entrance]
```

## 데이터 추출 : deQueue

```python
queue = ["일번", "이번", "삼번", None, None]
front = -1
rear = 2

print("---Queue State---")
print('[Exit] <--', end = ' ')
for i in range(0, len(queue), 1): # 0(start)부터 4(stop)까지 1(step)씩 증가
  print(queue[i],end = ' ')
print('<-- [Entrance]')

front += 1
data = queue[front]
queue[front] = None
print('deQueue -->', data)
# [Exit] <-- None 이번 삼번 None None <-- [Entrance]
```
