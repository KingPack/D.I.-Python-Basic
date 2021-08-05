# code test 

#teste 1
a = 10

b = 5

soma = a + b
subtracao = a - b
multiplicacao =  a * b
divisao = a / b
resto = a % b

#test 1 script
print ('soma : {soma}.'
    '\n subtração : {subtracao}.'
    '\n multiplicação : {multiplicacao}.'
    '\n divisão : {divisao}.'
    '\n Resto :{resto}'
        .format(soma = soma,
                subtracao = subtracao,
                resto = resto,
                divisao = divisao,
                multiplicacao = multiplicacao) )

print (type (soma),type(multiplicacao),type(divisao),type(resto))


#test 2

c = int(input('Primeiro valor:' ))
d = int(input('Segundo valor:'  ))

soma2 = c + d
subtracao2 = c - d
multiplicacao2 =  c * d
divisao2 = a / b
resto2 = a % b

resultado = ('soma : {soma2}.'
    '\n subtração : {subtracao2}.'
    '\n multiplicação : {multiplicacao2}.'
    '\n divisão : {divisao2}.'
    '\n Resto :{resto2}'
        .format(soma2 = soma2,
                subtracao2 = subtracao2,
                resto2 = resto2,
                divisao2 = divisao2,
                multiplicacao2 = multiplicacao2))

print(resultado)