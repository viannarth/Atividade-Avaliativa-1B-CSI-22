from padrao import TipoBebida
from estoque import Item, Bebida, BebidaDosada, BebidaLata, Ingrediente
from carrinho import Carrinho

class MaquinaVendas(): 
    def __init__(self) -> None:
        self.__estoque:dict[Item, int] = {}
        self.__vendas:dict[Bebida, int] = {}
        self.__saldo:float = 0

    def consultarSaldo(self) -> float:
        return self.__saldo

    def consultarEstoque(self) -> dict[Item, int]:
        return self.__estoque

    def consultarEstoqueItem(self, item:Item) -> int:
        return self.__estoque[item]

    def consultarValorTotal(self) -> float:
        pass

    def consultarValorBebida(self, tipo_bebida:TipoBebida) -> float:
        if tipo_bebida == BebidaLata.TipoBebida:
            return BebidaLata.consultarPreco()
        return BebidaDosada.consultarPreco()

    def atualizarSaldo(self, bebida:Bebida, quantidade_vendida:int) -> None:
        self.__saldo = self.__saldo + bebida.consultarPreco()*quantidade_vendida

    def atualizarVendas(self, bebida:Bebida, quantidade_vendida:int) -> None:
        pass

    def estocarItem(self, item:Item, quantidade_estoque:int) -> None:
        pass

    def realizarVenda(self, carrinho:Carrinho, bebida:Bebida, quantidade_vendida:int = 1) -> None:
        pass