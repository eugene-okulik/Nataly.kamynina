def task_3(my_string: str, index: int):
    words = my_string.split()
    result = int(words[index]) + 10
    return result


print(task_3('результат операции: 42', 2))
print(task_3('результат операции: 54', 2))
print(task_3('результат работы программы: 209', 3))
print(task_3('результат: 2', 1))
