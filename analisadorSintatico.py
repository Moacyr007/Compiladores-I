import analisadorLexico

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
        count+=1
    else:
        erro(tokens[count][1],"identificador", count)

def r():
    global count
    if(tokens[count][1] == "soma"):
        count += 1
        t()
        r()

def e():
    t()
    r()

def s():
    global count
    if(tokens[count][1] == "identificador" and tokens[count+1][1] == "atribuicao"):
        count += 2
        e()
    elif(tokens[count][1] == "condicional"):
        count += 1
        e()
        if(tokens[count][1] == "acao condicional"):
            count += 1
            s()
    else:
        erro(tokens[count][1],"identificador", count)

def o():
    global count
    if(tokens[count][1] == "ponto e virgula"):
        count += 1
        d()

def k():
    global count
    if(tokens[count][1] == "tipo"):
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
        erro(tokens[count][1],"identificador", count)

def z():
    i()
    s()


