s = 'ЗдрАвстВуйте, гости!'
print(n := s.lower())
print(s.upper())
print(s.title()) # все слова начинаются с большой буквы
print(s.capitalize()) # переменная начинается с большой буквы
print(s.rjust(40)) # переменная пишется в 40 знакоместах выравнивание по правому краю
print(s.ljust(40))
print(s.center(40))
print(s.strip()) # удаляем пробелы по краям
print(s.strip('! Зд'))
print(s.rstrip()) # убирает пробелы справа переменной
print(s.lstrip())
print(s.index('т', 8, 12)) # поиск индекса символа или начала подстроки
print(s.find('т', 8, 11))
print(s.replace('т', 'LN').replace(',', ''))
ls = s.split() # создает список разделяя слова по пробелу
ls = s.split(', ') # создает список разделяя слова по запятой
# с пробелом
print(ls)
print(", ".join(ls))

