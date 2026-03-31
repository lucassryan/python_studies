#-------------------------------------------------------------#
######### E X E R C Í C I O S - D I C I O N Á R I O S #########
#-------------------------------------------------------------#

#1. Crie um dicionário com nome, idade e cidade de uma pessoa e exiba cada valor.
data_engineer = {
    "nome":"Lucas",
    "idade": 22,
    "cidade":"Campinas"
}

for valor in data_engineer.values():
    print(valor)

#2. Adicione uma nova chave "profissão" ao dicionário criado.
data_engineer2 = {
    "nome":"Lucas",
    "idade": 22,
    "cidade":"Campinas"
}

data_engineer2["Engenheiro de Dados"] = "profissão"
print(data_engineer2)

#3. Atualize o valor da chave "cidade" no dicionário.
data_engineer3 = {
    "nome":"Lucas",
    "idade": 22,
    "cidade":"Campinas",
    "profissao": "Engenheiro de Dados"
}

data_engineer3["cidade"] = "Hortolândia"
print(data_engineer3)

#4. Remova uma chave do dicionário e exiba o resultado.
data_engineer3 = {
    "nome":"Lucas",
    "idade": 22,
    "cidade":"Hortolândia",
    "profissao": "Engenheiro de Dados"
}

data_engineer3.pop("cidade")
print(data_engineer3)

#5. Crie um dicionário com 3 alunos e suas notas. Mostre o nome e a nota do aluno com a maior nota.
alunos = {
    "Lucas": 7,
    "Leonardo": 10,
    "Rafael": 5
}

maior_nota = max(alunos.values())

for aluno in alunos:
    if alunos[aluno] >= maior_nota:
        print(aluno, alunos[aluno])

#6. Crie um dicionário e percorra suas chaves e valores com um loop.
alunos1 = {
    "Lucas": 7,
    "Leonardo": 10,
    "Rafael": 5,
    "Pedro" : 8,
    "Tiago" : 6,
    "Ana" : 9
}

for aluno in alunos1:
    print(aluno, alunos1[aluno])

#7. Verifique se uma chave específica existe dentro do dicionário.
alunos2 = {
    "Lucas": 7,
    "Leonardo": 10,
    "Rafael": 5,
    "Pedro" : 8,
    "Tiago" : 6,
    "Ana" : 9
}
if "Lucas" in alunos2:
    print("ok")

#8. Faça um dicionário que armazene produtos e preços. Calcule o preço médio.
produtos = {
    "Arroz": 25.90,
    "Feijão": 8.50,
    "Macarrão": 5.20,
    "Óleo": 7.80,
    "Leite": 4.50
}
valores = produtos.values()
media = sum(valores) / len(produtos)
print(round(media, 2))

#9. Crie um dicionário de contatos (nome → telefone) e permita buscar um telefone pelo nome.
contatos = {
    "Lucas": "11987654321",
    "Leonardo": "11991234567",
    "Rafael": "11999887766",
    "Pedro": "11995554433",
    "Ana": "11993332211"
}

nome = input('Digite o contato que deseja obter: ')
if nome in contatos:
    print(contatos[nome])
else:
    print('Contato inexistente.')

#10. Crie um dicionário de palavras e traduções (português → inglês) e mostre as traduções solicitadas pelo usuário.
traducao = {
    "cachorro": "dog",
    "gato": "cat",
    "casa": "house",
    "carro": "car",
    "livro": "book",
    "comida": "food",
    "água": "water"
}

portugues = input('Digite a palavra a ser traduzida: ')
if portugues in traducao:
    print(traducao[portugues])
