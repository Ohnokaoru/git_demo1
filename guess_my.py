import random

start = int(input("請輸入起始數字:"))
end = int(input("請輸入中止數字:"))

ans = random.randint(start, end)
while True:
    guess = int(input(f"請猜{start}-{end}的數字:"))
    if guess > ans:
        print("猜小一點")
        if end > guess:
            end = guess - 1

    elif guess < ans:
        print("猜大一點")
        if start < guess:
            start = guess + 1

    else:
        print(f"答對了答案是{ans}")
        break
