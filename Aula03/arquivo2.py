nome_arquivo = input("Digte o nome do arquivo:")
extensao_arquivo = input("Digite a extensao do arquivo:")
conteudo = input("Digite o conteúdo do arquivo:")

arq = open(nome_arquivo+"."+extensao_arquivo,"a")
arq.write(conteudo)
arq.close