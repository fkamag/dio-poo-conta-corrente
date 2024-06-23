class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nasc, endereco, senha):
        self._cpf = cpf
        self._nome = nome
        self._data_nasc = data_nasc
        self._senha = senha
        super().__init__(endereco)

    @property
    def cpf(self):
        return self._cpf

    @property
    def nome(self):
        return self._nome

    @property
    def senha(self):
        return self._senha

    @property
    def contas(self):
        return self._contas


def buscar_cliente(cpf, clientes):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente

    return None


def criar_cliente(clientes):
    cpf = input('Digite o cpf: ')
    cliente = buscar_cliente(cpf, clientes)
    if cliente:
        print('Cliente já cadastrado')
    else:
        nome = input('Digite o nome: ')
        data_nasc = input('Digite a data de nascimento [dd-mm-aaaa]: ')
        endereco = input('Digite o endereco: ')
        while True:
            senha = input('Digite a senha: ')
            confirma_senha = input('Confirme a senha: ')
            if senha == confirma_senha:
                break
            print('Senha inválida')

        cliente = PessoaFisica(cpf, nome, data_nasc, endereco, senha)

        clientes.append(cliente)
        print('Cliente cadastrado com sucesso')


def criar_conta():
    pass


def menu_contas(cliente):
    opcao = input('''
1 - Criar Conta
2 - Listar Contas
3 - Sair

Digite sua opção: ''')
    if opcao == "1":
        criar_conta()


def listar_contas(cliente):
    cliente.contas


def logar_cliente(clientes):
    cpf = input('Digite o cpf: ')
    cliente = buscar_cliente(cpf, clientes)
    if cliente:
        senha = input('Digite a senha: ')
        if cliente.senha == senha:
            print(f'''\n Bem vindo { cliente.nome }\n''')
            menu_contas(cliente)


def main():
    clientes = []
    while True:
        opcao = menuInitial()
        if opcao == "1":
            criar_cliente(clientes)
        elif opcao == "2":
            logar_cliente(clientes)
        elif opcao == "3":
            print()
            print('Obrigado por utilizar nossos serviços')
            print()
            break
        else:
            print('Opção Inválida')


def menuInitial():
    return input('''
1 - Criar Usuário
2 - Logar Usuário
3 - Sair

Digite sua opção: ''')


main()
