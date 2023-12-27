import random

x=random.randint(1,50)
for i in range(5):
    print(x)
    guess=int(input("請猜1-50:"))
    if guess==x:
        print("猜對了")
        break

    else:
        print("猜錯了")

