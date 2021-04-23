def perguntar():
    resposta = input("O que deseja realizar?\n" +
                     "<I> - Para Inserir um Usuário\n" +
                     "<P> - Para Pesquisar um usuário\n" +
                     "<E> - Para Excluir um usuário\n" +
                     "<L> - Para Listar um usuário\n" +
                     "<V> - Para Value:").upper()
    return resposta


def inserir(dicionario):
    dicionario[input("Código do lançamento \"Código Unico \": ")] = [input("Digite o Nome: ").upper(),
                                                                     input("Qual nível do úsuario: "),
                                                                     input("Qual o Login: "),
                                                                     input("Digite a última data de acesso: ").upper(),
                                                                     input("Qual a útilma estação acessada: ").upper(),
                                                                     input("Digite a Hora do Login: ")]


def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print("Nome......................:" + lista[0])
        print("Nível Úsuario.............:" + lista[1])
        print("Último acesso.............:" + lista[2])
        print("Login.....................:" + lista[3])
        print("Última estação acessada...:" + lista[4])
        print("Hora do Login.............:" + lista[5])


def excluir(dicionario, chave):
    if dicionario.get(chave) is not None:
        del dicionario[chave]
    print("Objeto Eliminado")


def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)


def valorDaLista(dicionario):
    for valor in dicionario.values():
        print("Valores....")
        print(valor)