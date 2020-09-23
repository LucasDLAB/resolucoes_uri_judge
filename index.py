#Resoluçao 1001

'''
a=int(input('Digite um número: '))
b=int(input('Digite um numero: '))
x=a+b
print(f'A soma dos valores é igual à {x}')

'''

#Resolução 1002

'''
n=3.14159
raio=float(input())
A=(n*(raio*raio))
print(f'A={A:.4f}')

'''

#Resolução 1003

'''
A=int(input())
B=int(input())
S=A+B
print(f'SOMA = {S}')
'''

#Resolução 1004

'''
A=int(input())
B=int(input())
PROD=A*B
print(f'PROD = {PROD}')
'''

#Resolução 1005

'''
A=float(input())
B=float(input())
MEDIA=(A*3.5+B*7.5)/11
print(f'MEDIA = {MEDIA:.5f}')
'''
#Resolução 1006

'''
A=float(input())
B=float(input())
C=float(input())
Media=(A*2+B*3+C*5)/10
print(f'MEDIA = {Media:.1f}')
'''

#Resolução 1007

'''
A=int(input())
B=int(input())
C=int(input())
D=int(input())
DIFERENCA=(A*B-C*D)
print(f'DIFERENCA = {DIFERENCA}')
'''

#Resolução 1008

'''
n=int(input())
nh=int(input())
v=float(input())
print(f'NUMBER = {n}')
print(f'SALARY = U$ {nh*v:.2f}')
'''
#Resolução 1009
'''
n=input()
sf=float(input())
tv=float(input())
TOTAL=sf+tv*15/100
print(f'TOTAL = R$ {TOTAL:.2f}')
'''

#Resolução 1010
'''
numeroDaPrimeiraLinha =input().split()
numeroDaSegundaLinha = input().split()

valorPrimeiraLinha = int(numeroDaPrimeiraLinha[1])*float(numeroDaPrimeiraLinha[2])
valorSegundaLinha = int(numeroDaSegundaLinha[1])*float(numeroDaSegundaLinha[2])

resultado = valorPrimeiraLinha + valorSegundaLinha

print(f"VALOR A PAGAR: R$ {resultado:.2f}")
'''

#Resolução 1011
'''
from math import pi
v=float(input())
a=pi
vol=((4/3)*a*pow(v,3))
print(f'VOLUME = {vol:.3f}')
'''
#Resolução 1012
'''
A=float(input())
B=float(input())
C=float(input())
print(f'TRIANGULO: {A*C/2:.3f}')
print(f'CIRCULO: {3.14159*pow(C,2):.3f}')
print(f'TRAPEZIO: {(A+B)*C/2:.3f}')
print(f'QUADRADO: {B*B:.3f}')
print(f'RETANGULO: {A*B:.3f}')
'''

#Resolução 1012(2º forma)
'''
num=[ float(i) for i in input().split() ]

TRIANGULO=num[0]*num[2]/2
CIRCULO=3.14159*pow(num[2],2)
TRAPEZIO=(num[0]+num[1])*num[2]/2
QUADRADO=num[1]*num[1]
RETANGULO=num[0]*num[1]
print(f'TRIANGULO: {TRIANGULO:.3f}')
print(f'CIRCULO: {CIRCULO:.3f}')
print(f'TRAPEZIO: {TRAPEZIO:.3f}')
print(f'QUADRADO: {QUADRADO:.3f}')
print(f'RETANGULO: {RETANGULO:.3f}')
'''

#Resolução 1013
'''
num=[int(i) for i in input().split() ]
print(f'max(num) eh maior')
'''

#Resolução 1014
'''
X=int(input())
Y=float(input())
c=X/Y
print(f'{c:.3f} km/l')
'''

#Resolução 1015
'''
num1=[float(i) for i in input().split()]
num2=[float(i) for i in input().split()]
D=((num2[0]-num1[0])**2)+(num2[1]-num1[1])**2
D=pow(D,1/2)
print(f'{D:.4f}')
'''
#Resolução 1016
'''
x = int(input())
result = x*2
print(f'{result} minutos')
'''

#Resolução 1017
'''
h=int(input())
v=int(input())
cc=(h*v/12)
print(f'{cc:.3f}')
'''

#Resolução 1018
'''
N=int(input())
print(N)
for c in (100,50,20,10,5,2,1):
	notas=0
	if N>=c:
		notas=(N//c)
	print(f'{notas} nota(s) de R$ {c},00')
	N-=notas*c
'''
#Resolução 1019
'''
n=(input())
h=m=s=0
for c in range (1,n+1):
	s+=1
	if s==60:
		s=0
		m+=1
		if m==60:
			m=0
			h+=1
print(f'{h}:{m}:{s}')
'''

#Resolução 1020
'''
n=int(input())
a=0
m=0
if n>=365:
	a=n//365
	n-=a*365
if n>=30:
	m=n//30
	n-=m*30
print(f'{a} ano(s)')
print(f'{m} mes(es)')
print(f'{n} dia(s)')
'''
#Resolução 1021
'''
N=float(input())
print(N)
print('NOTAS:')
for c in (100.00,50.0,20.0,10.0,5.0,2.0):
	notas=0
	if N>=c:
		notas=(N//c)
	print(f'{notas:.0f} nota(s) de R$ {c:.2f}')
	N-=notas*c
	N=round(N,2)
N=N*100
print('MOEDAS:')
for c in (1,0.50,0.25,0.10,0.05,0.01):
	notas=0
	if N>=c:
		notas=(N//(c*100))
	print(f'{notas:.0f} moeda(s) de R$ {c:.2f}')
	N-=notas*(c*100)
	N=round(N,2)
'''

#Resolução 1035
n=[float(i) for i in input().split()]
if n[1]>n[2] and n[3]>n[0] and (n[2]+n[3])>(n[0]+n[1]) and n[2]>0 and n[3]>0 and n[0]%2==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')


