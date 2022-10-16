T=' * '
S=' + '
R=range
Q='n'
P=')^'
O=True
N=ValueError
I='^'
H=int
G=input
B=print
A=str
def J(n):
	A=1
	for B in R(2,n+1):A*=B
	return A
def U(n,r):return J(n)//J(r)//J(n-r)
def K(n,i):
	if i==0 or i==n:return 1
	return U(n,i)
B('(a + b)^n\n')
L=G('Would you like to sub into a and b? (y/N) ').lower()=='y'
if L:
	while O:
		try:E=H(G('a: '));break
		except N:B('a must be a valid integer')
	while O:
		try:F=H(G('b: '));break
		except N:B('b must be a valid integer')
else:E='a';F='b'
while O:
	try:C=H(G('n: '));break
	except N:B('n must be a valid integer')
B()
B('Using ('+A(E)+S+A(F)+P+A(C)+'\n')
V=not G('Would you like to condense down the multiplication? (Y/n) ').lower()==Q
W=not G('Would you like to print each term on a new line? (Y/n) ').lower()==Q
X='\n+ 'if W else S
B()
for D in R(C+1):
	M=X if D!=C else'\n'
	if V:
		if L:B('['+A(K(C,D))+'('+A(E)+P+A(C-D)+'][('+A(F)+P+A(D)+']',end=M)
		else:B('('+A(K(C,D))+A(E)+I+A(C-D)+')('+A(F)+I+A(D)+')',end=M)
	else:B(A(E)+I+A(C-D)+T+A(F)+I+A(D)+T+A(K(C,D)),end=M)
B()
if L:
	Y=not G('Would you like to compute the result? (Y/n) ').lower()==Q;B()
	if Y:assert type(E)is H and type(F)is H,'a and b must be integers to compute the result. this code should never be reached.';B('Result: '+A((E+F)**C))