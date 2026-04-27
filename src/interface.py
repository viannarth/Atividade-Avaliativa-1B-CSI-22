from src.constantes import TipoItem, Doses
from time import sleep

class Interface():
    def __init__(self) -> None:
        print("Bem-vindo à maquina de vendas do General!")

    def estadoEspera(self) -> None:
        input("")

    def opcaoInvalida(self) -> None:
        print("Opção inválida. Digite uma opção válida.")
        self.estadoEspera()

    def senhaInvalida(self) -> None:
        print("Senha inválida. Tente novamente.")
        self.estadoEspera()

    def itemAdicinado(self) -> None:
        print("Item adicionado ao estoque com sucesso.")
        self.estadoEspera()

    def exibirSaldoMaquina(self, saldo_total:int, saldo_lata:int, 
    saldo_dosada:int) -> None:
        print("\nSaldo da máquina de vendas:")
        print(f"\tSaldo total de bebidas: {saldo_total}")
        print(f"\tSaldo de bebida dosadas: {saldo_dosada}")
        print(f"\tSaldo de bebidas em lata: {saldo_lata}")
        self.estadoEspera()

    def exibirEstoque(self, tipo_itens:list[TipoItem], nome_itens:list[str], quantidades:list[int]) -> None:
        dict_estoque:dict[TipoItem, list[tuple[str, int]]] = {tipo_item: [] for tipo_item in TipoItem}
        for idx, nome in enumerate(nome_itens):
            dict_estoque[tipo_itens[idx]].append((nome, quantidades[idx]))

        if len(dict_estoque[TipoItem.INGREDIENTE]) == 0 and len(dict_estoque[TipoItem.LATA]) == 0:
            print("O estoque está vazio.")
            return

        print("\nEstoque:")
        for tipo_item in TipoItem:
            if len(dict_estoque[tipo_item]) != 0: 
                print(f"\t{tipo_item.name.capitalize()}s:")
                for tupla in dict_estoque[tipo_item]:
                    nome:str = tupla[0]
                    quantidade:int = tupla[1]
                    print(f"\t\t{nome.capitalize()}: {quantidade}", end=" ")
                    if tipo_item == TipoItem.INGREDIENTE:
                        print("gramas")
                    elif tipo_item == TipoItem.LATA:
                        print("unidades")

    def exibirCarrinho(self, valor_total: int, nomes_bebidas:list[str], quantidades:list[int]) -> None:
        print("\nCarrinho:")
        for nome, quantidade in zip(nomes_bebidas, quantidades):
            print(f"\t{nome.capitalize()}: {quantidade}")
        print(f"Total a pagar: R${valor_total:.2f}")

    def _validarInput(self, input_:str, opcoes_validas:list[int]) -> int | ValueError:
        input_ = input_.strip()
        try:
            input_ = int(input_)
            if input_ in opcoes_validas:
                return input_
            return ValueError
        except:
            return ValueError
    
    def opcoesTelaInicial(self) -> int | ValueError:
        input_ = input("\nDigite uma opção:\n1 - Adicionar bebida ao carrinho\n" \
        "2 - Acesso restrito\n3 - Sair\n")
        opcoes_validas:list[int] = [1, 2, 3]
        return self._validarInput(input_, opcoes_validas)
    
    def verificarSenha(self) -> str:
        senha = input("\nDigite a senha para obter acesso restrito. Pressione " \
        "Enter para retornar à tela inicial.\n")
        senha = senha.strip()
        return senha
    
    def opcoesAcessoRestrito(self) -> int | ValueError:
        input_ = input("\nDigite uma opção:\n1 - Checar saldo\n2 - Consultar " 
        "estoque\n3 - Estocar item\n4 - Retornar à tela inicial\n")
        opcoes_validas:list[int] = [1, 2, 3, 4]
        return self._validarInput(input_, opcoes_validas)
    
    def receberItem(self) -> tuple[int, str, int] | ValueError:
        input_ = input("\nDigite o tipo de item a ser estocado:\n1 - Ingrediente\n"
        "2 - Bebida em Lata\n")
        opcoes_validas = [1, 2]
        tipo_item = self._validarInput(input_, opcoes_validas)
        if tipo_item == ValueError:
            return ValueError
        input_ = input("\nDigite o nome do item a ser estocado.\n")
        nome_item = input_.strip().capitalize()
        if nome_item == "":
            return ValueError
        input_ = input("\nDigite a quantidade do item a ser estocado.\n")
        try:
            quantidade = int(input_)
        except:
            return ValueError
        if quantidade < 0: 
            return ValueError
        return (tipo_item, nome_item, quantidade)
    
    def opcoesEscolhaBebida(self, carrinho_vazio:bool) -> int | ValueError:
        if carrinho_vazio:
            input_ = input("\nDigite uma opção:\n1 - Escolher bebida lata\n2 - Montar bebida " 
            "dosada\n3 - Retornar à tela inicial\n")
            opcoes_validas:list[int] = [1, 2, 3]
            return self._validarInput(input_, opcoes_validas)
        else:
            input_ = input("\nDigite uma opção:\n1 - Escolher bebida lata\n2 - Montar bebida " 
            "dosada\n3 - Finalizar compra\n4 - Cancelar compra\n")
            opcoes_validas:list[int] = [1, 2, 3, 4]
            return self._validarInput(input_, opcoes_validas)
        
    def escolherIngrediente(self) -> str:
        input_ = input("\nEscolha um ingrediente:\n")
        return input_.strip()
    
    def escolherSegundoIngrediente(self) -> str:
        input_ = input("\nEscolha o segundo ingrediente:\n")
        return input_.strip()
    
    def aguaInsuficiente(self) -> None:
        print("\nEstoque de água insuficiente. Chame alguém autorizado para abastecer.\n")
        self.estadoEspera()
        
    def escolherDose(self) -> Doses | ValueError:
        input_ = input("Escolha uma dose:\n1 - 30%\n2 - 50%\n3 - 70%\n4 - 100%\n")
        opcoes_validas:list[int] = [1, 2, 3, 4]
        dose = self._validarInput(input_, opcoes_validas)
        if dose == ValueError:
            return ValueError
        dose_map = {1: 3, 2: 5, 3: 7, 4: 10}
        return Doses(dose_map[dose])

    def verificarNomeBebidaLata(self) -> str:
        input_ = input("\nDigite o nome da bebida lata. Pressione Enter para " 
        "sair.\n")
        return input_.strip().capitalize()
    
    def verificarQuantidadeBebidaLata(self) -> int | ValueError:
        input_ = input("\nDigite a quantidade de bebida desejada.\n")
        try:
            quantidade = int(input_)
        except:
            return ValueError
        if quantidade < 0: 
            return ValueError
        return quantidade
    
    def opcoesFinalizarCompra(self) -> int | ValueError:
        input_ = input("\nEscolha uma forma de pagamento:\n1 - Pix\n2 - Débito\n"
                       + "3 - Crédito\n4 - Retornar à tela inicial\n")
        opcoes_validas:list[int] = [1, 2, 3, 4]
        return self._validarInput(input_, opcoes_validas)

    def finalizarCompra(self, forma_pagamento:int) -> None:
        if forma_pagamento == 1:
            input("\nRealize a transferência e pressione Enter para confirmar o pagamento.\n")

        if forma_pagamento == 2:
            input("\nInsira o cartão de débito e pressione Enter para confirmar o pagamento.\n")

        if forma_pagamento == 3:
            input("\nInsira o cartão de crédito e pressione Enter para confirmar o pagamento.\n")

        print("Validando pagamento", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".")
        sleep(1)
        print("Pagamento confirmado.")

    def dispensarBebidaLata(self, quantidade:int, bebida:str):
        print(f"\nDispensando {quantidade} {bebida}", end="")
        if quantidade > 1:
            print("s", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".", end="")
        sleep(1)
        print(".")
        sleep(1)
        print("\nBebida dispensada. Aproveite!")
        self.estadoEspera()

    def dispensarIngrediente(self, doses:list[int], ingredientes:list[str]):
        for index in range(len(ingredientes)):
            print(f"\nDispensando {doses[index]} g de {ingredientes[index]}", end="")
            sleep(1)
            print(".", end="")
            sleep(1)
            print(".", end="")
            sleep(1)
            print(".")
            sleep(1)

        print("\nBebida dosada dispensada. Aproveite!")
        self.estadoEspera()