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
  #if
    if entrada[a] == 'i' and entrada[a+1] == 'f':
        print('palavra reservada: if')
        a = a + 3
    
      #identificadores
    if entrada[a] in numeros or entrada[a] in lentras:
        inicio = a
        while entrada[a] in numeros or entrada[a] in lentras:
            print(entrada[a], end ='')
            a += 1
        print(', identificador')
            
  

    a += 1

'''
qtdeElementos = len(entradaSeparada)

a=0


#printar comentarios separados por /* */ 

while a != qtdeElementos:
    if entradaSeparada[a] == 'if':
        print (entradaSeparada[a], ", palavra reservada")
    if entradaSeparada[a] == '/*':
        inicioComentario = a
        for b in range(a,qtdeElementos):
            if entradaSeparada[b] == '*/\n{\n':
                fimComentario= b+1
        
        for c in range(inicioComentario,fimComentario):
            print(entradaSeparada[c], end = '')
        print(", comentario")
        
    a += 1


'''
