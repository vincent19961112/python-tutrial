# 參數的預設資料
def power(base,exp=0):
	return base**exp
result=power(3,2)
print(result)
result=power(4)
print(result)
# 使用參數名稱對應
def divide(n1,n2):
	print(n1/n2)
divide(2,4)
divide(n2=2,n1=4)
#無限/不定 參數資料
def avg(*ns): #不定長度的參數資料
	res=0
	for x in ns:
		res+=x
	return res/len(ns)
result=avg(3,4)
print(result)