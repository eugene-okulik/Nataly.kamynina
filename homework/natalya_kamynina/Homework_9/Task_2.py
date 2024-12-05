import datetime

given_time = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(given_time, '%b %d, %Y - %X')
month_name = python_date.strftime('%B')
new_format = datetime.datetime.strftime(python_date, '%d.%m.%Y, %I:%M')

print(f'python format: {python_date}')
print('==' * 50)
print(f'full name of the month: {month_name}')
print(f'new date formate: {new_format}')
