# week2 0.2.0

# n = int(input("정수 입력 : ")) # 정수형으로 입력받는다.
# result = 0
# for i in range(1, n+1): # 1부터 입력한 수까지 반복한다.
#     result = result + i # 0부터 입력한 수까지의 합.
#     print(result)
#     result = n * (n + 1) // 2  # O(1)
#     print(result)

# week2 0.3.0
import random # random 모듈 불러오기

answer = random.randint(1, 100) # 1부터 100까지의 난수 생성
win = False

for guesses in range(7):
    print(f"{7-guesses}번의 기회가 남았습니다. 숫자 입력 : ", end='')
    # {7-(0~6)} 7부터 1까지 기회 출력.
    # end=''는 출력후 줄바꿈하지 않도록 마지막에 '' 삽입.
    # '7번의 기회가 남았습니다. 숫자 입력 : 2' 라는 출력을 얻기 위한 end=''
    guess = int(input()) # 사용자가 입력한 문자열 숫자형으로 변환해서 저장.

    if answer == guess: # 난수와 입력한 수가 맞다면 정답.
        print("정답입니다!")
        win = True
        break # 반복문 탈출.
    elif answer > guess:
        print("입력하신 수는 정답보다 작은 수 입니다. LOW")
    else:
        print("입력하신 수는 정답보다 큰 수 입니다. HIGH")

if win: # for 문이 끝나면 맞췄다면
    print("You win!")
else:
    print(f"You lose. The answer is {answer}.")