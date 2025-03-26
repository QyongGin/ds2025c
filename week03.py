# Chapter8 배열, chapter1 공간 복잡도

# groups = ['HOT', 'Seventeen', 'Black Pink', 'NJZ']
# ratings = [1, 2, 4, 3]
#
# group_rating = list(zip(groups, ratings)) # zip 두 리스트 결합. 내부 반복문 돌아감. 작은 수 기준으로
# print(group_rating)
#
# groups = ['HOT', 'Seventeen', 'Black Pink', 'NJZ']
# ratings = [1, 2]
#
# group_rating = list(zip(groups, ratings)) # 두 리스트 길이 확인해야 함.
# print(group_rating)
#
# # set
# # 중복이 없어진다. 딕셔너리 키만 잇는 버전.
#
# def duplicate_city(cities):
#     result_city = list()
#     s = set()
#
#     for city in cities:
#         l1 = len(s)
#         s.add(city)
#         l2 = len(s)
#         if l1 == l2:
#             result_city.append(city)
#     return result_city
#
# cities = ['Suwon', 'Hwasung', 'Incheon', 'Incheon', 'Bucheon', 'Incheon', 'Seoul']
# cities.append('Seoul')
# cities.append('Antang')
# print(cities)
# print(set(duplicate_city(cities)))

# def inters(l1,l2):
#     s1 = set(l1)
#     s2 = set(l2)
#     # return list(s1.intersection(s1 & s2))
#     return list(s1.union(s2)) # 교집합
#
# l1 = [45, 5, 22, 31, 7, 19]
# l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
# print(inters(l1,l2))

# ------------------------------------------------------------------------------------

# 2025-03-26 revise
""" v0.4 array
l = [99, 0, -7, 0, 16] # 리스트 생성
for i in range(len(l)): # l 리스트의 요소 개수만큼 반복한다. i에 0~4 대입
    print(f"{l[i]:2} {id(l[i])}")
"""
    # 파이썬의 변수는 데이터가 메모리상에서 위치하는 주솟값이 저장되는 공간이다. 실제 데이터 저장 X
    # 리스트는 '이질 가변 길이 배열'이다.
    # '가변 길이 배열' -> 생성한 뒤에도 크기를 바꿀 수 있다.'이질 배열' -> 여러 타입의 데이터를 담을 수 있다.
    # l의 i요소:2 -> 숫자를 두칸으로 표현
    # id(l[i]) -> l의 i번째 요소 고유 주소 값 출력
    # 고유 주소 : 객체가 메모리 안에 위치한 주소. 객체의 수명 동안 유일하고 바뀌지 않음.
    # id() -> 객체의 고유 값을 리턴

# v0.5 array
"""
import array # array 모듈 불러오기

arr = array.array('f',[99, 0, -7, 0, 16])
    # 배열array는 '동질적 자료구조'로서 한 가지의 데이터 타입만 담는다.
    # '정적 자료구조'의 특징을 가져 크기를 바꾸지 못한다.
    # array.array 생성, 두 개의 매개변수 'f'(데이터타입 실수) 99~16(리스트)
for i in range(len(arr)): # 배열의 길이만큼 5번(0~4) 반복, 대입.
    print(f"{arr[i]:5} {id(arr[i])}")
    # 5개의 칸을 가지고 요소를 출력. 요소의 주소 출력.
"""

