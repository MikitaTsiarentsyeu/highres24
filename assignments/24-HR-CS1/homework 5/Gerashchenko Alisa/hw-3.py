def kick_out(l, num):
    while num in l:
        l.remove(num)
    return l

arr = input("Input array by space: ").split()
value_to_remove = input("Input number to remove: ")

print("Updated list:", kick_out(arr, value_to_remove))
