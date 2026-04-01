#----------------------------------------------------------#
######### E X E R C Í C I O S - C O N J U N T O S #########
#----------------------------------------------------------#

#1. Crie dois conjuntos: {1, 2, 3} e {3, 4, 5}. Mostre a união deles.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1 | set2
print(set3)

#2. Mostre a interseção entre os dois conjuntos do exercício anterior.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set4 = set1 & set2
print(set4)

#3. Mostre a diferença entre os dois conjuntos.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set5 = set1 - set2
print(set5)

#4. Adicione um novo número ao conjunto {10, 20, 30} e remova outro.
set6 = {10, 20, 30}

set6.add(40)
set6.remove(10)

print(set6)

#5. Crie um conjunto com números repetidos e mostre como o Python automaticamente remove duplicatas.
set7 = {1, 1, 4, 5, 6, 7, 6, 8, 9, 10, 9}
print(set7)

#6. Verifique se dois conjuntos são disjuntos (não têm elementos em comum).
times1 = {'Guarani', 'Bragantino', 'Palmeiras', 'Portuguesa'}
times2 = {'Corinthians', 'São Paulo',  'Santos', 'Mirassol'}

if times1.isdisjoint(times2):
    print('Sim')

#7. Verifique se um conjunto é subconjunto de outro.
times1 = {'Guarani', 'Bragantino', 'Palmeiras', 'Portuguesa'}
times2 = {'Corinthians', 'São Paulo',  'Santos', 'Mirassol'}

if times1.issubset(times2):
    print('Sim')
else:
    print('Não')

#8. Copie um conjunto para outro e adicione novos elementos no segundo.
times1 = {'Guarani', 'Bragantino', 'Palmeiras', 'Portuguesa'}
times2 = {'Corinthians', 'São Paulo',  'Santos', 'Mirassol'}

times2 = times1.copy()
times2.update(['Santo André', 'São Bernardo'])
print(times2)

#9. Converta uma lista em conjunto e exiba o resultado.
lista = list(range(21))

lista_convertida = set(lista)
print(lista_convertida)

#10. Peça ao usuário 5 números, armazene em um conjunto e exiba a quantidade de elementos únicos.
user_numeros = set()

for i in range(5):
    numeros = input('Digite um número: ')
    user_numeros.add(numeros)
print(len(user_numeros))



