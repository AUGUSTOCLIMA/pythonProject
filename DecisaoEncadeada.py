nome = input("digite seu nome:")
idade = int(input("digite sua idade: "))
doenca_infecto = input(" Suspeita de doença infectocontagiosa?").upper()

if idade >= 65:
    print("Paciente com prioridade!")
    if doenca_infecto == "SIM":
        print("encaminhe para sala amerela!")
    elif doenca_infecto == "NAO":
        print("Encaminhe para sala Branca!")
else:
    print("Paciente sem prioridade!")
    if doenca_infecto == "SIM":
        print("Encaminhe para sala amarela")
    elif doenca_infecto == "NAO":
        print("Encaminhe para sala Branca!")
    else:
        print("Responda o questionario!!!")
