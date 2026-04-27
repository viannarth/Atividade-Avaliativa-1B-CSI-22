from enum import Enum

class TipoItem(Enum):
    INGREDIENTE = 1
    LATA = 2


class TipoBebida(Enum):
    LATA = 1
    DOSADA = 2


class Doses(Enum):
    TRINTA = 3
    CINQUENTA = 5
    SETENTA = 7
    CEM = 10
    AGUA = 50


class FormaPagamento(Enum):
    PIX = 1
    DEBITO = 2
    CREDITO = 3

PRECO_BEBIDA_LATA:float = 5.0
PRECO_BEBIDA_DOSADA:float = 10.0
SENHA_ACESSO_RESTRITO:str = "1000000390"