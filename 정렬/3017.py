n=int(input())
a=[]
for i in range(n):
  score, score2=map(int, input().split())
  a.append([i+1, score, score2])

for i in range(len(a)-1):
  max_score=i
  for j in range(i+1, len(a)):
    if a[j][1]>a[max_score][1]or \
      (a[j][1] == a[max_score][1] and a[j][2] > a[max_score][2]) or \
      (a[j][1] == a[max_score][1] and a[j][2] == a[max_score][2] and a[j][0] < a[max_score][0]): 
      max_score=j
  a[max_score], a[i]=a[i],a[max_score]

for i in a:
  print(i[0], i[1], i[2])