# v0.6 array
"""
# def move_zeros(l): # enumerater()를 사용하지 않은 방법
#     zero_idx = 0
#     for i in range(len(l)):
#         n = l[i] # n은 l의 i번째 요소
#         if n != 0:
#             l[zero_idx] = n
#             if zero_idx != i:
#                 l[i] = 0
#             zero_idx = zero_idx + 1
#     return l

def move_zeros(l):
    zero_index = 0 # 0의 위치
    for index, n in enumerate(l): # enumerate() 함수는 인덱스와 원소로 이루어진 튜플을 만듦. 즉 인덱스와 원소를 동시에 반환.
        if n != 0: # 만약 원소의 값이 0이 아니라면. 원소의 값이 0이면 다음 반복 실행
            l[zero_index] = n # 리스트의 0의 위치 칸에 0이 아닌 현재 값을 대입.
            # 즉 l[zero_index]는 0이 아닌 값의 주소 
            if zero_index != index: # 0의 주소와 현 주소가 다르다면
                l[index] = 0 # 현 주소에 0 대입.
            zero_index += 1 # 0의 위치 +1
    return(l)

    # zero_index(0) index(0) n(99) -> 99 != 0 True -> l[0] = 99
    # 0 != 0 False zero_index += 1
    # zero_index(1) index(1) n(0) -> 0 != 0 False -> 다음 반복
    # zero_index(1) index(2) n(-7) -> -7 != 0 true -> l[1] = -7
    # 1 != 2 True -> l[2] = 0 zero_index += 1
    # zero_index(2) -> 현재 0의 위치.

l = [99, 0, -7, 0, 16] # 리스트 생성
move_zeros(l) # 함수 move_zeros에 리스트 l 대입
print(l)
"""

# v0.7 array
"""
groups = ['HOT', 'Seventeen', 'Black Pink', 'NJZ']
# ratings = [1, 2, 4, 3, 100]
ratings = [1, 2, 4, 3]

group_rating = list(zip(groups, ratings))
# 이터러블 데이터 -> 반복문에서 사용가능한 데이터로 for i in groups 같은 리스트를 가리킴.
# zip 함수는 하나 이상의 이터러블 데이터를 받아 요소를 순서대로 묶은 zip 객체를 반환하고 리스트로 변환한다.
# 아이돌 그룹과 순위가 묶인 튜플 리스트 생성
print(group_rating)
# >>> [('HOT', 1), ('Seventeen', 2), ('Black Pink', 4), ('NJZ', 3)]
"""

# v0.8 set
"""
cities = ['Suwon', 'Hwasung', 'Incheon', 'Incheon', 'Bucheon', 'Incheon', 'Seoul']
cities = set(cities)
# 세트(set)는 중복 요소를 포함하지 못하는 자료구조다.
# 즉, cities 리스트에서 중복된 요소를 제거한다.
print(cities)
# >>> {'Bucheon', 'Seoul', 'Hwasung', 'Suwon', 'Incheon'}
"""

# v0.9 set
"""
def duplicate_city(cities):
    result_city = list()
    s = set() # 빈 리스트와 세트 생성.

    for city in cities:
        l1 = len(s)
        s.add(city) # 세트에 cities의 요소 추가. set()는 중복된 요소는 포함시키지 않는다.
        l2 = len(s) # 중복된 요소가 변수에 대입되었을 때 길이는 변하지 않는다.
        if l1 == l2: # Incheon이 중복된 요소 타이밍에 l1과 l2의 길이는 동일하다.
            result_city.append(city) # city 변수는 중복된 요소. 그 요소를 result에 추가.
    return result_city


cities = ['Suwon', 'Hwasung', 'Incheon', 'Incheon', 'Bucheon', 'Incheon', 'Seoul']
cities.append('Seoul') # 리스트에 추가
cities.append('Anyang')
print(cities) # 중복된 값 포함된 리스트 그대로 출력.
print(set(duplicate_city(cities))) # 중복된 요소만 출력.
"""

# v1.0 교집합 찾기
"""
def inters(l1, l2): # 중복된 요소를 찾는 함수. 교집합 찾기
    l3 = list()
    for v in l1: # l1의 첫 요소부터 비교.
        if v in l2: # 만약 l2 리스트에 l1에 대입된 요소가 들어있다면
            l3.append(v) # l3에 추가한다.
    return l3 # 동일한 요소를 모두 찾았다면 반환.

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
print(inters(l1, l2))
"""

# v1.1 intersection()
"""
def inters(l1, l2): # 두 개의 리스트를 매개변수로 받는 함수
    s1 = set(l1)
    s2 = set(l2)
    return list(s1 & s2) # & -> 두 집합의 교집합을 구하는 연산.
    # return list(s1.intersection(s2))
    # intersection() 함수는 두개 이상의 세트에 모두 존재하는 요소를 반환하는 교집합 함수
    # (s1.intersection(s2,s3,s4)) 같은 여러 세트에서 찾기 가능.

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
print(inters(l1, l2))
"""




