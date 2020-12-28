#!/user/bin/env python3

#Alterado

TOTAL = 0
CONTADORNOTAS = 0

while CONTADORNOTAS <= 10:
	nota = int(input("Insira a nota: "))
	TOTAL += nota
	CONTADORNOTAS += nota
média = TOTAL/10
print(f'A média da disciplina é {(TOTAL/10)}.')

#Original

TOTAL = 0
CONTADORNOTAS = 0

while CONTADORNOTAS <= 10:
	nota = int(input("Insira a nota: "))
	TOTAL += nota
média = TOTAL/10
print(f'A média da disciplina é {(TOTAL/10)}.')


#Primeiro, para poder somar a nota ao total, deve-se atribuir isso a uma variável!
#Segundo, além de atribuir a uma variável, deve-se torná-la um inteiro, pois entra como uma string!
#Terceiro, está somando o valor ao TOTAL e não ao CONTADORNOTAS, que é a variável que alimenta o loop, ou seja, o loop será eterno.
#Quarto, se quiser que a média nunca supere 1, é preciso criar uma condicional na média onde qualquer valor de média superior a 1, será printado como 1.
