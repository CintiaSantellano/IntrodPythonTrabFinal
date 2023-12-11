# Variáveis

anos=0

altura_a = 1.85
altura_b = 1.64

idade_a = 56
idade_b = 35

taxa_crescimento_a  = 0.03
taxa_crescimento_b = 0.045

while altura_a > altura_b:
    altura_a += taxa_crescimento_a
    altura_b += taxa_crescimento_b
    anos += 1

    if idade_a >= 110 or idade_b >= 110:
        print ("Ultrapassou 110 anos")

print (f"Serão necessários {anos} para que a pessoa B alcance a pessoa A")