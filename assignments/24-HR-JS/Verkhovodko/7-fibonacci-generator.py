def fib_gen(n):
  nums = {
    0: 0, 
    1: 1
  }
     
  def generateNum(m):
    if m not in nums:
      nums[m] = fib(m-1) + fib(m-2)
    return nums[k]
     
  def fibonacci(k):
    for i in range(k):
       yield generateNum(i)
      
  return fibonacci
       
