from src.constantes import TipoItem
from src.item import BebidaLata, Ingrediente
from src.gerenciador import GerenciadorMaquina
from src.maquina import MaquinaVendas

agua = Ingrediente("Agua")
cafe = Ingrediente("Cafe")
leite = Ingrediente("Leite")
acucar = Ingrediente("Acucar")
coca = BebidaLata("Coca")
fanta = BebidaLata("Fanta")
guarana = BebidaLata("Guarana")
maquina = MaquinaVendas()
maquina.estocarItem(TipoItem.INGREDIENTE, agua.consultarNome(), 10000)
maquina.estocarItem(TipoItem.INGREDIENTE, cafe.consultarNome(), 10000)
maquina.estocarItem(TipoItem.INGREDIENTE, leite.consultarNome(), 10000)
maquina.estocarItem(TipoItem.INGREDIENTE, acucar.consultarNome(), 10000)
maquina.estocarItem(TipoItem.LATA, coca.consultarNome(), 100)
maquina.estocarItem(TipoItem.LATA, fanta.consultarNome(), 100)
maquina.estocarItem(TipoItem.LATA, guarana.consultarNome(), 100)
gerenciador = GerenciadorMaquina(maquina)

while(True):
    gerenciador.executarEstado()
