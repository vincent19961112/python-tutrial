def fn(item):

 right=len(item)-1
 length=len(item)
 result=True

 for left in range(length):

  if(item[left]==item[right]):
   right-=1
  else:
   result=False

 return result

result=fn("healeh")
print(result)