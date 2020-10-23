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
'''
n=[float(i) for i in input().split()]
if n[1]>n[2] and n[3]>n[0] and (n[2]+n[3])>(n[0]+n[1]) and n[2]>0 and n[3]>0 and n[0]%2==0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
'''

#Resolução 1036
'''
n=[float(i) for i in input().split()]
D=(n[1]**2)-4*n[0]*n[2]
if D<0 or n[0]==0:
	print('Impossível calcular')
else:
	r1=((-1*n[1])+ (pow(D,1/2)))/(2*n[0])
	r2=((-1*n[1])- (pow(D,1/2)))/(2*n[0])
	print(f'R1={r1}')
	print(f'R2={r2}')
'''


#Resolução 1037
'''
n= float(input())
lista=[[0,25],[25,50],[50,75],[75,100]]
cont=0
while True:
	if cont==4:
		break
	if cont==0:
		if lista[cont][0]<=n and n<=lista[cont][1]:
			break	
	else:	
		if n>lista[cont][0] and n<=lista[cont][1]:
			break
	cont+=1
if cont==0:
	print(f"Intervalo [{lista[cont][0]},{lista[cont][1]}]")		
elif cont>=1 and cont<=3:
	print(f"Intervalo ({lista[cont][0]},{lista[cont][1]}]")
elif cont==4:
	print('Fora de intervalo')
'''

#Resolução 1074
'''
n=int(input())
if n==0:
    print('NULL')
elif n%2==0 and n!=0:
    print('EVEN ',end='')
elif n%2==1:
    print('ODD ',end='')
if n>0:
    print('POSITIVE')
if n<0:
    print('NEGATIVE')
'''

#Resolução 1075
'''
n=int(input())
for c in range (1,10001):
	if c%13==2:
		print(c)
'''

#Resolução 1078
'''
n=int(input())
for c in range (1,11):
	print(f'{c} x {n} = {c*n}')
'''

#	Resolução 1079
'''
n=int(input())
med=0
for c in range (0,n):
	m=[float(i) for i in input().split()]
	for a in range (0,len(m)):
		if a==0:
			med=m[a]*2
		elif a==1:
			med+=m[a]*3
		elif a==2:	
			med+=m[a]*5
	med=med/10
	print(f'{med:.1f}')	
'''

#Resolução 1080
'''
l=[]
for c in range (0,99):
	n=int(input())
	l.append(n)
print('Maior: ',max(l))
print('Posição: ',(l.index(max(l))+1)) 
'''

#Resolução 1094
'''
n=int(input())
t=0
tc=0
tr=0
ts=0
for c in range (0,n):
	e=[str(i) for i in input() .split()]
	e[0]=int(e[0])
	t+=e[0]
	if e[1]in'Cc':
		tc+=e[0]
	elif e[1]in'Rr':
		tr+=e[0]
	elif e[1]in'Ss':
		ts+=e[0]
print(f'Total: {t} cobaias')
print(f'Total de coelhos: {tc}')
print(f'Total de ratos: {tr}')
print(f'Total de sapos: {ts}')
print(f'Percentual de coelhos: {tc/t*100:.2f}%')
print(f'Percentual de ratos: {tr/t*100:.2f}%')
print(f'Percentual de sapos: {ts/t*100:.2f}%')
'''

#Resolução 1095
'''
i=1
j=60
print(f'I={i} J={j}')
while j!=0:
	i+=3
	j-=5
	print(f'I={i} J={j}')
'''

#Resolução 1096
'''
i=1
while i<10:
	j=7
	for c in range (0,3):
		print(f'I={i} J={j}')
		j-=1
	i+=2
'''

#Resolução 1097
'''
i=1
j=7
while i<10:
	for c in range (0,3):
		print(f'I={i} J={j}')
		j-=1
	j+=5
	i+=2
'''

#Resolução 1098
'''
i=0
j=1
while i<=2:
	for c in range (0,3):
		print(f'I={i:.1f} J={j:.1f}')
		j+=1
	j-=3
	j+=0.2
	i+=0.2
'''

#Resolução 1099
'''
n=int(input())
for c in range (0,n):
	si=0
	num=[int(c) for c in input() .split()]
	if num[0]>num[1]:
		for c in range (num[1]+1,num[0]):
			if c%2==1:
				si+=c
	else:
		for c in range (num[0]+1,num[1]):
			if c%2==1:
				si+=c
	print(si)
'''

