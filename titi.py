# ----------------------------------------
# EXERCÍCIO 1 – Idade e entrada permitida
# ----------------------------------------

print("\nEXERCÍCIO 1 - Idade e Entrada Permitida")
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento
print(f"Idade: {idade}")

if idade >= 18:
    nome = input("Digite seu nome: ")
    print(f"{nome}, sua entrada foi permitida.")
else:
    print("Entrada não permitida para menores de 18 anos.")

# ----------------------------------------
# EXERCÍCIO 2 – Peso ideal
# ----------------------------------------

print("\nEXERCÍCIO 2 - Cálculo de Peso Ideal")
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
sexo = int(input("Digite seu sexo (1 para feminino, 2 para masculino): "))

if sexo == 1:
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Peso ideal (feminino): {peso_ideal:.2f} kg")
elif sexo == 2:
    peso_ideal = (72.7 * altura) - 58
    print(f"Peso ideal (masculino): {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Use 1 para feminino ou 2 para masculino.")

# ----------------------------------------
# EXERCÍCIO 3 e 4 – Polígonos e suas áreas
# ----------------------------------------

import math

print("\nEXERCÍCIO 3 e 4 - Tipos de Polígonos")
lados = int(input("Digite o número de lados do polígono regular: "))
medida = float(input("Digite a medida do lado (em cm): "))

if lados < 3:
    print("NÃO É UM POLÍGONO")
elif lados == 3:
    area = (medida ** 2 * math.sqrt(3)) / 4
    print("TRIÂNGULO")
    print(f"Área: {area:.2f} cm²")
elif lados == 4:
    area = medida ** 2
    print("QUADRADO")
    print(f"Área: {area:.2f} cm²")
elif lados == 5:
    print("PENTÁGONO (cálculo da área não especificado)")
else:
    print("POLÍGONO NÃO IDENTIFICADO")

# ----------------------------------------
# EXERCÍCIO 5 – Média de números positivos
# ----------------------------------------

print("\nEXERCÍCIO 5 - Média de Números Reais Maiores que Zero")
soma = 0
contador = 0

while True:
    numero = float(input("Digite um número real (0 para encerrar): "))
    if numero == 0:
        break
    elif numero > 0:
        soma += numero
        contador += 1
    else:
        print("Digite apenas números positivos.")

if contador > 0:
    media = soma / contador
    print(f"Você digitou {contador} números.")
    print(f"A média é: {media:.2f}")
else:
    print("Nenhum número válido foi digitado.")
