aaa = 5

while True:
    user_input = input('Enter a number between 1 - 20  or stop to exit: ')
    if str(aaa) == user_input:
        print('Congrats!!! You won!')
        break
    elif user_input == 'stop':
        print('Bye bye!!!')
        break
    else:
        print('Try again')
