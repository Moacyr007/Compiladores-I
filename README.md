<<<<<<< HEAD
Analisador Léxico da Linguagem G

G = ( {Z,I,D,L,X,K,O,S,E,R,T}, {var, : , id, , , integer, real, ; , :=, if, then,+}, P, Z)
P:
Z → I S
I → var D
 D → L : K O
L → id X
 X → , L
 X → ε
 K → integer
 K → real
 O → ; D
 O →ε
 S → id := E
S → if E then S
E → T R
R → + T R
R → ε
T → id
=======
Implementação de um compilador para disciplina de Compiladores
>>>>>>> master
