def analisadorLexico(entrada):
    dicionario = {
    "var" : "declaracao",
    "integer": "tipoInteger",
    "real": "tipoReal",
    "if": "condicional",
    "then": "acao condicional",
    "+":"soma",
    ",": "virgula",
    ";": "ponto e virgula",
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
    linha = 0
    while a < tamanhoEntrada:
        
        if entrada[a] == ':' and entrada[a+1] == '=':
            token = ':='
            tokens.append([token, dicionario[token]])
            a+=2
        token = ''

        if entrada[a] == ':' and entrada[a+1] != '=':
            token = ':'
            tokens.append([token, "dois pontos"])
            a+=1
            token = ''
        
        while entrada[a] in numeros or entrada[a] in lentras and a < finalEntrada:
            token += entrada[a]
            a += 1
        if a == finalEntrada:
            print("ENTROU FINAL ENTRADA")
            token = entrada[a]
            if(entrada[a] in dicionario):
                token = entrada[a]
                tokens.append([token, dicionario[token]])
                a += 1
            elif(token != ''):
                tokens.append([token, "identificador"])
            break



            token += entrada[a]
        if(token in dicionario):
            tokens.append([token, dicionario[token]])
        elif(token != ''):
            tokens.append([token, "identificador"])
        
        if(entrada[a] in dicionario):
            token = entrada[a]
            tokens.append([token, dicionario[token]])
            a += 1

        if entrada[a]in espacoEQuebraDeLinha and a < finalEntrada:
            if(entrada[a] == '\n'):
                linha += 1
            a+=1
        if (entrada[a] not in simbolos and entrada[a] not in lentras  and entrada[a] not in numeros and entrada[a] not in espacoEQuebraDeLinha):
            raise ValueError('Erro em na linha '+ str(linha) + ", o token '"+ entrada[a]+"' não pertence a linguagem")

    for x in tokens:
            print(x[0], "|", x[1] )
    return tokens