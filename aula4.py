
#Test 2

import random

num = random.randint(1, 100)

print('O número aleatório gerado é = {}'.format(num))

for num in range(num):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1
    if div == 2:
        print(num)

# Teste 1
# Calculadora de numero primo com valor aleatorio de 1 a 100

import random

NumberRandom = random.randint(1, 100) # Sorteando numero

div = 0
# Calculo de resto
for i in range(1, NumberRandom+1):
    resto = NumberRandom % i
    print('O Resto de {} divido por {} sobra {}'.format(NumberRandom,i,resto))
    if resto == 0:
        div = div + 1

if div == 2:
    print('O número {} é primo'.format(NumberRandom))
else:
    print('O número {} não é primo'.format(NumberRandom))



