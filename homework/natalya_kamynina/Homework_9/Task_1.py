temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

def is_hot_days(x):
    return x > 28

temperatures = filter(is_hot_days, temperatures)
new_list = (list(temperatures))
max_temp = max(new_list)
min_temp = min(new_list)
aver_temp = sum(new_list) / len(new_list)

print(f"my new list: {new_list}")
print(f"my new sorted list: {sorted(new_list)}")
print('==' * 50)
print(f"max temp: {max_temp}")
print(f"min temp: {min_temp}")
print(f"average temp: {round(aver_temp)}")

