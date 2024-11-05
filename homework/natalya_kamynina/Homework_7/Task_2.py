words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}
for key in words:
    if key.startswith('I'):
        print(key * words['I'])
    elif  key.startswith('l'):
        print(key * words['love'])
    elif key.startswith('P'):
        print(key)
    else:
        print(key * words['!'])
