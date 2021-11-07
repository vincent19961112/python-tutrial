# 函式 function
def hello():
    print("hello")
hello()

def hello1( name, age):
    print("hello" + name + "你今年" + str(age) + "歲" )
hello1("小許", 26)

def add(num1,num2):
    return num1 + num2
total = add(2,5)
print(total)