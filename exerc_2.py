# variaveis:

valor_faturamento =  0
lucro_faturamento = 0.32
imposto_total = 0

valor_faturamento = float (input (f"Digite o valor do faturamento: "))

if valor_faturamento < 5.000:
    imposto_faturamento = (valor_faturamento * 12)/100
elif valor_faturamento == 5.000 < 15.000:
    imposto_faturamento = (valor_faturamento * 18)/100
elif valor_faturamento <= 15.000:
    imposto_faturamento = (valor_faturamento * 30)/100

lucro_faturamento = valor_faturamento * 0.32
print (f"O lucro total é {lucro_faturamento}")

print (f"O valor do imposto cobrado é {imposto_faturamento}")

imposto_total = valor_faturamento - imposto_faturamento
print (f"O valor total restante é {imposto_total}")

