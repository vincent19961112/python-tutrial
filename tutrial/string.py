# 如何使用字串，字串的用法
print("Hello \nMr.White")
# \n 換行
print("Hello\"Mr.White")
# \" 斜線後不是雙引號而是字串
print("Hello"+"Mr.White")

#函式 lower() islower() upper() isupper() index() int() float()

phrase = "Hello Mr.white"
# 所有字串變成小寫
print(phrase.lower())
# 是否所有字串都是小寫 否
print(phrase.islower())
# 同上兩個函式相加 是
print(phrase.lower().islower())
# 所有字串變成大寫
print(phrase.upper())
# 是否所有字串都是大寫 否
print(phrase.isupper())
# 同上兩個函式相加 是
print(phrase.upper().isupper())
# 尋找字串位置 0
print(phrase.index("H"))
# 替換字串
print(phrase.replace("H","h"))
# 將字串轉換成正整數
print(int("851112"))
# 將字串轉換成浮點數
print(float("851112.125"))
