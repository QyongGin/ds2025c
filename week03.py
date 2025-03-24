import array # 배열 비슷한 성능을 내고 싶다면 array

def move_zeros(arr):
    zero_index = 0
    for index, n in enumerate(arr):
        if n != 0:
            arr[zero_index] = n
            if zero_index != index:
                arr[index] = 0
            zero_index += 1
    return(arr)

arr = array.array('f',[99, 0, -7, 0, 16]) # 배열이 아니라 리스트.
move_zeros(arr)
print(arr)
# 메모리 아끼기위해 일정 범위 안 동일숫자를 베껴서 주소가 같다..















for i in range (len(arr)):
    print(f"{arr[i]:5} {id(arr[i])}") # l의 i번째 칸. l이라는 리스트의 i 주소 #0은 같은 주소 사용
    # 리스트를 배열처럼 쓸 뿐. 배열 제공 없음.

