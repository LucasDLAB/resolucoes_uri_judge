#Resolução dos exercicios de Classe
 
#Exercicio 01
'''
class bola(object):
	def trocacor(self,c):
		self.cor=c
	def mostracor(self,c):
		self.trocacor(c)
		print(f'A cor era {color} foi alterada para {self.cor}')
from math import pi
b=bola()
r=pi *pow(int(input()),2)
m=input('Material: ')
color=input('Digite a cor da bola: ')
while True:
	D=input('Deseja trocar a cor da bola? [S/N] ').upper()[0]
	if D in 'SN':
		if D in 'S':
			cor=input('Digite a cor da bola : ')
			print(f''O raio da bola é {r:.2f}
A bola é de {m}'')
			b.mostracor(cor)
		elif D in 'N':
			print(f''O raio da bola é {r:.2f}
A bola é de {m}
A cor da bola é {color}'')
		break
	else:
		print('Tente novamente')
'''

#Exercicio 02
'''
class quad(object):
	l=0
	def mudarlado(self):
		self.l=float(input('Digite dos lados: ')) 
	def calculo(self,a):
		c=a*a
		return c
A=quad()
A.mudarlado()
print(A.l)
calc=A.calculo(A.l)
print(f'A area do quadrado é {calc}')
'''

#Exercicio 03
'''
class ret(object):
	b=0
	h=0
	def mudarlado(self):
		self.b=float(input('Digite a base: '))
		while True:
			self.h=float(input('Digite a altura: '))
			if self.b!=self.h:
				break
			else:
				print('Os lados devem ser diferentes')
	def calculo(self,a,b):
		re=a*b
		return re
	def perimetro(self,a,b):
		re=((2*a)*(2*b))
		return re
r=ret()
r.mudarlado()
a=r.calculo(r.b,r.h)
p=r.perimetro(r.b,r.h)
print(f'Area={a} Perimetro={p}')
'''

#Exercicio 04
''
