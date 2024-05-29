import os

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
'Nome': Nome,
'CPF': Cpf,
'RG': Rg,
'Data Nascimento': DataNasc,
'Gênero': Genero,
'E-mail': Email,
'Telefone': Telefone,
'Tipo Sanguíneo':TipoSanguineo,
'Profissão':Profissao,
'Empresa':Empresa
}

os.system('cls')

print("Dados da Pessoa:\n")

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')

