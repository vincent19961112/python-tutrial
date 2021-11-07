# 建立一個基本計算機
number1 = input("請輸入第一個數字:")
operation = input("請輸入運算符號:")
number2 = input("請輸入第二個數字:")
n1 = float(number1)
n2 = float(number2)
total = 0

def operaters_to_total(argument):
  switcher = {
  "+": n1 + n2,
  "-": n1 - n2,
  "*": n1 * n2,
  "/": n1 / n2
  }
  return switcher.get(argument)
total = operaters_to_total(operation)
print("結果是:"+str(total))