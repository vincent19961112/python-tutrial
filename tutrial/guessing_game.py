# 猜數字遊戲
import random

RandomNumber = int(100 * random.random())
inputValue = 0

while inputValue != RandomNumber:
    inputValue = int(input("請輸入數字:"))
    if (inputValue > RandomNumber):
        print("輸入小一點的數字")
    elif (inputValue < RandomNumber):
        print("輸入大一點的數字")
print("你猜到了")