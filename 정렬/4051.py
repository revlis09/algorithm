tall=[]
for i in range(7):
  n=int(input())
  tall.append(n)


for j in range(0, len(tall)):
  max=j
  for x in range(j+1, len(tall)):
    if tall[x]>tall[max]:
      max=x
  tall[j], tall[max]=tall[max], tall[j]

count=1
for i in tall:
  print(i)
  if count==2:
    break
  count+=1