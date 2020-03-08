import analisadorLexico
import analisadorSintatico

path = r'D:\Projetos\analisadorLexicoSecreto\entradaCodigo.txt'
f = open(path, 'r')
entrada = f.read()

tokens = analisadorLexico.analisadorLexico(entrada)
entrada_sintaticamente_correta = analisadorSintatico.analisadorSintatico(tokens, entrada)