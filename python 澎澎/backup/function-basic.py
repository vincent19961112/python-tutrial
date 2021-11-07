n1=int(input("請輸入n1: "))
n2=int(input("請輸入n2: "))

# 定義函數
def multiply(n1,n2):
	return n1*n2

# 呼叫函數
result=multiply(n1,n2)
print(result)

# 程式的包裝
def Accumulate(num):
	sum=0
	for x in range(num+1):
		sum+=x
	return sum
num1 = int(input("請輸入:"))
result=Accumulate(num1)
print(result)