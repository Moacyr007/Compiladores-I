f = open('D:\Projetos\Compiladores 1\Analisador lexico\entradaAva.txt', 'r')
entrada = f.read()

palavrasReservadas= ['if']
operadores=['+','/','*','-']

lentras = 'abcdefghijklmnopqrstuvwxyz'
numeros = '0123456789'

entrada = entrada.replace(' ', '')
tamanhoEntrada= len(entrada)

a = 0
while a < tamanhoEntrada-1:

    #comentario //
     
    if entrada[a] == '/' and entrada[a+1] == '/':
        while entrada[a] != "\n":
            print(entrada[a], end ='')
            a+=1
        
        print(", comentario")

    #comentario /* */
    if entrada[a] == '/' and entrada[a+1] == '*':
        print(entrada[a], end ='')
        print(entrada[a+1], end ='')
        a += 2
        while entrada[a] != '*' and entrada[a+1] != '/':
            print(entrada[a], end ='')
            a+=1
        print("*/ , comentario")
  
    #operador de atruibuição =
    if entrada[a] == '=':
        print('=, atribuição')
        a = a + 1

    #if
    if entrada[a] == 'i' and entrada[a+1] == 'f':
        print('palavra reservada: if')
        a = a + 3
    
    #identificadores
    if entrada[a] in numeros or entrada[a] in lentras:
        while entrada[a] in numeros or entrada[a] in lentras:
            print(entrada[a], end ='')
            a += 1
        print(', identificador')
        a -= 1
  

    a += 1
