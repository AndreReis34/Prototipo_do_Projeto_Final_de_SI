from hashlib import sha256

class Usuario:
	def __init__(self, n_usuario, numero, email, identidade, r_perguta, senha):#ainda estou pensando e  botar um confirmador de produto
		self.n_usuario = n_usuario
		self.numero = numero
		self.email = email
		self.identidade = sha256(identidade.encode()).digest()#ESSA OPERAÇÃO TRANSFORMA OS DADOS EM BITS E DEPOIS ARMAZENA NO ATRIBUTOS
		self.r_perguta = sha256(r_perguta.encode()).digest()
		self.senha = sha256(senha.encode()).digest()
		print('Conta criada com sucesso!!!')

# area onde é confirmado o acesso do usuario no sistema
	def confirmarLogin(self, id, senha):#botar um return True mais tarde ou mais funções
		if self.n_usuario == id or self.numero == id or self.email == id:
			print('Usuario é cadastrado no sistema...')
			if self.senha == sha256(senha.encode()).digest():
				print('Bem vindo ao sistema...')
			else:
				print('Senha incorreta!!!')
		else:
			print('Usuario não cadastrado no sistema...')


# area para recuperar o acesso ao sistema com alguns alementos se são preenchidos no cadastro
	def recuperarAcesso(self, id, identidade, r_perguta):#se usa identidade e eprguntas para a recuperação
		if self.n_usuario == id or self.numero == id or self.email == id:
			print('Usuario é cadastrado no sistema...')
			if self.identidade == sha256(identidade.encode()).digest() and self.r_perguta == sha256(r_perguta.encode()).digest():
				print('Identidade comprovada com sucesso! Você pode digitar uma nova senha...')
			else:
				print('Identidade invalida!!!')
		else:
			print('Usuario não está cadastrado no sistema')