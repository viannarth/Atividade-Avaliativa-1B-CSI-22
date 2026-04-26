from src.constantes import TipoBebida, FormaPagamento, TipoItem
from src.estoque import Estoque
from src.item import Item, Bebida, BebidaDosada, BebidaLata
from src.carrinho import Carrinho


class MaquinaVendas():
    """!
    @brief Maquina Vendas que tem
    @param _carrinho uma instanciacao da classe Carrinho
    @param _estoque uma instanciacao da classe Estoque
    @param _vendas um dicionario que associa um tipo de bebida com sua quantidade vendida
    """
    def __init__(self) -> None:
        """!
        @brief Inicializa instanciando os objetos das classes e criando o dicionario
        """
        self._carrinho:Carrinho = Carrinho()
        self._estoque:Estoque = Estoque()
        self._vendas:dict[TipoBebida, int] = {tipo_bebida: 0 for tipo_bebida in TipoBebida}

    def consultarEstoqueLista(self) -> list[Item]:
        return self._estoque.consultarEstoqueLista()

    def consultarEstoqueItem(self, nome_item:str) -> int:
        return self._estoque.consultarEstoqueItem(nome_item)
    
    def consultarCarrinho(self) -> list[Bebida]:
        self._carrinho.consultarBebidas()

    def consultarFormaPagamento(self) -> FormaPagamento:
        return self._carrinho.consultarFormaPagamento()
    
    def consultarValorCarrinho(self) -> int:
        self._carrinho.consultarValorTotal()

    def consultarSaldo(self) -> int:
        saldo = 0
        for tipo_bebida in self._vendas:
            saldo += self._vendas[tipo_bebida]
        return saldo
    
    def consultarSaldoBebida(self, tipo_bebida:TipoBebida) -> int:
        return self._vendas[tipo_bebida]

    def checarVazio(self) -> bool:
        self._carrinho.checarVazio()

    def verificarIngrediente(self, nome_ingrediente:str) -> Item | False:
        return self._estoque.verificarItem(nome_ingrediente)
    
    def verificarBebidaLata(self, nome_bebida:str) -> BebidaLata | False:
        return self._estoque.verificarItem(nome_bebida)
    
    def estocarItem(self, tipo_item:TipoItem, nome_item:str, quantidade_estoque:int) -> None:
        self._estoque.estocarItem(tipo_item, nome_item, quantidade_estoque)

    def adicionarBebida(self, nome_bebida:str = None, num_bebidas:int = 1, bebida_dosada:BebidaDosada = None) -> None:
        self._carrinho.adicionarBebida(nome_bebida, num_bebidas, bebida_dosada)

    def removerBebida(self, nome_bebida:str = None, num_bebidas:int = 1, bebida_dosada:BebidaDosada = None) -> None:
        self._carrinho.removerBebida(nome_bebida, num_bebidas, bebida_dosada)

    def esvaziarCarrinho(self) -> None:
        self._carrinho.esvaziarCarrinho()
    
    def _atualizarVendas(self, bebida:Bebida | BebidaDosada, quantidade_vendida:int) -> None:
        """!
        @brief Aumenta a quantidade do item vendida na maquina e atualiza o estoque com os itens usados
        @param bebida A bebida a ser vendida
        @param quantidade_vendida Quantidade do item vendida
        @details Se a bebida for em lata apenas chamamos a funcao de atualizar sua quantidade no estoque. Se for uma
        bebida dosada devemos percorrer seu dicionario que contem os itens e subtrair de suas quantidades
        """
        self._vendas[bebida.consultarTipoBebida()] += bebida.consultarPreco()*quantidade_vendida
        if (bebida.consultarTipoBebida() == TipoBebida.LATA):
            self._estoque.atualizarEstoqueItem(bebida.consultarNome(), quantidade_vendida)
        else:
            ingredientes = bebida.consultarIngrediente()
            for ingrediente in ingredientes:
                self._estoque.atualizarEstoqueItem(ingrediente.consultarNome(), quantidade_vendida*ingredientes[ingrediente])

    def realizarVenda(self, forma_pagamento:FormaPagamento) -> None:
        """!
        @brief Realiza a venda do carrinho da maquina de vendas
        @param forma_pagamento Forma de pagamento
        @details atualiza a forma de pagamento e para cada bebida eu aciona atualizar vendas, eliminando ela apos isso
        e esvaziando o carrinho ao final
        """
        self._carrinho.definirFormaPagamento(forma_pagamento)
        bebidas = self._carrinho.consultarBebidas()
        for bebida in bebidas:
            self._atualizarVendas(bebida, bebidas[bebida])
            if bebida.consultarTipoBebida() == TipoBebida.LATA:
                self._carrinho.removerBebida(bebida.consultarNome(), bebidas[bebida])
            else:
                self._carrinho.removerBebida(bebida)
        self._carrinho.esvaziarCarrinho()


