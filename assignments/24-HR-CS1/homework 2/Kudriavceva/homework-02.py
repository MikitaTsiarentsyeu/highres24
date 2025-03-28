start = float(input("Startovyj kapital: "))
rate = float(input("Stavka %: ")) 
period = int(input("Period: "))
answer = start * (1 + rate / 100) ** period
print("Summa sostavliaet:", answer)