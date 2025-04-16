def removeElement(l: list, val: object) -> None:
    while val in l:  #While element exist in list
        l.remove(val) #Remove element

inputList = input("Enter numbers, separated by spaces: ")
myList = [int(i) for i in inputList.split()]
inputElement = int(input("Enter specific element: "))
removeElement(myList, 2)
print(myList) #Print List