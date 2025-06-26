def sel_sort(a):
  n=len(a)
  for i in range(0, n-1):#마지막 숫자는 자동으로 정렬되기 떄문에 n-2까지 반복문으로 돌리기
    min_idx=i #i가 가장 작은 인덱스라고 정렬
    for j in range(i+1, n): # i 다음 요소부터 끝까지 검사해서 최솟값 찾기
      if a[j]<a[min_idx]:
        min_idx=j
    a[i], a[min_idx]=a[min_idx], a[i]
    print(a)

d=[2, 4, 5, 1, 3]
sel_sort(d)
print(d)