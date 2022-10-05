C=range
A=print
from math import comb
def D(n,i):
	if i==0 or i==n:return 1
	return comb(n,i)
def B(n):return[str(D(n,A))for A in C(n+1)]
def E(n):
	D=' '.join(B(n));E=len(D)
	for F in C(n):G=' '.join(B(F));A(G.center(E))
	A(D)
if __name__=='__main__':F=int(input('Number of lines: '));A();E(F)