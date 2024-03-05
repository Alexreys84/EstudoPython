def criarArquivoTabuada():
    numero = input("Digite um número para a tabuada: ")

    if not numero.isdigit():
        print("Por favor, insira um número válido.")
        return

    numero = int(numero)
    nome_arquivo = f"tabuada_{numero}.txt"

    with open(nome_arquivo, "w") as arquivo:
        for i in range(1, 11):
            resultado = numero * i
            linha = f"{numero} x {i} = {resultado}\n"
            arquivo.write(linha)

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")

# Exemplo: Solicitar ao usuário que insira o número para a tabuada
criarArquivoTabuada()
