print("Programa que verifica se o CPF é válido")

# Variável que guarda o CPF digitado pelo usuário
cpf_usuario = input("Digite o seu CPF: ")

# Criar uma variável para guardar o CPF que estamos calculando
cpf_calc = '10'

peso10 = 10
peso11 = 11

# A variável resultado guarda a soma das multiplicações
# entre os dígitos de CPF e os pesos
resultado = 0

# Para obter os 9 primeiros dígitos do CPF, foi necessário
# usar uma estrutura for com uma contagem de 0 até 8
for i in range(9):
    # Exibindo um dígito de CPF por vez em tela
    print(cpf_usuario[i])

    # Adicionar à variável cpf_calc os nove primeiros
    # dígitos do CPF e adicionar o primeiro dígito
    # verificador mais adiante
    cpf_calc += cpf_usuario[i]

    print(int(cpf_usuario[i]) * peso10)

    # Para calcular um dígito por vez com o peso, foi
    # necessário converter cada dígito em número inteiro
    # depois, somamos os resultados obtidos armazenando
    # na variável resultado.
    resultado += int(cpf_usuario[i]) * peso10

    # Todas as vezes que o laço for rodar, será subtraído
    # o valor 1 da variável peso10
    peso10 -= 1

# Exibindo o resultado encontrado
print(resultado)

# A variável resto guarda o resto da divisão
resto = resultado % 11

# Se o resto da divisão for menor que 2, então o
# primeiro dígito será 0 (zero); Caso contrário, devemos
# subtrair 11 pelo valor encontrado em resto
if resto < 2:
    print("Primeiro dígito é 0")
    cpf_calc += "0"
else:
    print("Primeiro dígito é " + str(11 - resto))
    cpf_calc += str(11 - resto)
    resultado = 0

    # Calcular o segundo dígito verificador
    for i in range(10):
        resultado += int(cpf_calc[i]) * peso11

        resto = resultado % 11
        if resto < 2:
            cpf_calc += "0"
        else:
            cpf_calc += str(11 - resto)

# Validar se o CPF do usuário é igual ao CPF calculado
if cpf_usuario == cpf_calc:
    print("CPF é Válido")
else:
    print("CPF Inválido")
