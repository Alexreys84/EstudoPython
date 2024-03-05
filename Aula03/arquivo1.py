#Open é uma função q permite abrir um arquivo 
#ler ou escrever neste arquivo
arq = open("dados.txt","a")
#A função write, permite escrever em um arquivo 
arq.write("Olá\n")
#A função close fecha o arquivo retirando-o da
#memória
arq.close()
