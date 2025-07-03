def print_all_friends(g, v):
  qu=[]
  done=set()
  qu.append(v)
  done.add(v)
  while qu:
    a=qu.pop()
    print(a)
    for x in g[a]:
      if x not in(done):
        qu.append(x)
        done.add(x)




fr_info = {
    'Summer': ['John', 'Justin', 'Mike'],
    'John': ['Summer', 'Justin'],
    'Justin': ['John', 'Summer', 'Mike', 'May'],
    'Mike': ['Summer', 'Justin'],
    'May': ['Justin', 'Kim'],
    'Kim': ['May'],
    'Tom': ['Jerry'],
    'Jerry': ['Tom']
}

print_all_friends(fr_info, 'Summer')
print()
print_all_friends(fr_info, 'Jerry')
