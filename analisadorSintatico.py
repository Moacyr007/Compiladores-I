import analisadorLexico
import analisadorSemantico
count = 0

def analisadorSintatico(tokensl ,entrada):
    global tokens 
    tokens = tokensl
    global count
    count = 0
    z()
    return(entrada)

def erro(recebido, esperado, i):
    raise ValueError("erro, recebeu "+recebido+" mas esperava "+esperado+", item numr:"+str(i))

def t():
    global count
    if(tokens[count][1] == "identificador"):
        analisadorSemantico.inserir_verificacao(tokens[count][0])
        count+=1
    else:
        erro(tokens[count][1],"identificador", count)

def r():
    global count
    if(count < len(tokens)):
        if(tokens[count][1] == "soma"):
            count += 1
            t()
            r()
        else:
            analisadorSemantico.verificar_tipos()

def e():
    t()
    r()

def s():
    global count
    if(tokens[count][1] == "identificador"):
        analisadorSemantico.verificar_declaracao(tokens[count][0])
        analisadorSemantico.inserir_verificacao(tokens[count][0])
        count += 1
        if(tokens[count][1] == "atribuicao"):
            count += 1
            e()
            analisadorSemantico.verificar_tipos()
    elif(tokens[count][1] == "condicional"):
        count += 1
        e()
        if(tokens[count][1] == "acao condicional"):
            count += 1
            s()
        else:
            erro(tokens[count][1],"identificador", count)
    else:
        erro(tokens[count][1],"identificador", count)

def o():
    global count
    if(tokens[count][1] == "ponto e virgula"):
        count += 1
        d()

def k():
    global count
    if(tokens[count][1] == "tipoReal" or tokens[count][1] == "tipoInteger"):
        analisadorSemantico.inserir_tipo_id(tokens[count][0])
        count += 1
    else:
        erro(tokens[count][1],"integer ou real", count)

def x():
    global count
    if(tokens[count][1] == "virgula"):
        count += 1
        l()

def l():
    global count
    if(tokens[count][1] == "identificador"):
        analisadorSemantico.inserir_id(tokens[count][0], tokens[count][1])
        count += 1
        x()
    else:
        erro(tokens[count][1],"identificador", count)
    

def d():
    global count
    l()
    if(tokens[count][1] == "dois pontos"):
        count += 1
    else:
        erro(tokens[count][1],"dois pontos", count)
    k()
    o()

def i():
    global count
    if(tokens[count][1] == "declaracao"):
        count += 1
        d()
    else:
        erro(tokens[count][1],"declaracao", count)

def z():
    i()
    s()
    if(len(tokens) > count):
         raise ValueError("Esperava fim do código mas ainda tinham mais tolkens")
