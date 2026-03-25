#-------------------------------------------------#
######### E X E R C Í C I O S - L I S T A #########
#-------------------------------------------------#

### 1. Crie uma lista com 5 nomes e exiba o primeiro e o último.
lista_nomes = ['Mateus', 'Marcos', 'Lucas', 'João', 'Pedro']

print(f"Primeiro {lista_nomes[0]}")
print(f"Útimo {lista_nomes[-1]}")

#2. Peça ao usuário 5 números, armazene em uma lista e mostre a soma de todos.
lista_valores = []

for i in range(5):
    valor = input('Digite um valor: ')
    lista_valores.append(valor)

print(lista_valores)

#3. Crie uma lista de frutas e adicione uma nova fruta no final.
frutas = ['Maçã', 'Banana', 'Pera', 'Acerola', 'Lixia']

frutas.append('Laranja')
print(frutas)

#4. Remova um elemento específico de uma lista.
frutas2 = ['Maçã', 'Banana', 'Pera', 'Acerola', 'Lixia', 'Laranja']

frutas2.remove('Maçã')
print(frutas2)

#5. Ordene uma lista de números em ordem crescente e depois em ordem decrescente.
lista_valores2 = list(range(11))

crescente = sorted(lista_valores2)
decrescente = sorted(lista_valores2, reverse=True)

print(crescente)
print(decrescente)

#6. Crie uma lista com 10 números e mostre apenas os números pares e depois os impares.
lista_valores3 = list(range(11))

#Pares
for valor in lista_valores3:
    if valor % 2 == 0:
        print(valor)

#Impares
for valor in lista_valores3:
    if valor % 2 == 1:
        print(valor)

#7. Conte quantas vezes um elemento aparece em uma lista.
frutas3 = ['Melancia', 'Banana', 'Melancia', 'Acerola', 'Banana', 'Laranja', 'Melão', 'Melancia']
print(frutas3.count('Melancia'))

#8. Inverta a ordem dos elementos de uma lista sem usar o método reverse().
lista_valores4 = list(range(11))

print(f'Lista normal {lista_valores4}')
print(f'Lista invertida {lista_valores4[::-1]}')

#9. Crie uma lista e mostre o maior e o menor valor.
lista_valores5 = list(range(16))

maior = max(lista_valores5)
menor = min(lista_valores5)

print(f'O maior é {maior}')
print(f'O menor é {menor}')

#10. Faça um programa que multiplique todos os elementos de uma lista por 2.
lista_valores5 = list(range(21))

lista_valores_multiplicada = []

for i in lista_valores5:
    i = i *2
    lista_valores_multiplicada.append(i)

print(lista_valores_multiplicada)







