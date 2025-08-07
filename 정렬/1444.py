num=int(input())
b=[]
for i in range(num):
  a=int(input())
  b.append(a)

n=len(b)
for y in range(1, n):
  key=b[y]
  j=y-1
  while j>=0 and b[j]>key:
    b[j+1]=b[j]
    j-=1
  b[j+1]=key

for x in b:
  print(x)
