#print("Digite o local do arquivo de entrada:")
#path = input()

path = r'D:\Projetos\analisadorLexicoSecreto\entradaAva.txt'

f = open(path, 'r')
entrada = f.read()

palavrasReservadas= ['var','id','integer','real','if', 'then']
simbolos = [':',',' , ';' , ':=','+']
#operadores=['+','/','*','-']
#operadoresRelacionais=['<', '<=', '==', '!=', '>=', '>']

lentras = 'abcdefghijklmnopqrstuvwxyz'
numeros = '0123456789'

entrada = entrada.replace(' ', '')
entrada = entrada.replace('\n', '')

tamanhoEntrada= len(entrada)

tokens = []
a = 0
while a < tamanhoEntrada-1:
    print('a:',a)
    #identificadores
    token = ''
    while entrada[a] in numeros or entrada[a] in lentras and a < tamanhoEntrada-1:
        token += entrada[a]
        a += 1
    if a == tamanhoEntrada-1:
        token += entrada[a]
    if(token in palavrasReservadas):
        tokens.append([token,'palavra reservada'])
    else:
        tokens.append([token,'identificador'])
    if entrada[a] == ':' and entrada[a+1] == '=':
        token = ':='
        tokens.append([token,'atribuicao'])
        a+=2
    if entrada[a] in simbolos:
        a+=1
        token = entrada[a]
        tokens.append([token,'simbolo'])

print(tokens)
  

