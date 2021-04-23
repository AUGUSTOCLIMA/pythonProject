nome = input("Digite o nome: ")
idade = int(input("digite a idade: "))
doenca_infecto = input("Suspeita de donça infectocontagiosa? ").upper()

# PRIMEIRO PROBLEMA A SER RESOLVIDO

if doenca_infecto == "SIM":
    print("Encaminhe para sala amerela!")
elif doenca_infecto == "NAO":
    print("Encaminhe para sala Branca!!")
else:
    print("Responda o questionario!!!!")

# SEGUNDO PROBLEMA A SER RESOLVIDO

if idade >= 65:
    print("Paciente com proiridade!")
else:
    genero = input("digite o gênero do paciente: ").upper()
    if genero == "FEMININO" and idade > 10:
        gravidez = input("A paciente está grávida? ").upper()
        if gravidez == "SIM":
            print("Paciente com prioridade")
        else:
            print("Paciente sem proridade")
    else:
        print("Paciente sem prioridade")
