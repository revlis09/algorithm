def find_max(n):
  length=len(n)
  max_value=n[0]
  for i in range(1, length):
    if n[i]>max_value:
      max_value=n[i]
  return max_value

v = [17, 92, 18, 33, 58, 7, 33, 42]
#2번을 해보세요!
print(find_max(v))