# dicionário
pessoa = {
'nome':'Alex Machado',
'idade':39,
'profissao':'programador',
'empresa':'SENAI'
}
print(pessoa)

# coleções
colecao1 = ['Fulano','Cicrano','Beltrano']
colecao2 = ('Brasília','São Paulo','Rio de Janeiro')
colecao3 = {'Nome':'Fulano de Tal', 'Profissao':'Programador', 'Genero':'Masculino'}
# verificando os tipos de coleções
print(type(colecao1))
print(type(colecao2))
print(type(colecao3))

# FORMA 1
pessoa = {
'nome':'Alex Machado',
'idade':39,
'profissao':'programador',
'empresa':'SENAI'
}
# exibindo os dados do dicionário
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['profissao'])
print(pessoa['empresa'])

pessoa = {
'nome':'Alex Machado',
'idade':39,
'profissao':'programador',
'empresa':'SENAI'
}
try:
    print(pessoa['cidade'])
except:
    print('Dados inexistentes')

# FORMA 2
pessoa = {
'nome':'Alex Machado',
'idade':39,
'profissao':'programador',
'empresa':'SENAI'
}
print(pessoa.get('nome'))
print(pessoa.get('idade'))
print(pessoa.get('profissao'))
print(pessoa.get('empresa'))
print(pessoa.get('cidade'))

# ADICIONANDO NOVA CHAVE
pessoa = {
'nome':'Alex Machado',
'idade':39,
'profissao':'programador',
'empresa':'SENAI'
}
# adicionando uma nova chave ao dicionário
pessoa['cidade'] = 'Brasília'
# exibindo os dados do dicionário
print(pessoa.get('nome'))
print(pessoa.get('idade'))
print(pessoa.get('profissao'))
print(pessoa.get('empresa'))
print(pessoa.get('cidade'))

# ADICIONANDO VIA INPUT
pessoa = {
'nome':'Alex Machado',
'idade':39,
'profissao':'programador',
'empresa':'SENAI'
}
# adicionando uma nova chave ao dicionário
pessoa['cidade'] = input('Informe o nome da cidade: ')
# exibindo os dados do dicionário
print(pessoa.get('nome'))
print(pessoa.get('idade'))
print(pessoa.get('profissao'))
print(pessoa.get('empresa'))
print(pessoa.get('cidade'))

pessoa = {
'nome':'Alex Machado',
'idade':39,
'profissao':'programador',
'empresa':'SENAI'
}
pessoa.pop(input('Informe a chave que deseja excluir: '), None)
# exibe os novos dados na tela
print(pessoa)