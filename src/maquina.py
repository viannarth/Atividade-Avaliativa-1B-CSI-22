from src.constantes import TipoBebida, FormaPagamento
from src.estoque import Estoque
from src.item import Item, Bebida, BebidaDosada, BebidaLata
from src.carrinho import Carrinho

class MaquinaVendas(): 
    def __init__(self) -> None:
        self._carrinho:Carrinho = Carrinho()
        self._estoque:Estoque = Estoque()
        self._vendas:dict[TipoBebida, int] = {}

    def consultarEstoque(self) -> dict[Item, int]:
        return self._estoque.consultarEstoque()

    def consultarEstoqueItem(self) -> int:
        return self._estoque.consultarEstoqueItem()
    
    def estocarItem(self, item:Item, quantidade_estoque:int) -> None:
        self._estoque(item, quantidade_estoque)

    def consultarCarrinho(self) -> dict[Bebida, int]:
        self._carrinho.consultarBebidas()

    def consultarValorTotal(self) -> int:
        self._carrinho.consultarValorTotal()

    def checarVazio(self) -> bool:
        self._carrinho.checarVazio()

    def adicionarBebida(self, bebida:Bebida, num_bebidas:int = 1) -> None:
        self._carrinho.adicionarBebida(bebida, num_bebidas)

    def removerBebida(self, bebida:Bebida, num_bebidas:int = 1) -> None:
        self._carrinho.removerBebida(bebida, num_bebidas)

    def esvaziarCarrinho(self) -> None:
        self._carrinho.esvaziarCarrinho()
    
    def consultarSaldo(self) -> int:
        saldo = 0
        for tipo_bebida in self._vendas:
            saldo += self._vendas[tipo_bebida]
        return saldo
    
    def consultarSaldoBebida(self, tipo_bebida:TipoBebida) -> int:
        return self._vendas[tipo_bebida]

    def _atualizarVendas(self, bebida:Bebida, quantidade_vendida:int) -> None:
        self._vendas[bebida.consultarTipoBebida()] += bebida.consultarPreco()*quantidade_vendida
        if (bebida.consultarTipoBebida() == TipoBebida.LATA):
            self._estoque.atualizarEstoqueItem(bebida, quantidade_vendida)
        else:
            for ingrediente in bebida._bebida_dosada:
                self._estoque.atualizarEstoqueItem(ingrediente, quantidade_vendida*bebida._bebida_dosada[ingrediente])

    def realizarVenda(self, forma_pagamento:FormaPagamento) -> None:
        self._carrinho.definirFormaPagamento(forma_pagamento)
        bebidas = self._carrinho.consultarBebidas()
        for bebida in bebidas:
            self._atualizarVendas(bebida, bebidas[bebida])
            self._carrinho.removerBebida(bebida, bebidas[bebida])
        self._carrinho.esvaziarCarrinho()


