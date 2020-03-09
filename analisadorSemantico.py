global tabelaSimbolos
global tabelaVerificacaoTipos
tabelaSimbolos = []
tabelaVerificacaoTipos = []

#{cadeia, tipoTOken, tipoIdentificador}

def inserir_id(cadeia, tipoToken):
    global tabelaSimbolos
    tabelaSimbolos.append([cadeia, tipoToken, ""])

def inserir_tipo_id(tipo):
    global tabelaSimbolos
    for a in range(len(tabelaSimbolos)):
        if(tabelaSimbolos[a][2] == ""):
            tabelaSimbolos[a][2] = tipo

#verifica se um id existe na tabela de simbolos
def verificar_declaracao(cadeia):
    global tabelaSimbolos
    flagDeclarado = 0
    for a in range(len(tabelaSimbolos)):
        if(tabelaSimbolos[a][0] == cadeia):
            flagDeclarado = 1
            return True
    if(flagDeclarado == 0):
        raise ValueError("A variável "+cadeia+" não foi declarada")  

#verifica se os tipos da tabelaVErificacaoTIpos são os mesmos
def verificar_tipos():
    global tabelaVerificacaoTipos
    tipo = tabelaVerificacaoTipos[0][1]
    for a in range(len(tabelaVerificacaoTipos)):
        if(tabelaVerificacaoTipos[a][1] == tipo):
            print("")
        else:
            raise ValueError("Operação com tipos diferentes")
    tabelaVerificacaoTipos = []

#inseri um identificador na tabela de verificação
def inserir_verificacao(cadeia):
    global tabelaSimbolos
    global tabelaVerificacaoTipos
    flag_verificacao = 0
    for a in range(len(tabelaSimbolos)):
        if(tabelaSimbolos[a][0] == cadeia):
            tipo = tabelaSimbolos[a][1]
            flag_verificacao = 1
    if(flag_verificacao == 0):
        raise ValueError("A variável "+cadeia+" não foi declarada")
    tabelaVerificacaoTipos.append([cadeia, tipo])

