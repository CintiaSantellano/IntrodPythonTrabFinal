# Lista com as informações de idade e peso
pessoas = []

# Receba a idade e o peso de cada pessoa e adiciona à lista
for i in range(10):
    idade = int(input(f"Informe a idade da pessoa {i+1}: "))
    peso = float(input(f"Informe o peso da pessoa {i+1}: "))
    pessoas.append((idade, peso))

# Calcula a média de peso das pessoas menores de idade
soma_peso_menores = 0
num_menores = 0
for idade, peso in pessoas:
    if idade < 18:
        soma_peso_menores += peso
        num_menores += 1
if num_menores > 0:
    media_peso_menores = soma_peso_menores / num_menores
else:
    media_peso_menores = 0

# Média de peso das pessoas maiores de idade
soma_peso_maiores = 0
num_maiores = 0
for idade, peso in pessoas:
    if idade >= 18:
        soma_peso_maiores += peso
        num_maiores += 1
if num_maiores > 0:
    media_peso_maiores = soma_peso_maiores / num_maiores
else:
    media_peso_maiores = 0

# Comparar as médias de peso e informar qual é maior
if media_peso_menores > media_peso_maiores:
    print("A média de peso é maior entre as pessoas menores de idade.")
elif media_peso_maiores > media_peso_menores:
    print("A média de peso é maior entre as pessoas maiores de idade.")
else:
    print("As médias de peso das pessoas menores e maiores de idade são iguais.")
