print("Este Programa analisa os valores")
digito = input("Entre com o número de 0 a 6")
 
 
match digito:
    case '0' | '10':
        print("Domingo")
    case '1':
        print("Segunda-feira")
    case '2':
        print("Terça-feira")
    case '3':
        print("Quarta-feira")
    case '4':
        print("Quinta-feira")
    case '5':
        print("Sexta-feira")
    case '6':
        print("Sábado")
    case _:
        print("Valor incorreto. Tente outra vez")