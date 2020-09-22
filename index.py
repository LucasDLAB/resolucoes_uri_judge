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
''
num=[int(i) for i in input().split() ]
print(max(num))

