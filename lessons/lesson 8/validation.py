

while True:

    try:
        value = input("enter a positive integer number")
        
        try:
            value = int(value)
        except ValueError:
            raise RuntimeError("Please try again enter an interger value next time")

        if value < 0:
            raise RuntimeError("The number should be positive, please try again")


    except RuntimeError as e:
        print(e)
        continue

    break