def find_min_idx(r, v):
  for i in range(0, len(r)):
    if r[i]>v:
      return i
  return len(r)

def ins_sort(a):
  result=[]
  while a:
    value=a.pop(0)
    min_idx=find_min_idx(result, value)
    result.insert(min_idx, value)
  return result

d =[2, 4, 5, 1, 3]
print(ins_sort(d))