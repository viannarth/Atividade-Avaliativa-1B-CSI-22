from abc import ABC, abstractmethod

# TODO: implement __str__ method in Item, Bebida and Estoque

class GerenciadorTelas():
    def __init__(self) -> None:
        self._tela_atual:Tela = TelaInicial(self)

    def alterarTela(self, proxima_tela:Tela) -> None:
        self._tela_atual = proxima_tela

    def limparTela(self) -> None:
        pass

    def exibirTela(self) -> None:
        self.limparTela()
        self._tela_atual.gerenciarInput()


class Tela(ABC):
    def __init__(self, gerenciador_telas:GerenciadorTelas) -> None:
        self._gerenciador = gerenciador_telas

    @abstractmethod
    def gerenciarInput(self) -> None:
        pass


class TelaInicial(Tela):
    def __init__(self, gerenciador_telas:GerenciadorTelas) -> None:
        super().__init__(gerenciador_telas)

    def mensagemInicial(self) -> str:
        pass

    def gerenciarInput(self) -> None:
        pass