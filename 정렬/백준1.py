a=list(map(int,input().split()))
n=len(a)
for i in range(n):
  key=a[i]
  j=i-1
  while j>=0 and a[j]>=key:
    a[j+1]=a[j]
    j-=1
  a[j+1]=key

for i in a:
  print(i, end=" ")
