#print("Digite o local do arquivo de entrada:")
#path = input()

path = r'D:\Projetos\analisadorLexicoSecreto\entradaAva.txt'

f = open(path, 'r')
entrada = f.read()


diconario = {
  "var" : "declaracao",
  "integer": "tipo",
  "real": "tipo",
  "if": "condicional",
  "then": "acao condicional",
  "+":"soma",
  ":": "dois pontos",
  ",": "virgula",
  ";": "pronto e virgula",
  ":=": "atribuicao"
}
simbolos = [':',',' , ';' , ':=','+']
lentras = 'abcdefghijklmnopqrstuvwxyz'
numeros = '0123456789'
espacoEQuebraDeLinha= [' ', '\n']

tamanhoEntrada= len(entrada)
finalEntrada = tamanhoEntrada-1
tokens = []
a = 0
while a < tamanhoEntrada-1:
    
    if entrada[a] == ':' and entrada[a+1] == '=':
        token = ':='
        tokens.append([token, diconario[token]])
        a+=2
    token = ''
    
    while entrada[a] in numeros or entrada[a] in lentras and a < finalEntrada:
        token += entrada[a]
        a += 1
    if a == finalEntrada:
        token += entrada[a]
    if(token in diconario):
        tokens.append([token, diconario[token]])
    elif(token != ''):
        tokens.append([token, "identificador"])
    
    if(entrada[a] in diconario):
        token = entrada[a]
        tokens.append([token, diconario[token]])
        a += 1

    if entrada[a]in espacoEQuebraDeLinha and a < finalEntrada:
        a+=1
    if (entrada[a] not in simbolos and entrada[a] not in lentras  and entrada[a] not in numeros) and entrada[a] not in espacoEQuebraDeLinha:
        raise ValueError('Erro em:', entrada[a])


for x in tokens:
    print(x[0], "|", x[1] )
