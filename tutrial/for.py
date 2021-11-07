# for 迴圈

# for 變數 in 字串OR列表
# 要重複執行的程式碼
# 五次迴圈
for num in [0,1,2,3,4]:
    print(num)
# 五十次迴圈
for num in range(50):
    print(num)
# 2->7 不包括7
for num in range(2,7):
    print(num)
def power(base,doub):
    result = 1
    for num in range(doub):
        result *= base
    return result
result = power(4,2)
print(result)
