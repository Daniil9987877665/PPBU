with open('code.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    key = input('Введите ключ шифрования: ')
    unsecrets = ''
    for c in s:
        code = ord(c) - int(key)
        symbol = chr(code)
        unsecrets += symbol
    print('Текст расшифрован!')

with open('decode.txt', 'w', encoding='utf-8') as f:
    f.write(unsecrets)
print('Файл "decode.txt" для отправки сформирован.')