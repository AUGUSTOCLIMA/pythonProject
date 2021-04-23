equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento..: ", (indice + 1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])

busca = input('Digite o nome do equipamento que deseja buscar: ')
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print('Valor..: ', valores[indice])
        print('Serial.: ', seriais[indice])
        print('Departamento.: ', departamentos[indice])

depreciacao = input('Qual equipamento será depreciado: ')

for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print('Valor antigo : ', valores[indice])
        valores[indice] = valores[indice] * 0.9
        print('Valor novo: ', valores[indice])

serial = int(input('Digite qual serial do equimento a ser deletado: '))

for indice in range(0, len(equipamentos)):
    if seriais[indice] == serial:
        del departamentos[indice]
        del valores[indice]
        del equipamentos[indice]
        del seriais[indice]
        break

for indice in range(0, len(equipamentos)):
    print("Equipamento..: ", (indice + 1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])
