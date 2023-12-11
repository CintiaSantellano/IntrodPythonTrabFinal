# variaveis
# Show 1:
publico_1 = 150
ingresso_1 = 5.00
ingresso_2 = 5.50

total_faturamento = 0
lucro = 0
despesas = 0


if ingresso_1:
    despesa_1 = ingresso_1 - 0.30
    total_faturamento_1 = despesa_1 * publico_1
    lucro_1_show_1 = total_faturamento_1 * 150
    print (f"O total de faturamento do Show 1 Ingresso 1 foi {total_faturamento_1}")
    print (f"O lucro total do Show 1 Ingresso 1 foi {lucro_1_show_1}")
    print (f"Despesas gerais Show 1 Ingresso 1 foi {despesa_1}")

if ingresso_2:
    despesa_2 = ingresso_2 - 0.50
    total_faturamento_2 = despesa_2 * publico_1
    lucro_2_show_1 = total_faturamento_2 * 150
    print (f"O total do faturamento do Show 1 Ingresso 2 foi {total_faturamento_2}")
    print (f"O lucro total do Show 1 Ingresso 2 foi {lucro_2_show_1}")
    print (f"Despesas gerais Show 1 ingresso 2 foi {despesa_2}")