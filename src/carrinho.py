from src.estoque import Bebida
from src.constantes import FormaPagamento

class Carrinho():
    def __init__(self) -> None:
        self.__carrinho:list[Bebida] = []
        self.__valor_total:float = 0
        self.__forma_pagamento:FormaPagamento = None

    def consultarBebidas(self) -> list[Bebida]:
        return self.__carrinho
    
    def consultarValorTotal(self) -> float:
        return self.__valor_total

    def definirFormaPagamento(self, forma_pagamento:FormaPagamento) -> None:
        self.__forma_pagamento = forma_pagamento

    def adicionarBebida(self, bebida:Bebida, num_bebidas:int = 1) -> None:
        if bebida in self.__carrinho:
            self.__carrinho[bebida] += num_bebidas
        else:
            self.__carrinho.append(bebida)
            self.__carrinho[bebida] = num_bebidas
        self.__valor_total += bebida.consultarPreco()*num_bebidas

    def removerBebida(self, bebida:Bebida, num_bebidas:int = 1) -> None:
        self.__carrinho[bebida] -= num_bebidas
        if self.__carrinho[bebida] == 0:
            self.__carrinho.remove(bebida)
        self.__valor_total -= bebida.consultarPreco()*num_bebidas

    def esvaziarCarrinho(self) -> None:
        for item in self.__carrinho:
            self.__carrinho.remove(item)
        self.__valor_total = 0
