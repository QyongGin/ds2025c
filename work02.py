import random

random_number = random.randint(1, 100)

while True:
    try:
        user_input = int(input("숫자를 맞춰보세요 : "))

        if random_number == user_input:
            print(f"맞추셨습니다! 숫자는 {user_input}입니다!")
            break
        elif random_number > user_input:
            print("랜덤숫자가 더 큽니다!")
        else:
            print("랜덤숫자가 더 작습니다!")
    except ValueError:
        print("숫자를 입력해 주세요.")