# 載入內建的 sys 模組並取得資訊
import sys
sys.path.append("modules") # 在模組的搜尋路徑列表中[新增路徑]
print(sys.platform)
print(sys.maxsize)

# 建立 geometry 模組，載入使用(自訂模組)
import geometry 
result = geometry.distance(1,1,5,5)
print(result)
result = geometry.slope(1,2,5,6)
print(result)

# 調整搜尋模組的路徑
import sys
print(sys.path) #印出模組的所有搜尋路徑