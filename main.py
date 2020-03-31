from fila_prioritaria import FilaPrioriatia

fila_teste = FilaPrioriatia()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()

print(fila_teste.chama_cliente(10))
print(fila_teste.chama_cliente(2))
print(fila_teste.chama_cliente(4))

print(fila_teste.estatistica('10/01/1993', 210, 'detail'))
