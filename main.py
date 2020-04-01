

from fabrica_fila import FabricaFila
# from estatistica_detalhada import EstatisticaDetalhada
from estatistica_resumida import EstatisticaResumida


teste_fabrica = FabricaFila.pega_fila('prioritaria')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()

print(teste_fabrica.chama_cliente(2))
print(teste_fabrica.chama_cliente(10))
print(teste_fabrica.estatistica(EstatisticaResumida('17/02/1999', 10)))
print(teste_fabrica.clientes_atendidos)
teste_fabrica.apaga_dados('secret_key')
print(teste_fabrica.clientes_atendidos)
