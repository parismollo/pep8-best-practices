# from fila_prioritaria import FilaPrioritaria

from fabrica_fila import FabricaFila

# fila_teste = FilaPrioritaria()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()
# fila_teste.atualiza_fila()

# print(fila_teste.chama_cliente(10))
# print(fila_teste.chama_cliente(2))
# print(fila_teste.chama_cliente(4))

# print(fila_teste.estatistica('10/01/1993', 210, 'detail'))

teste_fabrica = FabricaFila.pega_fila('normal')
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()
teste_fabrica.atualiza_fila()

print(teste_fabrica.chama_cliente(2))
