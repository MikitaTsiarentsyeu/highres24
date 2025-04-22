def primecheck(n):
  i=2
  while i*i<=n:
    if n%i==0:
      return False
  return True
