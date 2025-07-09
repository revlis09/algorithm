n=int(input())
count=0
a=[]
while count<=n+1:
  n_1=int(input())
  a.append(n)
  count+=1

na=len(a)
min=0
for i in range(na):
  min=i
  for j in range(i+1, na):
    if a[min]>a[j]:
      min=j
  a[min], a[i]=a[i], a[min]


for i in a:
  print(i) 