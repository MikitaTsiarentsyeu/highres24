startSum = float(input())
interest = float(input())/100
time = float(input())
currentAmount = startSum
for i in range(time):
  currentAmount *= (interest+1)
totalBalance = currentAmount
print(totalBalance) 
