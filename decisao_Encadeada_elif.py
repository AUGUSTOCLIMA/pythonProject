nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
doenca_infectocontagiosa = input("Suspeita de doençao infecto-contagiosa?").upper()

if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para sala amarela!")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente será direcionado para sala amarela!")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala Braca!")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente será direcionado para sala Branca!")

else:
    print("Responda a suspeita de doença infecocontagiosa!")
