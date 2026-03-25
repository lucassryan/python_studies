#---------------------------------------------------#
######### E X E R C Í C I O S - T U P L A S #########
#---------------------------------------------------#

#1. Crie uma tupla com 4 cores e exiba o segundo elemento.
cores = ('Azul', 'Amarelo', 'Vermelho', 'Verde')
print(f'O segundo elemento é: {cores[1]}')

#2. Verifique se uma cor específica está dentro da tupla.
cores2 = ('Azul', 'Amarelo', 'Vermelho', 'Verde', 'Preto', 'Branco')

if 'Azul' in cores2:
    print('OK')
else:
    print('Não tem essa cor.')

#3. Crie uma tupla com números e exiba o maior e o menor valor.
tupla_numeros = tuple(range(21))

print(tupla_numeros)

maior = max(tupla_numeros)
menor = min(tupla_numeros)

print(f'O maior é {maior}, o menor é {menor}.')

#4. Converta uma lista em tupla e exiba o tipo antes e depois da conversão.
lista = ['Amarelo', 'Vermelho', 'Verde', 'Preto', 'Branco']
print(type(lista))

tupla = tuple(lista)
print(type(tupla))

#5. Faça um programa que conte quantas vezes um número aparece em uma tupla.
tupla3 = ('Amarelo', 'Vermelho', 'Verde', 'Preto', 'Branco', 'Branco', 'Vermelho', 'Rosa', 'Vermelho')

print(tupla3.count('Vermelho'))

#6. Crie duas tuplas e concatene-as.
tupla01 = ('Azul', 'Amarelo', 'Branco')
tupla02 = ('Preto', 'Roxo', 'Verde')

tupla03 = tupla01 + tupla02
print(tupla03)

#7. Acesse um intervalo de elementos (slice) em uma tupla.
tupla04 = ('Azul', 'Amarelo', 'Branco', 'Preto', 'Roxo', 'Verde')

print(tupla04[4:5])

#8. Crie uma tupla com 5 elementos e tente alterar um deles (observe o erro).
tupla05 = ('Azul', 'Amarelo', 'Branco', 'Preto', 'Roxo', 'Verde', 'Rosa')

tupla05['Azul'] = 'Vermelho'
print(tupla05)

#9. Crie uma tupla com nomes e exiba cada um usando um loop for.
tupla_nomes = ('Lucas', 'Pedro', 'João', 'Thiago', 'Leonardo')

for nome in tupla_nomes:
    print(nome)

#10. Crie uma tupla com 10 números e mostre apenas os números maiores que 5.

tupla_numeros01 = tuple(range(11))

for numero in tupla_numeros01:
    if numero > 5:
        print(numero)