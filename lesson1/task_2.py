# 2.Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
#   Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
#   https://drive.google.com/file/d/1scROf123rN5mehlWb5gat5JvfS0a7sx8/view?usp=sharing
a = 5
b = 6

c = bin(a & b)
print(c)

c = bin(a | b)
print(c)

c = bin(a >> 2)
print(c)

c = bin(a << 2)
print(c)

