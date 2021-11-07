s1={3,4,5}
print(3 in s1) # true
print(10 not in s1) # true
s2={4,5,6,7}
s3=s1&s2 #交集: 取兩個集合中，相同的資料
print(s3)
s4=s1|s2 #聯集: 取兩個集合中的所有資料，但不重複取
print(s4)
s5=s1-s2 #差集: 從 s1 中，減去和 s2 重複的部分
print(s5)
s6=s1^s2 #反交集: 取兩個集合中，不重疊的部分
print(s6)
s=set("hello") # set(字串) 字串被拆解成集合
print("h" in s)

# 字典的運算: key-value 配對
dic={"apple":"蘋果","bug":"蟲蟲"}
dic1={x:x*2 for x in [3,4,5]}
print(dic1)
dic2={i:i for i in ["apple","蘋果","bug","蟲蟲"]}
print(dic2)


