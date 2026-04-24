from src.estoque import Bebida
from src.constantes import FormaPagamento

class Carrinho():
    def __init__(self) -> None:
        self._carrinho:list[Bebida] = []
        self._valor_total:float = 0.0
        self._forma_pagamento:FormaPagamento = None

    def consultarBebidas(self) -> list[Bebida]:
        return self._carrinho
    
    def consultarValorTotal(self) -> float:
        return self._valor_total
    
    def checarVazio(self) -> bool:
        if len(self._carrinho) == 0:
            return True
        return False

    def definirFormaPagamento(self, forma_pagamento:FormaPagamento) -> None:
        self._forma_pagamento = forma_pagamento

    def adicionarBebida(self, bebida:Bebida, num_bebidas:int = 1) -> None:
        if bebida in self._carrinho:
            self._carrinho[bebida] += num_bebidas
        else:
            self._carrinho.append(bebida)
            self._carrinho[bebida] = num_bebidas
        self._valor_total += bebida.consultarPreco()*num_bebidas

    def removerBebida(self, bebida:Bebida, num_bebidas:int = 1) -> None:
        self._carrinho[bebida] -= num_bebidas
        if self._carrinho[bebida] == 0:
            self._carrinho.remove(bebida)
        self._valor_total -= bebida.consultarPreco()*num_bebidas

    def esvaziarCarrinho(self) -> None:
        self._forma_pagamento = None
        self._carrinho.clear()
        self._valor_total = 0
