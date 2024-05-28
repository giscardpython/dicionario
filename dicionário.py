
Nome = input('\nInforme o nome da pessoa: ')
Cpf  = int(input('\nInforme o CPF: '))
Rg   = int(input('\nInforme o RG: '))
DataNasc = input('\nInforme a Data de Nascimento: ')
Genero = input('\nInforme o Gênero: ')
Email = input('\nInforme o E-mail: ')
Telefone = input('\nInforme o Telefone: ')
TipoSanguineo = input('\nInforme o Tipo Sanguineo: ')
Profissao = input('\nInforme a Profissão: ')
Empresa = input('\nInforme a Empresa: ')

# dicionário
pessoa = {
'nome': Nome,
'cpf': Cpf,
'rg': Rg,
'datanasc': DataNasc,
'genero': Genero,
'email': Email,
'telefone': Telefone,
'tiposanguineo':TipoSanguineo,
'profissao':Profissao,
'empresa':Empresa
}

print("Dados da Pessoa:\n")

print(pessoa['nome'])
print(pessoa['cpf'])
print(pessoa['rg'])
print(pessoa['datanasc'])
print(pessoa['genero'])
print(pessoa['email'])
print(pessoa['telefone'])
print(pessoa['tiposanguineo'])
print(pessoa['profissao'])
print(pessoa['empresa'])


