from time import sleep

class Interface():
    def __init__(self) -> None:
        print("Bem-vindo à loja do General!")

    def opcaoInvalida(self) -> None:
        print("Opção inválida. Digite uma opção válida.\n")

    def senhaInvalida(self) -> None:
        print("Senha inválida. Tente novamente.\n")

    def exibirPedido(self) -> None:
        pass

    def validarInput(self, input_:str, opcoes_validas:list[int]) -> int | ValueError:
        input_ = input_.strip()
        try:
            input_ = int(input_)
            if input_ in opcoes_validas:
                return input_
            return ValueError
        except:
            return ValueError

    def opcoesTelaInicial(self) -> int | ValueError:
        input_ = input("Digite uma opção:\n1 - Adicionar bebida ao carrinho\n" \
        "2 - Acesso restrito\n3 - Sair\n")
        opcoes_validas:list[int] = [1, 2, 3]
        return self.validarInput(input_, opcoes_validas)
    
    def verificarSenha(self) -> str:
        senha = input("Digite a senha para obter acesso restrito. Pressione " \
        "Enter para retornar à tela inicial.\n")
        senha = senha.strip()
        return senha
    
    def opcoesAcessoRestrito(self) -> int | ValueError:
        input_ = input("Digite uma opção:\n1 - Checar saldo\n2 - Estocar item\n" \
        "3 - Retornar à tela inicial\n")
        opcoes_validas:list[int] = [1, 2, 3]
        return self.validarInput(input_, opcoes_validas)
    
    #TODO: implement sleep to mimic payment
    def opcoesFinalizarCompra(self) -> int | ValueError:
        input_ = input("Escolha uma forma de pagamento:\n1 - Pix\n2 - Débito\n"
                       + "3 - Crédito\n4 - Retornar à tela inicial\n")
        opcoes_validas:list[int] = [1, 2, 3, 4]
        return self.validarInput(input_, opcoes_validas)