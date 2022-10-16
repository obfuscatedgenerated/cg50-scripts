b='-csc^2'
a='sec^2'
Z='-sin'
Y=ValueError
X=input
T='e'
S='ln'
R='csc'
Q='sin'
P=str
K='cot'
J='sec'
I='tan'
H=print
E='cos'
from math import sin as A,cos as B,tan as F,log,e
U=lambda x:log(x,e)
L=lambda x:1/B(x)
M=lambda x:1/A(x)
N=lambda x:1/F(x)
O={A:Q,B:E,F:I,L:J,M:R,N:K,U:S,e:T}
G={A:B,B:lambda x:-A(x),F:lambda x:1/B(x)**2,L:lambda x:L(x)*F(x),M:lambda x:-M(x)*N(x),N:lambda x:-1/A(x)**2,U:lambda x:1/x,e:lambda x:e**x}
f={Q:E,E:Z,I:a,J:'sec tan',R:'-csc cot',K:b,S:'1/x',T:'e^x'}
def c(func,x):A={Q:E+x,E:Z+x,I:a+x,J:J+x+I+x,R:'-csc'+x+K+x,K:b+x,S:'1/'+x,T:'e^'+x};return A[func]
def g(func,x,h=0.0001):return(func(x+h)-func(x))/h
def d(func,x):return G[func](x)
V=0
for C in G:H(P(V+1)+') '+O[C]+"'(x) = "+c(O[C],'(x)'));V+=1
H()
while True:
	D=X('Select a function by number (leave blank to exit): ')
	if D=='':break
	try:
		D=int(D)
		if D not in range(1,len(G)+1):raise Y
	except Y:H('Invalid option');continue
	C=list(G)[D-1];W=float(X('Enter a value for x: '));H(O[C]+"'("+P(W)+') = '+P(d(C,W)))