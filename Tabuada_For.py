numero = int(input("Digite um número :"))
intervalo = int(input("Digite até que numero vai tabuada:\t"))
comeco = int(input("Qual numero começar tabuada:\t"))
passo = int(input("Digite o passo da tabuada:\t"))

while passo < 1:
    print("Digite numero maior que 0")
    passo = int(input("Digite o passo da tabuada:\t"))

print("Tabuada valor", numero, passo)
# Saída da tabuada

for valor in range(comeco, intervalo, passo):
    print(numero, "X", valor, "=", numero * valor)

    # saída somente do multiplicação

for valor in range(0, 11, 1):
    valor = valor * numero
    print(valor)
print("fim")
