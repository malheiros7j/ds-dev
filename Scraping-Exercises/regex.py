import re

text00 = '054.684.891-55'
text01 = '0544.684.891-55'

#text00 = '3 numeros 1 ponto 3 numeros 1 ponto 3 numeros 1 traco 2 numeros'
# . qualquer caracter 
# d-> 0-9
# ^ -> começo string $ -> final string

regex = '^\d{4}\.\d{3}\.\d{3}-\d{2}$'

print(bool(re.match(regex,text01)))

'''
## Marcadores de Início e Fim de Linha

^Python - Encontra qualquer string que esteja em inicio de linha e contenha os caracteres 'Python'
Python$ - Encontra qualquer string que esteja em fim de linha e contenha os caracteres 'Python'


## Marcadores de quantidaed

* -> Se refere imediamente ao caracter anterior a ele

Pyt* - Encontra string com sequencia de caractereces 'Py', seguida de zero ou mais ocorrencia do caracter 't'. - 0 ou mais
Pyt+ - Encontra string com sequencia de caractereces 'Py', seguida de uma ou mais ocorrencia do caracter 't'. - Pelo menos 1
Pyt? - Encontra string com sequencia de caractereces 'Py', seguida de zero ou uma ocorrencia do caracter 't'. - 0 ou 1
Pyt{3} - Encontra string com sequencia de caracteres 'PY', seguida de exatamente 3 ocorrencias do caracter 't'.
Pyt{2,4} - Encontra string com sequencia de caracteres 'PY', seguida de 2 a 4 ocorrencias do caracter 't'.
Pyt{3,} - Encontra string com sequencia de caracteres 'PY', seguida de 3 ou mais ocorrencias do caracter 't'.
Py(th)* - Encontra string com sequencia de caracteres 'PY', seguida de zero ou mais ocorrencias da sequencia 'th'.

## Marcador de alternativa ou operador OR ( | )

Este marcador é utilizado para inserir no padrão uma alternativa de caractere ou sequência de caracteres. 
Na prática, funciona como o operador OR na sequência expressa no padrão. Exemplos:

Pyt|hon – Encontra strings com a sequência de caracteres “Pyt” ou strings com a sequência de caracteres “hon”. 
Py(t|h) – Encontra strings com a sequência de caracteres “Py” seguida do caractere “t” ou do caractere “h”. 
Py(t|h|o) – Encontra strings com a sequência de caracteres “Py” seguida do caractere “t” ou do caractere “h” ou do caractere “o”. 


## Marcador de definição de Conjuntos ([ ])
Utilizando este marcador, podemos definir um conjunto de caracteres para a composição de padrões. O último exemplo do tópico anterior pode ser reescrito da seguinte forma:

Py[tho] – Encontra strings com a sequência de caracteres “Py” seguida de um caractere pertencente ao conjunto (t, h, o). 
Outros exemplos comuns de conjuntos utilizados:
Py[0-9] – Encontra strings com a sequência de caracteres “Py” seguida de um caractere pertencente ao conjunto de dígitos de 0 a 9. 
Py[a-z] – Encontra strings com a sequência de caracteres “Py” seguida de um caractere pertencente ao conjunto de caracteres alfabéticos de “a” a “z”. 


Marcadores de classes de caracteres (\w, \d, \s e .)
\w – Representa um caractere alfanumérico, incluindo ocorrências maiúsculas e minúsculas das letras e o caractere “_”.
\d – Representa um caractere numérico e equivale a definição do conjunto [0-9]
\s – Representa um espaço em branco, incluindo tabulações e quebras de linha

. – Este caractere é utilizado como coringa e representa qualquer caractere.
A utilização de \W, \D e \S serve como negação de suas correspondentes descritas acima. \W vai encontrar, por exemplo, qualquer caractere que não seja relevante para \w.


#################


























