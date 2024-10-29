my_string = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
             'facilisis vitae semper at, dignissim vitae libero')

new_text = my_string.replace(',', 'ing,')
new_text2 = new_text.replace('.', 'ing.')
new_text_split = new_text2.split(' ')

for word in new_text_split:
    if word.endswith('ing,') or word.endswith('ing.'):
        print(word)
    else:
        result = word + 'ing'
        print(result)




