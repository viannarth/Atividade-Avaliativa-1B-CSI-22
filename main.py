from src.constantes import TipoItem
from src.item import BebidaLata, Ingrediente
from src.gerenciador import GerenciadorMaquina
from src.maquina import MaquinaVendas

agua = Ingrediente("Agua")
coca = BebidaLata("Coca")
maquina = MaquinaVendas()
maquina.estocarItem(TipoItem.INGREDIENTE, agua.consultarNome(), 10000)
maquina.estocarItem(TipoItem.LATA, coca.consultarNome(), 100)
gerenciador = GerenciadorMaquina(maquina)

while(True):
    gerenciador.executarEstado()