#Resolução 1101
'''
while True:
	s=0
	num=[int(c) for c in input() .split()]
	if 0 in num:
		break
	if num[0]>num[1]:
		for c in range (num[1],num[0]+1):
				s+=c
	else:
		for c in range (num[0],num[1]+1):
				s+=c
	print(s)
'''

#Resolução 1113
'''
while True:
	s=0
	num=[int(c) for c in input() .split()]
	if num[0]==num[1]:
		break
	if num[0]<num[1]:
		print('Crescente')
	else:
		print('Decrescente')
'''

#Resolução 1114
'''
while True:
	s=input()
	if s=="2002":
		print('Acesso permitido')
		break
	else:
		print('Senha Inválida')
'''

#Resolução 1115
'''
while True:
	num=[int(c) for c in input() .split()]
	if num[0]>0 and num[1]>0:
		print('Primeiro')
	elif num[0]<0 and num[1]>0:
		print('Segundo')
	elif num[0]<0 and num[1]<0:
		print('Terceiro')
	elif num[0]>0 and num[1]<0:
		print('Quarto')
	else:
		print('Nulo')
		break
'''

#Resolução 1116
'''
n=int(input())
for c in range (0,n):
	num=[int(i) for i in input() .split()]
	if num[1]!=0:
		print(num[0]/num[1])
	else:
		print('Divisão impossível')
'''

#Resolução 1117
'''
while True:
	n1=float(input())
	if n1>=0 and n1<=10:
		break
	else:
		print('Senha inválida')
while True:
	n2=float(input())
	if n2>=0 and n2<=10:
		break
	else:
		print('Senha inválida')
print(f'Média: {(n1+n2)/2}')
'''

#Resolução 1118
'''
while True:
	while True:
		n1=float(input())
		if n1>=0 and n1<=10:
			break
		else:
			print('Senha inválida')
	while True:
		n2=float(input())
		if n2>=0 and n2<=10:
			break
		else:
			print('Senha inválida')
	print(f'Média: {(n1+n2)/2}')
	while True:
		print('Novo calcúlo? [1-sim/2-não]')
		x=int(input())
		if x==1 or x==2:
			break
	if x==2:
		break
'''

#Resolução 1131
'''
t1=t2=e=0
while True:
	num=[int(i) for i in input() .split()]
	if num[0]>num[1]:
		t1+=1
	elif num[1]>num[0]:
		t2+=1
	else:
		e+=1	
	while True:
		print('Novo grenal? [1-sim/2-não]')
		x=int(input())
		if x==1 or x==2:
			break
	if x==2:
		break
print(f'Time 1:{t1}')
print(f'Time 2:{t2}')
print(f'Empate:{e}')
if t1>t2:
	print('Time 1 venceu mais')
elif t1<t2:
	print('Time 2 venceu mais')
else:
	print('Os times tem a mesma pontução')
'''

#Resolução 1132
'''
n1=int(input())
n2=int(input())
s=0
if n1>n2:
	for c in range (n2,n1+1):
		if c%13==1:
			s+=c
else:
	for c in range (n1,n2+1):
		if c%13!=0:
			s+=c
print(s)
'''

#Resolução 1133
'''
n1=int(input())
n2=int(input())
if n1>n2:
	for c in range (n2,n1):
		if c%5==2 or c%5==3:
			print(c)
else:
	for c in range (n1,n2):
		if c%5==2 or c%5==3:
			print(c)
'''

#Resolução 1134
'''
A=D=G=0
while True:
	while True:
		e=int(input())
		if e<=4 and e>0:
			break
	if e==1:
		A+=1
	elif e==2:
		G+=1
	elif e==3:
		D+=1
	else:
		break
print('Muito obrigado!!!')
print(f'Alcool:{A}')
print(f'Gasolina:{G}')
print(f'Diesel:{D}')
'''

#Resolução 1142
'''
v=int(input())
n=0
for c in range (0,v):
	n+=1
	for a in range (0,3):
		print(n,end=' ')
		n+=1
	print('PUM')	
'''

#Resolução 1143
'''
v=int(input())
n=1
for c in range (1,v+1):
	print(f'{c} {c**2} {c**3}')
'''

#Resolução 1144
'''
n2=n3=1
v=int(input())
t=1
s=0
for c in range (1,v+1):
	print(f'{c} {n2} {n2*c}')
	print(f'{c} {n2+1} {n2*c+1}')
	n2+=1
	n3+=1
	s+=2
	if t==1:
		n2+=s
'''
	
	
	



















