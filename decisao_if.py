nome = input("digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 65:
    print("O paciente", nome, "possui etendimento prioritário!").upper()
else:
    print("O paciente", nome, "não possui atendimento proritário")
