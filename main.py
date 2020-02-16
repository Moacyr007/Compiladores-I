import analisadorLexico

path = r'D:\Projetos\analisadorLexicoSecreto\entradaAva.txt'
f = open(path, 'r')
entrada = f.read()

analisadorLexico.analisadorLexico(entrada)
