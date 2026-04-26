from src.item import Bebida, BebidaDosada, BebidaLata
from src.constantes import FormaPagamento


class Carrinho:
    """!
    @brief Carrinho de compras da maquina de vendas
    @details possui como variaveis
    @param _carrinho  Um dicicionario de uma bebida e sua reespectiva quantidade
    @param _valor_total  O valor total da compra no carrinho
    @param _forma_pagamento  A forma de pagamento para a compra
    """
    def __init__(self) -> None:
        """!
        Inicializa a carrinho
        """
        self._carrinho:dict[Bebida, int] = {}
        self._valor_total:int = 0
        self._forma_pagamento:FormaPagamento = None


    def consultarBebidas(self) -> list[Bebida]:
        """!
        Consulta a bebida da maquina
        @return retorna a lista de bebidas na maquina
        """
        bebidas:list[Bebida] = [bebida for bebida in self._carrinho]
        return bebidas

    
    def consultarValorTotal(self) -> int:
        """!
        Consulta o valor total da compra
        @return retorna o valor total da compra
        """
        return self._valor_total
    
    def consultarFormaPagamento(self) -> FormaPagamento:
        return self._forma_pagamento
    
    def checarVazio(self) -> bool:
        """!
        checa se o carrinho esta vazio
        @return retorna verdadeiro se o carrinho estiver vazio
        """
        if len(self._carrinho) == 0:
            return True
        return False
    
    def verificarBebidaLata(self, nome_bebida:str) -> BebidaLata | False:
        """!
        @brief verifica se tem uma determinada bebida em lata no carrinho
        @param nome_bebida A bebida a ser verificada
        @return retorna verdadeiro se encontrou
        """
        for bebida in self._carrinho:
            if bebida.consultarTipoBebida == BebidaLata:
                if nome_bebida == bebida.consultarNome():
                    return bebida
        return False
    
    def definirFormaPagamento(self, forma_pagamento:FormaPagamento) -> None:
        """!
        Define a forma de pagamento
        @param forma_pagamento A forma de pagamento
        """
        self._forma_pagamento = forma_pagamento


    def adicionarBebida(self, nome_bebida:str = None, num_bebidas:int = 1, bebida_dosada:BebidaDosada = None) -> None:
        """!
        @brief Adiciona bebida no carrinho
        @param num_bebidas Numero de bebidas a serem adicionadas
        """
        if nome_bebida == None:
            self._carrinho[bebida_dosada] = num_bebidas
            self._valor_total += bebida_dosada.consultarPreco()*num_bebidas
        else:
            bebida = self.verificarBebidaLata(nome_bebida)
            if not bebida:
                self._carrinho[bebida] = num_bebidas
            else:
                self._carrinho[bebida] += num_bebidas
            self._valor_total += bebida.consultarPreco()*num_bebidas


    def removerBebida(self, nome_bebida:str = None, num_bebidas:int = 1, bebida_dosada:BebidaDosada = None) -> None:
        """!
        @brief Remove bebida no carrinho
        @param nome_bebida A bebida a ser removida
        @param num_bebidas A quantidade de bebidas a serem removidas
        """
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
        """!
        reinicia o carrinho para que seja utilizado novamente em uma nova compra
        Apaga a forma de pagamente, o dicionario do carrinho e coloca o valor total como zero
        """
        self._forma_pagamento = None
        self._carrinho.clear()
        self._valor_total = 0
