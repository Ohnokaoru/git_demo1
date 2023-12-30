import random

start = int(input("請輸入起始數字:"))
end = int(input("請輸入中止數字:"))

ans = random.randint(start, end)
while True:
    guess = int(input(f"請輸入猜的數字:"))
    if guess > ans:
        end = guess
        print("猜小一點")
        print(f"答案介於{start}-{end-1}")

    elif guess < ans:
        start = guess
        print("猜大一點")
        print(f"答案介於{start+1}-{end}")
    else:
        print(f"答對了答案是{ans}")
        break
