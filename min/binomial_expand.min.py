K='n'
J=int
F=input
C=print
from math import comb as G
if __name__=='__main__':
	C('(a + b)^n\n');H=F('Would you like to sub into a and b? (y/N) ').lower()=='y'
	if H:D=J(F('a: '));E=J(F('b: '))
	else:D='a';E='b'
	A=J(F('n: '));C();C(f"Using ({D} + {E})^{A}\n");L=not F('Would you like to condense down the multiplication? (Y/n) ').lower()==K;M=not F('Would you like to print each term on a new line? (Y/n) ').lower()==K;N='\n+ 'if M else' + ';C()
	for B in range(A+1):
		I=N if B!=A else'\n'
		if L:
			if H:C(f"[{G(A,B)}({D})^{A-B}][({E})^{B}]",end=I)
			else:C(f"({G(A,B)}{D}^{A-B})({E}^{B})",end=I)
		else:C(f"{D}^{A-B} * {E}^{B} * {G(A,B)}",end=I)
	C()
	if H:
		O=not F('Would you like to compute the result? (Y/n) ').lower()==K;C()
		if O:C(f"Result: {(D+E)**A}")