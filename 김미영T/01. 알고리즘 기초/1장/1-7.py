def find_same_name(a):
  n=len(a)
  result=set()
  for i in range(n+1):
    for j in range(i+1, n):
      if a[i]==a[j]:
        result.add(a[i])
  return result


name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]  # 대소문자 유의: 파이썬은 대소문자를 구분함
#2번을 해보세요!
print(find_same_name(name))