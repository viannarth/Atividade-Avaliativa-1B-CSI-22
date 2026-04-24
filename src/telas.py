from abc import ABC, abstractmethod
from src.maquina import MaquinaVendas

# TODO: implement __str__ method in Item and Bebida

class GerenciadorTelas():
    def __init__(self, maquina:MaquinaVendas) -> None:
        self._maquina:MaquinaVendas = maquina
        self._tela_atual:Tela = TelaInicial()

    def alterarTela(self, proxima_tela:Tela) -> None:
        self._tela_atual = proxima_tela

    def limparTela(self) -> None:
        pass

    def exibirTela(self) -> None:
        self.limparTela()
        self._tela_atual.mensagemTerminal()

class Tela(ABC):
    def __init__(self, gerenciador_telas:GerenciadorTelas) -> None:
        self._gerenciador = gerenciador_telas    

    @abstractmethod
    def interagirUsuario(self) -> None:
        pass

class TelaInicial(Tela):
    def __init__(self, gerenciador_telas:GerenciadorTelas) -> None:
        super().__init__(gerenciador_telas)

    def interagirUsuario(self) -> None:
        pass

