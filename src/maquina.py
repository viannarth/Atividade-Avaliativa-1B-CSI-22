from src.constantes import TipoBebida, FormaPagamento, TipoItem, Doses, PRECO_BEBIDA_LATA, PRECO_BEBIDA_DOSADA
from src.estoque import Estoque, Ingrediente
from src.item import Item, Bebida, BebidaDosada, BebidaLata
from src.carrinho import Carrinho

class MaquinaVendas: 
    def __init__(self) -> None:
        self._carrinho:Carrinho = Carrinho()
        self._estoque:Estoque = Estoque()
        self._vendas:dict[TipoBebida, int] = {tipo_bebida: 0 for tipo_bebida in TipoBebida}

    def consultarEstoqueLista(self) -> list[Item]:
        return self._estoque.consultarEstoqueLista()

    def consultarEstoqueItem(self, nome_item:str, tipo_item:TipoItem) -> int:
        return self._estoque.consultarEstoqueItem(nome_item, tipo_item)
    
    def consultarItemCarrinho(self, nome_bebida:str) -> int:
        return self._carrinho.consultarItem(nome_bebida)
    
    def consultarCarrinho(self) -> list[Bebida]:
        return self._carrinho.consultarBebidas()

    def consultarFormaPagamento(self) -> FormaPagamento:
        return self._carrinho.consultarFormaPagamento()
    
    def consultarValorCarrinho(self) -> int:
        return self._carrinho.consultarValorTotal()

    def consultarSaldo(self) -> int:
        saldo = 0
        for tipo_bebida in self._vendas:
            saldo += self._vendas[tipo_bebida]
        return saldo
    
    def consultarSaldoBebida(self, tipo_bebida:TipoBebida) -> int:
        return self._vendas[tipo_bebida]

    def checarVazio(self) -> bool:
        return self._carrinho.checarVazio()

    def verificarIngrediente(self, nome_ingrediente:str) -> Item | False:
        return self._estoque.verificarItem(nome_ingrediente, TipoItem.INGREDIENTE)
    
    def verificarBebidaLata(self, nome_bebida:str) -> BebidaLata | False:
        return self._estoque.verificarItem(nome_bebida, TipoItem.LATA)
    
    def estocarItem(self, tipo_item:TipoItem, nome_item:str, quantidade_estoque:int) -> None:
        self._estoque.estocarItem(tipo_item, nome_item, quantidade_estoque)

    def criarBebidaDosada(self, dict_dosada:dict[Ingrediente, Doses]) -> BebidaDosada:
        agua:Ingrediente = self._estoque.verificarItem("Agua", TipoItem.INGREDIENTE)
        bebida_dosada:BebidaDosada = BebidaDosada(agua)
        for ingrediente, dose in dict_dosada.items():
            bebida_dosada.adicionarIngrediente(ingrediente, dose)
        return bebida_dosada

    def adicionarBebida(self, nome_bebida:str = None, num_bebidas:int = 1, bebida_dosada:BebidaDosada = None) -> None:
        self._carrinho.adicionarBebida(nome_bebida, num_bebidas, bebida_dosada)

    def removerBebida(self, nome_bebida:str = None, num_bebidas:int = 1, bebida_dosada:BebidaDosada = None) -> None:
        self._carrinho.removerBebida(nome_bebida, num_bebidas, bebida_dosada)

    def esvaziarCarrinho(self) -> None:
        self._carrinho.esvaziarCarrinho()
    
    def _atualizarVendas(self, quantidade_vendida:int, bebida_dosada: BebidaDosada = None, nome_bebida:str = None) -> None:
        if nome_bebida == None:
            ingredientes = bebida_dosada.consultarIngredientes()
            for ingrediente in ingredientes:
                self._estoque.atualizarEstoqueItem(TipoItem.INGREDIENTE, ingrediente.consultarNome(), quantidade_vendida*ingredientes[ingrediente].value)
            self._vendas[TipoBebida.DOSADA] += PRECO_BEBIDA_DOSADA*quantidade_vendida
        else: 
            self._estoque.atualizarEstoqueItem(TipoItem.LATA, nome_bebida, quantidade_vendida)
            self._vendas[TipoBebida.LATA] += PRECO_BEBIDA_LATA*quantidade_vendida

    def realizarVenda(self, forma_pagamento:FormaPagamento) -> None:
        self._carrinho.definirFormaPagamento(forma_pagamento)
        bebidas = self._carrinho.consultarBebidas()
        for bebida in bebidas:
            if bebida.consultarTipoBebida() == TipoBebida.LATA:
                quantidade = self._carrinho.consultarItem(bebida.consultarNome())
                self._carrinho.removerBebida(nome_bebida=bebida.consultarNome(), num_bebidas=quantidade)
                self._atualizarVendas(quantidade_vendida=quantidade, nome_bebida=bebida.consultarNome())
            else:
                self._carrinho.removerBebida(bebida_dosada=bebida)
                self._atualizarVendas(quantidade_vendida=1, bebida_dosada=bebida)
        self._carrinho.esvaziarCarrinho()


