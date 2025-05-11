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
삽입은 rear(꼬리)가 1씩 이동하며 각 index에 차례대로 데이터를 삽입한다.
```python
queue = [None, None, None, None, None]
front = rear = -1

rear += 1 # index[0]부터 차례대로 데이터 삽입 
queue[rear] = "one"
rear += 1
queue[rear] = "two"
rear += 1
queue[rear] = "three"

print("---Queue State---")
print('[Exit] <--', end = ' ')
for i in range(0, len(queue), 1): # 0(start)부터 4(stop)까지 1(step)씩 증가
  print(queue[i],end = ' ')
print('<-- [Entrance]')
# [Exit] <-- one two three None None <-- [Entrance]
```

## 데이터 추출 : deQueue
추출은 front(머리)가 1씩 이동하며 각 index의 데이터를 출력 후 삭제한다.
```python
queue = ["one", "two", "three", None, None]
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
# [Exit] <-- one two three None None <-- [Entrance]
# deQueue --> one
# [Exit] <-- None two three None None <-- [Entrance]
```

## 큐 초기화

SIZE값만 변경하면 원하는 크기의 빈 큐 생성(초기화)
```python
SIZE = 5 # 큐 크기
queue = [None for _ in range(SIZE)] # [None, None, None, None, None]
front = rear = -1
```

## 큐가 꽉 찼는지 확인하는 함수
rear 값이 'queue SIZE-1'과 같다면 큐가 꽉 찬 상태
```python
def isQueueFull():
  global SIZE, queue, front, rear # 전역변수
  if (rear == SIZE-1):
    return True
  else:
    return False

SIZE = 5
queue = ["one", "two", "three", "four", "five"]
front = -1
rear = 4

print("큐가 꽉 찼는지 여부 ==>", isQueueFull())
# 큐가 꽉 찼는지 여부 ==> True
```
