import random


start = 1
end = 50

x = random.randint(1, 50)
for i in range(5):
    print(x)
    y = int(input(f"請猜{start}-{end}:"))
    if y == x:
        print("猜對了")
        break

    else:
        if y > x:
            print("猜低一點")
        else:
            print("猜高一點")
