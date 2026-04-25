class Interface():
    def __init__(self) -> None:
        print("Bem-vindo à loja do General!")

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
        input_ = input("Digite uma opção:\n1 - Adicionar bebida ao carrinho\n" 
        + "2 - Acesso Restrito\n3 - Sair\n")
        opcoes_validas:list[int] = [1, 2, 3]
        return self.validarInput(input_, opcoes_validas)
    
    def verificarSenha(self) -> str:
        input_ = input("Digite a senha para obter acesso restrito.")
        input_ = input_.strip()
        return input_