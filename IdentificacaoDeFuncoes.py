def preencherInventario(lista):
    resp = 'S'
    while resp == 'S':
        equipamento = [input('Equipamentos: '),
                       float(input('Valor : ')),
                       int(input('Número serial: ')),
                       input('Departamento: ')]
        lista.append(equipamento)
        resp = input('Digite \'S\' para continuar. ').upper()


def exibirInventario(lista):
    for elemento in lista:
        print('Nome..........: ', elemento[0])
        print('Valor.........: ', elemento[1])
        print('Serial .......: ', elemento[2])
        print('Departamento..: ', elemento[3])


def localizarPorNome(lista):
    busca = input('Digite o nome do equipamento: ')
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor....: ", elemento[1])
            print("Serial...: ", elemento[2])


def depreciarPorNome(lista):
    depreciacao = input("digite o nome do equipamento que será depreciado: ")
    porc = float(input('Digite a depreciação em racional ex:10% = 0,1:'))
    for elemento in lista:
        if depreciacao == elemento[0]:
            print('Valor antigo: ', elemento[1])
            elemento[1] = elemento[1] * (1 - porc / 100)
            print('Valor novo: ', elemento[1])


def excluirPorSerial(lista):
    serial = int(input('Digite o serial do equipamento a ser excluido:  '))
    for elemento in lista:
        if serial == elemento[2]:
            lista.remove(elemento)
    return "Intens Excluidos!!!"


def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento masi caro é: ", max(valores))
        print("O equipamento mais barato é: ", min(valores))
        print("O total dos equipamentos é de: ", sum(valores))
