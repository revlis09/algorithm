num=int(input())
arr=list(map(int, input().split()))

for i in range(0, num-1):
  min_idx=i
  for j in range(i+1, num):
    if arr[min_idx]<arr[j]:
      min_idx=j
  arr[i], arr[min_idx]=arr[min_idx],arr[i]

for x in arr:
  print(x, end=" ")