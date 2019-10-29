f = open('D:\Projetos\Compiladores 1\Analisador lexico\entradaAva.txt', 'r')
entrada = f.read()

palavrasReservadas= ['if']
operadores=['+','/','*','-']
operadoresRelacionais=['<', '<=', '==', '!=', '>=', '>']
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
        
        a += 2
    
     #abre chaves
    if entrada[a] == '{':
        print(entrada[a],',  abre chaves')
        a = a + 1
   
    #fecha chave
    if entrada[a] == '}':
        print(entrada[a], ',  fecha chaves')
        a = a + 1

    #operador de atruibuição =
    if entrada[a] == '=':
        print('=, atribuição')
        a = a + 1
      
    #operadores aritiméticos  +, -, *, /
    if entrada[a] in operadores:
        print(entrada[a], ',  operador aritimético')
        a = a + 1
      
    #operadores relacionais   <, <=, ==, !=, >=, >
    if entrada[a] in operadoresRelacionais:
        print(entrada[a], ',  operador relacional')
        a = a + 1
      
    #abre parênteses
    if entrada[a] == '(':
        print(entrada[a], ',  abre parênteses')
        a = a + 1
   
    #fecha parênteses
    if entrada[a] == ')':
        print(entrada[a], ',  fecha parênteses')
        a = a + 1
    
    
    #if
    if entrada[a] == 'i' and entrada[a+1] == 'f':
        print('if, palavra reservada')
        a = a + 2
    
    #numero real
    if entrada[a] in numeros and entrada[a+1] == ".":
        print(entrada[a], end ='')
        print(entrada[a+1], end ='')
        a+=2
        while entrada[a] in numeros:
            print(entrada[a], end ='')
            a += 1
        print(', numero real')
    

    #identificadores
    if entrada[a] in numeros or entrada[a] in lentras:
        while entrada[a] in numeros or entrada[a] in lentras:
            print(entrada[a], end ='')
            a += 1
        print(', identificador')

    if entrada[a] == '\n':
        a+=1
    



    
  

