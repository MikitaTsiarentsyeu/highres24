import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()  
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        return {
            "result": result,
            "execution_time": elapsed_time
        }
    return wrapper
#Slow function
@timer
def slow_function():
    time.sleep(2)
    return "Медленная функция завершена!"
#Fast function
@timer
def fast_function():
    return sum(range(1000)) 

#Using decorator
slow_output = slow_function()
fast_output = fast_function()

print("Результат медленной функции:", slow_output["result"])
print("Время выполнения медленной функции:", slow_output["execution_time"], "секунд")

print("Результат быстрой функции:", fast_output["result"])
print("Время выполнения быстрой функции:", fast_output["execution_time"], "секунд")

