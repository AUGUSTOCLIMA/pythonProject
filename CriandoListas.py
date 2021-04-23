# lista preenchida estaticamente
lista_estatica = ["xpto", True]

usuario = input("Digite o usuário: ")
logado = bool(int(input("Está logado? ")))
print(usuario, logado)

# lista preenchida dinamicamente
lista_dinamica = [usuario, logado]

# lista vazia
lista_vazia = []

print(lista_dinamica, lista_estatica, lista_vazia)
