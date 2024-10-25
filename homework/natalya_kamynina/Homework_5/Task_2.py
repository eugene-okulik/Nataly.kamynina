aaa = 'результат операции: 42'
start_index = aaa.index(':') + 2
result_text = aaa[start_index:]
result_int = int(result_text)
result = result_int + 10
print(result)

print('_' * 100)

bbb = 'результат операции: 514'
start_index1 = bbb.index(':') + 2
result_text1 = bbb[start_index1:]
result_int1 = int(result_text1)
result1 = result_int1 + 10
print(result1)

print('_' * 110)

ccc = 'результат работы программы: 9'
start_index2 = ccc.index(':') + 2
result_text2 = ccc[start_index2:]
result_int2 = int(result_text2)
result2 = result_int2 + 10
print(result2)
