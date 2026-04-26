from enum import Enum

class TipoBebida(Enum):
    """!
    @brief Atribui a LATA e DOSADA valores para que se consiga usa-las como tipos
    @param PRECO_BEBIDA_LATA Define o o preco da bebida em lata
    @param PRECO_BEBIDA_DOSADA Define o o preco da bebida dosada
    """
    LATA = 1
    DOSADA = 2


class Doses(Enum):
    """!
    @brief Define os valores de cada dose
    @details O valor de TRINTA (que se refere a trinta por cento) vale 0.3 * 10 g , entao vale 3 g.
    CINQUENTA (que se refere a cinquenta por cento) vale 0.3 * 10  = 5  e assim em diante
    """
    TRINTA: 3
    CINQUENTA: 5
    SETENTA: 7
    CEM: 10


class FormaPagamento(Enum):
    """!
    @brief Atribui a PIX, DEBITO e CREDITO valores para que se consiga usa-las como tipos
    """
    PIX = 1
    DEBITO = 2
    CREDITO = 3

PRECO_BEBIDA_LATA:int = 5
PRECO_BEBIDA_DOSADA:int = 10
