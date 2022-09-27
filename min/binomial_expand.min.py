Q=range
L='n'
K=int
F=input
C=print
from math import comb as G
if __name__=='__main__':
	C('(a + b)^n\n');H=F('Would you like to sub into a and b? (y/N) ').lower()=='y'
	if H:D=K(F('a: '));E=K(F('b: '))
	else:D='a';E='b'
	B=K(F('n: '));C();C(f"Using ({D} + {E})^{B}\n");M=not F('Would you like to condense down the multiplication? (Y/n) ').lower()==L;N=not F('Would you like to print each term on a new line? (Y/n) ').lower()==L;O='\n+ 'if N else' + ';C()
	for A in Q(B+1):
		I=O if A!=B else'\n'
		if M:
			if H:C(f"[{G(B,A)}({D})^{B-A}][({E})^{A}]",end=I)
			else:C(f"({G(B,A)}{D}^{B-A})({E}^{A})",end=I)
		else:C(f"{D}^{B-A} * {E}^{A} * {G(B,A)}",end=I)
	C()
	if H:
		P=not F('Would you like to compute the result? (Y/n) ').lower()==L;C()
		if P:
			J=0
			for A in Q(B+1):J+=G(B,A)*D**(B-A)*E**A
			C(f"Result: {J}")