def kick_out(lst: list, val: object) -> None:
    i = 0
    while i < len(lst):
        if lst[i] == val:
            lst.pop(i)  
        else:
            i += 1  

my_list = list(map(int, input("Введите список чисел через пробел: ").split()))
value_to_remove = int(input("Введите значение для удаления: "))
print("Исходный список:", my_list)
kick_out(my_list, value_to_remove)
print("Список после удаления:", my_list)