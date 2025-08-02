num=int(input())
list=[]
for i in range(num):
  n=int(input())
  list.append(n)

swapped = True
pass_num = 0

while swapped:
    swapped = False
    for i in range(len(list) - 1 - pass_num):
        if list[i] > list[i + 1]:
            list[i], list[i + 1] = list[i + 1], list[i]
            swapped = True
    pass_num += 1 
for x in list:
  print(x)