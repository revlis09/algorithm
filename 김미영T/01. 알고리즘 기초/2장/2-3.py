def gcd(a, b):
  if (a<b):
    i=a
  elif(a>b):
    i=b
  while True:
    if a%i==0 and b%i==0:
      return i
    i-=1

print(gcd(3, 6))