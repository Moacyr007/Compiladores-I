import analisadorLexico
import analisadorSintatico

path = r'D:\Projetos\analisadorLexicoSecreto\entradaAva.txt'
f = open(path, 'r')
entrada = f.read()

tokens = analisadorLexico.analisadorLexico(entrada)
print(tokens)
analisadorSintatico.analisadorSintatico(tokens)