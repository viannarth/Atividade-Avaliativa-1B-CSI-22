from enum import Enum

class TipoBebida(Enum):
    LATA = 1
    DOSADA = 2


class Doses(Enum):
    TRINTA: 3
    CINQUENTA: 5
    SETENTA: 7
    CEM: 10
    AGUA: 50


class FormaPagamento(Enum):
    PIX = 1
    DEBITO = 2
    CREDITO = 3

PRECO_BEBIDA_LATA:int = 5
PRECO_BEBIDA_DOSADA:int = 10
