n=int(input())
a=[]
for i in range(n):
  x=list(input().split())
  a.append(x)

for i in a:
  y=len(i)
  for j in range(i):
    if j==0:
      j=int(j)