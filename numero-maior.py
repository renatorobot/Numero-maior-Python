
verificador = 0

for c in range(5):

    numeros = int(input("Digite um numero: "))

    if numeros > verificador:

        verificador = numeros

print(f'O numero maior digitado foi: {verificador}')