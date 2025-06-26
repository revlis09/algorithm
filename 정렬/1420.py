num=int(input())
top_1=("", -1)
top_2=("", -1)
top_3=("", -1)

for i in range(num):
  name, score=input().split()
  score=int(score)
  if score>top_1[1]:
    top_3=top_2
    top_2=top_1
    top_1=(name, score)
  elif score>top_2[1]:
    top_3=top_2
    top_2=(name, score)
  elif score>top_3[1]:
    top_3=(name,score)
print(top_3[0])
  