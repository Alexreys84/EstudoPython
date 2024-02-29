# Nota do aluno dividido por 4

n1 = input("Digite a primeira nota do aluno:")
n2 = input("Digite a segunda nota do aluno:")
n3 = input("Digite a terceira nota do aluno:")
n4= input("Digite a quarta nota do aluno:")
rs = (int(n1)+int(n2)+int(n3)+int(n4)) /4
# Se o Aluno tiver uma media acima ou igual a 7
# entao estara APROVADO.
# Se a média do Alunon for abaixo ou igual a 4, 
# estão estara REPROVADO, caso contrário estara em
# RECUPERAÇÃO 
print("A sua Média é "+str(rs)+", então você está: ")


if(rs >= 7):
    print("APROVADO")
elif(rs <= 4):
    print("REPROVADO")
else:
    print("RECUPERAÇÃO")


