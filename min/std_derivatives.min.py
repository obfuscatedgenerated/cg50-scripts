W=ValueError
V=input
S='e'
R='ln'
Q='cot'
P='csc'
O='sec'
N='tan'
M='sin'
H='cos'
G=print
from math import sin as A,cos as B,tan as E,log,e
T=lambda x:log(x,e)
I=lambda x:1/B(x)
J=lambda x:1/A(x)
K=lambda x:1/E(x)
L={A:M,B:H,E:N,I:O,J:P,K:Q,T:R,e:S}
F={A:B,B:lambda x:-A(x),E:lambda x:1/B(x)**2,I:lambda x:I(x)*E(x),J:lambda x:-J(x)*K(x),K:lambda x:-1/A(x)**2,T:lambda x:1/x,e:lambda x:e**x}
a={M:H,H:'-sin',N:'sec^2',O:'sec tan',P:'-csc cot',Q:'-csc^2',R:'1/x',S:'e^x'}
def X(func,x):A={M:f"cos{x}",H:f"-sin{x}",N:f"sec^2{x}",O:f"sec{x}tan{x}",P:f"-csc{x}cot{x}",Q:f"-csc^2{x}",R:f"1/{x}",S:f"e^{x}"};return A[func]
def b(func,x,h=0.0001):return(func(x+h)-func(x))/h
def Y(func,x):return F[func](x)
if __name__=='__main__':
	for (Z,C) in enumerate(F):G(f"{Z+1}) {L[C]}'(x) = {X(L[C],'(x)')}")
	G()
	while True:
		D=V('Select a function by number (leave blank to exit): ')
		if D=='':break
		try:
			D=int(D)
			if D not in range(1,len(F)+1):raise W
		except W:G('Invalid option');continue
		C=list(F)[D-1];U=float(V('Enter a value for x: '));G(f"{L[C]}'({U}) = {Y(C,U)}")