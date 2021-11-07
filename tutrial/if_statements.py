# if判斷
if True:
    print('True')
else:
    print('false')

if False:
    print('True')
else:
    print('false')

score = input("請輸入你的分數:")

if (int(score) == 100):
    print("獎勵: 100")
elif (int(score) >= 80):
    print("獎勵: 50")
elif (int(score) >= 60):
    print("獎勵: 20")
elif (int(score) >= 20):
    print("獎勵: 5")
else:
    print("獎勵: 1")

def max_num(num1,num2,num3):
    if(num1 >= num2 and num1 >= num3):
        return num1
    elif(num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3

maxnum = max_num(1,3,2)

print(maxnum)
