def binary_search(a, v):
  start=0
  end=len(a)

  while start<=end:
    mid=(start+end)//2
    if v==a[mid]:
      return mid
    elif v>a[mid]:
      start=mid+1
    else:
      end=mid-1

  return -1
    

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))