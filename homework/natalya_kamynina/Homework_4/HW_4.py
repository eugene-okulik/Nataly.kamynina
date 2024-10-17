my_dict = {
    'tuple': (1, 22, 'text', True, 2.4),
    'list': ['one', '2.5', 'AAA', '55', 'False'],
    'dict': {
        '1': 'Mama',
        'two': 'Papa',
        '3': 'Sister',
        'four': 'Big Brother',
        '5': 'Little Brother'
    },
    'set': {1, 2, 3, 4, 5}
}

print(my_dict['tuple'][-1])
print('-' * 100)

my_dict['list'].append('88')
my_dict['list'].pop(1)
print(my_dict['list'])
print('-' * 100)

my_dict['dict']['i am a tuple'] = '2'
del my_dict['dict']['5']
print(my_dict['dict'])
print('-' * 100)

my_dict['set'].add(888)
my_dict['set'].remove(5)
print(my_dict['set'])
print('-' * 100)

print(my_dict)
print('-' * 100)
