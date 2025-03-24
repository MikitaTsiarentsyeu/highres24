

while True:

    res = input("Enter an integer bigger than 100:\n")

    if not res.isdigit():
        print("Please try again and eneter a number")
        continue

    if '.' in res:
        print("Please try again and eneter an integer number")
        continue

    res = int(res)

    if res < 100:
        print("Please try again and eneter an integer number bigger than 100")
        continue

    break

print(res)


