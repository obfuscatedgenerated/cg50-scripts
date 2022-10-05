M='n'
L=True
K=ValueError
G=int
F=input
A=print
from math import comb
def H(n,i):
	if i==0 or i==n:return 1
	return comb(n,i)
if __name__=='__main__':
	A('(a + b)^n\n');I=F('Would you like to sub into a and b? (y/N) ').lower()=='y'
	if I:
		while L:
			try:D=G(F('a: '));break
			except K:A('a must be a valid integer')
		while L:
			try:E=G(F('b: '));break
			except K:A('b must be a valid integer')
	else:D='a';E='b'
	while L:
		try:B=G(F('n: '));break
		except K:A('n must be a valid integer')
	A();A(f"Using ({D} + {E})^{B}\n");N=not F('Would you like to condense down the multiplication? (Y/n) ').lower()==M;O=not F('Would you like to print each term on a new line? (Y/n) ').lower()==M;P='\n+ 'if O else' + ';A()
	for C in range(B+1):
		J=P if C!=B else'\n'
		if N:
			if I:A(f"[{H(B,C)}({D})^{B-C}][({E})^{C}]",end=J)
			else:A(f"({H(B,C)}{D}^{B-C})({E}^{C})",end=J)
		else:A(f"{D}^{B-C} * {E}^{C} * {H(B,C)}",end=J)
	A()
	if I:
		Q=not F('Would you like to compute the result? (Y/n) ').lower()==M;A()
		if Q:assert type(D)is G and type(E)is G,'a and b must be integers to compute the result. this code should never be reached.';A(f"Result: {(D+E)**B}")