from src.item import Bebida, BebidaDosada, BebidaLata
from src.constantes import FormaPagamento

class Carrinho:
    def __init__(self) -> None:
        self._carrinho:dict[Bebida, int] = {}
        self._valor_total:int = 0
        self._forma_pagamento:FormaPagamento = None

    def consultarBebidas(self) -> list[Bebida]:
        bebidas:list[Bebida] = [bebida for bebida in self._carrinho]
        return bebidas
    
    def consultarItem(self, bebida:Bebida) -> int:
        return self._carrinho[bebida]
    
    def consultarValorTotal(self) -> int:
        return self._valor_total
    
    def consultarFormaPagamento(self) -> FormaPagamento:
        return self._forma_pagamento
    
    def checarVazio(self) -> bool:
        if len(self._carrinho) == 0:
            return True
        return False
    
    def verificarBebidaLata(self, nome_bebida:str) -> BebidaLata | False:
        for bebida in self._carrinho:
            if bebida.consultarTipoBebida == BebidaLata:
                if nome_bebida == bebida.consultarNome():
                    return bebida
        return False
    
    def definirFormaPagamento(self, forma_pagamento:FormaPagamento) -> None:
        self._forma_pagamento = forma_pagamento

    def adicionarBebida(self, nome_bebida:str = None, num_bebidas:int = 1, bebida_dosada:BebidaDosada = None) -> None:
        if nome_bebida == None:
            self._carrinho[bebida_dosada] = num_bebidas
            self._valor_total += bebida_dosada.consultarPreco()*num_bebidas
        else:
            bebida = self.verificarBebidaLata(nome_bebida)
            if not bebida:
                bebida = BebidaLata(nome_bebida)
                self._carrinho[bebida] = num_bebidas
            else:
                self._carrinho[bebida] += num_bebidas
            self._valor_total += bebida.consultarPreco()*num_bebidas

    def removerBebida(self, nome_bebida:str = None, num_bebidas:int = 1, bebida_dosada:BebidaDosada = None) -> None:
        if nome_bebida == None:
            self._carrinho.pop(bebida_dosada)
            self._valor_total -= bebida_dosada.consultarPreco()*num_bebidas
        else:
            bebida = self.verificarBebidaLata(nome_bebida)
            self._carrinho[bebida] -= num_bebidas
            if self._carrinho[bebida] == 0:
                self._carrinho.pop(bebida)
            self._valor_total -= bebida.consultarPreco()*num_bebidas

    def esvaziarCarrinho(self) -> None:
        self._forma_pagamento = None
        self._carrinho.clear()
        self._valor_total = 0
