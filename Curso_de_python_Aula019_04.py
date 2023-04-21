estado = {}
brasil = []
for i in range (0,3):
    estado['UF'] = str(input('Digite A Unidade Federativa: '))
    estado['Sigla'] = str(input('Digite A Sigla: '))
    brasil.append(estado.copy())
print(brasil)