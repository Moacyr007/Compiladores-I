tabelaSimbolos = []
tabelaVerificacaoTipos = []

#{cadeia, tipoTOken, tipoIdentificador}

def inserir_id(cadeia, tipoToken):
    tabelaSimbolos.append([cadeia, tipoToken])

def inserir_tipo_id(cadeia, tipo):
    for a in range(len(tabelaSimbolos)):
        if(tabelaSimbolos[a][0] == cadeia):
            tabelaSimbolos[a][2] = tipo

    ValueError("A variável "+cadeia+" não foi declarada")  

#verifica se um id existe na tabela de simbolos
def verificar_declaracao(cadeia):
    flagDeclarado = 0
    for a in range(len(tabelaSimbolos)):
        if(tabelaSimbolos[a][0] == cadeia):
            flagDeclarado = 1
            return True
    if(flagDeclarado == 0):
        raise ValueError("A variável "+cadeia+" não foi declarada")  

#verifica se os tipos da tabelaVErificacaoTIpos são os mesmos
def verificar_tipos():
    tipo = tabelaVerificacaoTipos[0][1]
    for a in range(len(tabelaVerificacaoTipos)):
        if(tabelaVerificacaoTipos[a][1] == tipo):
            print("")
        else:
            raise ValueError("A variável "+cadeia+" não foi declarada")
    tabelaVerificacaoTipos = []

#inseri um identificador na tabela de verificação
def inserir_verificacao(cadeia):
    for a in range(len(tabelaSimbolos)):
        if(tabelaSimbolos[a][0] == cadeia):
            tipo = tabelaSimbolos[a][1]
        else:
            raise ValueError("A variável "+cadeia+" não foi declarada")
    tabelaVerificacaoTipos.append([cadeia, tipo])

