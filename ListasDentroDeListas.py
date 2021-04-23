inventario = []
resposta = 'S'

while resposta == 'S':
    equipamento = [input('Equipamento: '),
                   float(input('Valor: ')),
                   int(input('Número serial: ')),
                   input('Departamento; ')]
    inventario.append(equipamento)
    resposta = input('Digite \'S\' para continuar: ').upper()

for elemento in inventario:
    print('nome.........: ', elemento[0])
    print('Valor........: ', elemento[1])
    print('Número.......: ', elemento[2])
    print('Departamento.: ', elemento[3])

busca = input('Digite o nome do equipamento a ser buscado:  ')
for elemento in inventario:
    if busca == elemento[0]:
        print('Valor...:', elemento[1])
        print('Serial...:', elemento[2])

depreciacao = input(' Digite qual equipamento será depreciado')
for elemento in inventario:
    if depreciacao == elemento[0]:
        print('Valor antigo; ', elemento[1])
        elemento[1] = elemento[1] * 0.9
        print('Valor Novo: ', elemento[1])

serial = int(input('Digite qual serial do eqquipamento a ser deletado: '))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

for elemento in inventario:
    print('nome.........: ', elemento[0])
    print('Valor........: ', elemento[1])
    print('Número.......: ', elemento[2])
    print('Departamento.: ', elemento[3])

valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print('O equipamento mais caro custa: ', max(valores))
    print('O equipamento mais barato custa: ', min(valores))
    print('O  total de equipamentos é de: ', sum(valores))
