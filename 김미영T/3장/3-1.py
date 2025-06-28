def search_list(a, b):
  for i in range(0, len(a)):
    if b==a[i]:
      return i
  return -1


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 900))