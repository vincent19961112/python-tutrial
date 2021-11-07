# 儲存檔案
# file=open("data.txt", mode="w",encoding="utf-8") # 開啟
# file.write("hello File\nSecond Line") # 操作
# file.write("\n測試中文")
# file.close() # 關閉

# 同上方式
# with open("data.txt", mode="w", encoding="utf-8")as file:
# 	file.write("5\n3")
# 讀取檔案
# with open("data.txt",mode="r",encoding="utf-8") as file:
# 	data=file.read()
# print(data)

# 使用 JSON 格式讀取、複寫檔案
# sum=0
# with open("data.txt",mode="r",encoding="utf-8") as file:
# 	for line in file:
# 		sum+=int(line)
# print(sum)
import json
with open("config.json",mode="r") as file:
	data=json.load(file)
print("name: ",data["name"])
data["name"]="New Name"
with open("config.json",mode="w") as file:
	json.dump(data, file)