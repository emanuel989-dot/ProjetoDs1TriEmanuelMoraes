nota1 = input('digite um número: ')
nota1 = int(nota1)
nota2 = int (input('Digite um número: '))

def media():
    resultado = nota1 + nota2
    resultado = resultado / 2
    print(resultado)

    if resultado >= 7:
         print("aprovado")
    else:
        print("reprovado")

media()