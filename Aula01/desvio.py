# Pede um número e verifica se e Par ou Impar
numero = input("Digite um número")
numero = int(numero)
# É necessário realizar a conversão de texto para 
# Número, pois a função input sempre retorna o valor 
# em formato texto, Então, utilizamos a função
# int para converter a variável numero em valor
# numérico inteiro e assim realizar os cálculos 
# necessário. 
if(numero % 2 == 0):
    print("O número digitado e Par")
else:
    print("O número Digitado e Impar")
