equipamentos = []
valores = []
seriais = []
departamantos = []
resposta = 'S'

while resposta == 'S':
    equipamentos.append(input('Equipamentos: '))
    valores.append(float(input('Valores: ')))
    seriais.append(int(input('serial: ')))
    departamantos.append(input('Departamento: '))
    resposta = input('Digite \"S\" para continuar.').upper()
for equipamento in equipamentos:
    print('Equipamentos: ', equipamento)
for valor in valores:
    print('Valor: ', valor)
for serial in seriais:
    print('Serial: ', serial)
for departamanto in departamantos:
    print("Departamento: ", departamanto)
