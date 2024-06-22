class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nasc, endereco):
        self._cpf = cpf
        self._nome = nome
        self._data_nasc = data_nasc
        super().__init__(endereco)

    @property
    def cpf(self):
        return self._cpf


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
        cliente = PessoaFisica(cpf, nome, data_nasc, endereco)

        clientes.append(cliente)
        print('Cliente cadastrado com sucesso')


def main():
    clientes = []
    while True:
        opcao = menuInitial()
        if opcao == "1":
            criar_cliente(clientes)
        elif opcao == "2":
            print('Logar Usuário')
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
