def customsort (value,key_func) :
    return sorted(value, key=key_func)

# Example (how we can use this function :)
data = [-5, 4, 3, -9, 6]
sorted_data = customsort(data, key_func=abs)  
print("New List :", sorted_data)