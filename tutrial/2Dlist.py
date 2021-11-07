nums = [
    [0,1,2],  # [0][0,1,2]
    [3,4,5],  # [1][0,1,2]
    [6,7,8],  # [2][0,1,2]
    [9]       # [3][0]
]

for row in nums:
    for col in row:
       print(col)

for num1 in range(1,10):
    for num2 in range(1,10):
       result = num1 * num2
       print(str(num1) + " * " + str(num2) + " = " + str(result))

