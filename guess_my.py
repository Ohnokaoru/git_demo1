import random

ans = random.randint(1, 100)

while True:
    guess = int(input("請輸入猜的數字:"))
    if guess > ans:
        print("猜小一點")
    elif guess < ans:
        print("猜大一點")
    else:
        print(f"答對了答案是{ans}")
