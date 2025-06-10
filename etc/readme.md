# 리스트
- 리스트는 대괄호 ``[]`` 또는 ``list()``
```python
students = ["연우","호연","민수","진수"]
print(students[0]) # 연우
print(students[-1]) # 진수

for student in students:
  print(student)
# 연우
# 호연
# 민수
# 진수

for i in range(4): # 0부터3까지
  print(students[i]
# 위 항목과 동일

print(len(students)) # students의 길이는 4

house = ["인천","서울","대구","부산"]

name = input("이름은?") # input 문자열 반환

for i in ragne(len(students)):
  if studens[i] == name:
    print(f"집 : {house[i]}") # -연우 집 : 인천
    break
```

# 딕셔너리 Dictionary
- 키(key)와 값(value)을 쌍으로 연결한 데이터 구조.
- var = {키:값, 키:값}

```python
students = {"연우" : "인천",
            "호연" : "서울",
            "민수" : "대구"}

print(students["연우"]) # index 사용하지 않는다. 키값을 사용한다.
# "인천"

print(studnets)
# {"연우" : "인천", "호연" : "서울", "민수" : "대구"}

for st in students:
  print(st)
# 연우, 호연, 민수

for st in students:
  print(student[st])
# 인천, 서울, 대구

for st in students:
  print(st, students[st], sep=", ")
# 연우, 인천 호연, 서울 민수, 대구

studnets = [ {"name" : "용진", "집" : "인천", "나이" : "23"},
             {"name" : "민수", "집" : "북한", "나이" : "23"} ]

for st in studnets:
  print(st["name"], st["집"], st["나이"], sep = ", ")

# 용진, 인천, 23
# 민수, 북한, 23
```
# 라이브러리
- 공통적으로 필요한 기능(함수)을 구현해 모아 놓은 것
- 모듈(Modules)이라는 파이썬 파일(.py) 단위로 배포
- random, math, sys 등.

```python
import random
coin = random.choice( ["손바닥", "손등"] )
print(coin) # 손바닥 or 손등

from random import choice # random 모듈 속 choice 함수만 사용
coin = choice( ["손바닥", "손등"] )

# 1부터 10까지 랜덤 정수 randint()
number = random.randint(1,10)
print(number)

# 데이터 섞기 shuffle()

cards = ["잭", "퀸", "킹"]
random.shuffle(cards) # cards 원본 자체를 섞는다.
print(cards) # 섞여서 출력 

# statistics 통계 모듈

# 평균값 mean()
import statistics
num = statistics.mean( [80, 100, 90] ) # 수의 평균
print(num) = 90 

# median 중앙값
num = statistics.mean( [80, 100, 90] ) # 가장 중간 수 
print(num) = 90

# math 수학 모듈

# sqrt() 제곱근

# calendar, time 모듈
import calendar, time
print(calendar.calendar(2024)) # 달력 생성
```


