# 列表list，列表的用法
scores = [90,70,60,50,60]
friends = ["小黑","小黃","小斯"]
things = [90,"小黑",True]
print(scores)
# 列表list 最後一值
print(scores[-1])
# 列表list 從0到2顯示(2不顯示)
print(scores[0:2])
# sort() 由小到大排列
scores.sort()
print(scores)
# extend() 延伸其他list到最後一個
scores.extend(things)
print(scores)
# append() 從最後加入一個值
scores.append(100)
print(scores)
# insert() 插入(位置,值)
scores.insert(2,30)
print(scores)
# remove() 刪除(值)
scores.remove(90)
print(scores)
# pop() 移除最後一位
scores.pop()
print(scores)
# reverse() 順序反轉
scores.reverse()
print(scores)
# index() 尋找第一個相同值的位置
scores.index(70)
print(scores)
# count() list 裡有幾個值
scores.count(70)
print(scores)
# clear() 清除列表
scores.clear()
print(scores)
