# 判斷式
x = input("請輸入數字: ")
if x:
    print("True 執行")
else:
    print("false 執行")

y=input("請輸入數字: ")
y=int(y)
if y>200:
    print("大於200")
elif y>100:
    print("大於100")
else:
    print("小於等於100")
n1=int(input("請輸入數字一:"))
n2=int(input("請輸入數字二:"))
op=input("請輸入運算:+,-,*,/")
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援")