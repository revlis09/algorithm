num=int(input())
n=list(map(int, input().split()))

swapped = True
pass_num = 0

while swapped:
    swapped = False
    for i in range(len(n) - 1 - pass_num):
        if n[i] > n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
            swapped = True
    pass_num += 1 

print(pass_num-1)