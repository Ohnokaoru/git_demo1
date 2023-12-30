import random

start = 1
end = 50

x = random.randint(start, end)

for i in range(5):
    y = int(input(f"請猜{start}-{end}:"))
    if y == x:
        print("猜對了")
        break

    else:
        if y > x:
            print("猜低一點")

            if end > y:
                end = y - 1

        else:
            if start < y:
                start = y + 1
            print("猜高一點")

if y != x:
    print(f"猜錯了，答案為{x}")
else:
    print(f"一共猜{i+1}次")
