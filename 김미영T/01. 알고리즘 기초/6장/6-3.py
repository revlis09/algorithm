def find_min(a):
  min_idx=a[0]
  for i in a:
    if min_idx>i:
      min_idx=i
  return min_idx

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_min(v))