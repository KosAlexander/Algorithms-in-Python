# 5.Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
#   https://drive.google.com/file/d/1fea_DgbzH905YaD1mmonc1jM65vSyMsB/view?usp=sharing
print('Введите две буквы')
letter_1 = input()
letter_2 = input()
num_l1 = int(ord(letter_1.lower())) - 96
num_l2 = int(ord(letter_2.lower())) - 96

if num_l1 > num_l2:
    num = num_l1 - num_l2 - 1
else:
    num = num_l2 - num_l1 - 1

print(num_l1)
print(num_l2)
print(num)
