#variáveis para armazenar os valores máximos e mínimos
max_idade = 0
min_altura = float('inf')
nome_max_idade = ""
nome_min_altura = ""

# inicializa a variável para armazenar a soma das idades
soma_idades = 0

# loop para receber os dados das 5 pessoas
for i in range(5):
    # recebe o nome, idade e altura da pessoa i
    nome = input("Digite o nome da pessoa {}: ".format(i+1))
    idade = int(input("Digite a idade da pessoa {}: ".format(i+1)))
    altura = float(input("Digite a altura da pessoa {} em metros: ".format(i+1)))

    # verifica se a pessoa i tem a maior idade
    if idade > max_idade:
        max_idade = idade
        nome_max_idade = nome

    # verifica se a pessoa i tem a menor altura
    if altura < min_altura:
        min_altura = altura
        nome_min_altura = nome

    # adiciona a idade da pessoa i à soma das idades
    soma_idades += idade

# calcula a média das idades
media_idades = soma_idades / 5

# imprime os resultados
print("A pessoa com a maior idade é {}.".format(nome_max_idade))
print("A pessoa com a menor altura é {}.".format(nome_min_altura))
print("A média de idade das 5 pessoas é {} anos.".format(media_idades))


