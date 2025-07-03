def palindrome(a):
  qu=[]
  st=[]
  for i in a:
    if i.isalpha():
      qu.append(i.lower())
      st.append(i.lower())
  for j in qu:
    if j != st.pop():
      return False
  return True


print(palindrome("Madam, I’m Adam."))
print(palindrome("Madam, I am Adam."))
print(palindrome("kayak"))