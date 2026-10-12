with open('text.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    key = input('Введите ключ шифрования: ')
    secrets = ''
    for c in s:
        code = ord(c) + int(key)
        symbol = chr(code)
        secrets += symbol
    print('Текст зашифрован!')

with open('code.txt', 'w', encoding='utf-8') as f:
    f.write(secrets)
print('Файл "code.txt" для отправки сформирован.')