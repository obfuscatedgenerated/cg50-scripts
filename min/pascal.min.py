E=range
B=print
from math import comb
def A(n):return[str(comb(n,A))for A in E(n+1)]
def C(n):
	H=' ';C=H.join(A(n));D=len(C)
	for F in E(n):G=H.join(A(F));B(G.center(D))
	B(C)
if __name__=='__main__':D=int(input('Number of lines: '));B();C(D)