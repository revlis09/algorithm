num=int(input())
list=[]
for i in range(num):
  n=int(input())
  list.append(n)
n=len(list)

for i in range(0, n-1):
  min_idx=i
  for j in range(i+1, n):
    if list[min_idx]>list[j]:
      min_idx=j
  list[i], list[min_idx]=list[min_idx],list[i]

for x in list:
  print(x)
  