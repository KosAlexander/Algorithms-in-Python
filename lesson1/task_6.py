# 6.Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
#  https://drive.google.com/file/d/1lGVK6eUG1vtkmXW-_DupYo6i26xslruw/view?usp=sharing
number = int(input('Введите номер буквы в алфавите: '))

char = chr(number + 96)

print(char)