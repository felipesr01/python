'''
ANSI escape sequence
comeca com \ depois codigo
#cor sempre comeca com \033 e por fim uma letra minuscula
\033[style:text:backm]

#estilos style
0 = none
1 = bold
4 = underline
7 = negative

#texto text
30 branco
31 vermelho
32 verde
33 amarelo
34 azul
35 magenta
36 ciano
37 cinza

#fundo back
40
41
42
43
44
45
46
47

#Testes
\033[0;30;41m]
\033[4;33;44m]
\033[1;35;43m]
\033[0;30;43m]
\033[m
\033[7;30m

#print('\033[7:40mOla Mundo')
print('Minha cor favorita é \033[4:34:40mAzul\033[m')
'''