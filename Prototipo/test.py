from usuario import *


list_usuarios = []
list_usuarios.append(Usuario('Andre Reis', '23434366', 'andrereis@gmail.com', '32546763', 'morango', '123456'))
list_usuarios.append(Usuario('Paula Moraz', '4658674', 'paula123@gmail.com', '8864568', 'laranja', '654321'))

op = 's'

while op == 's' or op == 'S':

	print('<<<<<<<<<< OPÇÕES >>>>>>>>>>')
	print('1 - Cadastro')
	print('2 - Login')
	print('3 - Recuperar Senha')
	esc = input('Escolha a sua opção: ')
	if esc == '1':#parte onde se faz o cadastro
		n_usuario = input('Nome: ')
		num_tel = input('Numero de telefone: ')
		email = input('Email: ')
		identidade = input('Numero de identidade: ')
		r_perguta = input('Qual a sua fruta favorita: ')#Nessa parte o usuario poderá escolher ou criar a sua pergunta
		senha = input('Senha: ')
		list_usuarios.append(Usuario(n_usuario, num_tel, email, identidade, r_perguta, senha))
	
	if esc == '2':#Onde é feito Login
		login = input('Usuario: ')
		for list in list_usuarios:
			if list.n_usuario == login or list.numero == login or list.email== login:
				senha = input('Senha: ')
				list.confirmarLogin(login, senha)
				break

	if esc == '3':#onde é feito o recuperamneto de senha
		login = input('Usuario: ')
		for list in list_usuarios:
			if list.n_usuario == login or list.numero == login or list.email== login:
				identidade = input('Identidade: ')
				r_perguta = input('Qual sua fruta favorita: ')
				list.recuperarAcesso(login, identidade, r_perguta)
				break

	else:
		print('Opção invalida!!!')

	op = input('Você quer continuar?[S - sim][N - não]:')

print('Programa finalizado...')