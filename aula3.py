# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('foi digitado numero par')
# else:
#     print('nenhum numero par')

a = int(input('Primeiro bimestre: '))
b = int(input('segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
d = int(input('quarto Bimestre: '))

media = (a + b + c + d) / 4

if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('media : {}' .format(media))
else:
    print('Valor invalido digite entre 0 a 10 ' )