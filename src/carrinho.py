from src.item import Bebida
from src.constantes import FormaPagamento

class Carrinho():
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

    def consultarBebidas(self) -> dict[Bebida]:
        """!
        Consulta a bebida da maquina
        @return retorna o dicionario de bebidas e suas reespectivas quantidades
        """
        return self._carrinho
    
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
    
    def definirFormaPagamento(self, forma_pagamento:FormaPagamento) -> None:
        """!
        Define a forma de pagamento
        @param forma_pagamento A forma de pagamento
        """
        self._forma_pagamento = forma_pagamento

    def adicionarBebida(self, bebida:Bebida, num_bebidas:int = 1) -> None:
        """!
        Adiciona bebida no carrinho
        @param bebida A bebida a ser comprada
        @param num_bebidas A quantidade de bebidas que serao compradas
        """
        if bebida in self._carrinho:
            self._carrinho[bebida] += num_bebidas
        else:
            self._carrinho[bebida] = num_bebidas
        self._valor_total += bebida.consultarPreco()*num_bebidas

    def removerBebida(self, bebida:Bebida, num_bebidas:int = 1) -> None:
        """!
        Remove bebida no carrinho
        @param bebida A bebida a ser removida
        @param num_bebidas A quantidade de bebidas a serem removidas
        """
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
