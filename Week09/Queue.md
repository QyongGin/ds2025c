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
def isQueueFull(): # is로 시작하는 함수는 반환값이 bool 타입인 경우가 많다.
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

## 큐에 데이터를 삽입하는 함수

```python
def enQueue(data): # 함수 하나에 하나의 역할만 부여.
  global SIZE, queue, front, rear
  if (isQueueFull()):
    print("큐가 꽉 찼습니다.")
    return
  rear += 1
  queue[rear] = data

SIZE = 5
queue = ["일",None,None,None,None]
front = -1
rear = 0
enQueue("이") # ['일','이',None,None,None]
```

## 큐가 비었는지 확인하는 함수
front와 rear의 값이 같다면 큐가 빈 상태
입력하지 않았다면 '-1'로 같다.<br>
rear가 3이라 가정했을 때 front는 삭제하려고 +1씩 이동하므로 
rear가 머무는 요소까지 다 삭제했다면 rear = 3 front = 3으로 같다. 즉, 비었다.
```python
def isQueueEmpty():
  global SIZE, queue, front, rear
  if (front == rear):
    return True
  else:
    return False

SIZE = 5
queue = [None for _ in range(SIZE)] # None 값을 넣기 때문에 _ 사용
front = rear = -1 # 큐가 비었는지 여부 => True
```

## 큐에서 데이터를 추출하는 함수
```python
def deQueue():
  global SIZE,queue,front,rear
  if (isQueueEmpty()):
    print("큐가 비었습니다.")
    return None
  front += 1
  data = queue[front] # 추출할 값 저장
  queue[front] = None
  return data

SIZE = 5
queue = ['일','이',None,None,None]
front = -1
rear = 1

retData = deQueue()
print("추출한 데이터 -->", retData) # '일'
print(queue) # [None,'이',None,None,None]
```
## peek(픽) : 추출될 데이터를 큐에 그대로 두고 확인만 한다.
```python
def peek():
  global SIZE, queue, front, rear
  if (isQueueEmprty()):
    print("큐가 비었습니다.")
    return None
  return Queue[front+1]
# front를 저장하지 않아서 peek을 계속 사용해도 삭제될 값만 그대로 반환한다.

SIZE = 5
queue = [None,'이',None,None,None]
front = 0
rear = 1
print(peek()) # '이'
```


