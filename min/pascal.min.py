D=print
C=range
A=' '
def B(n):
	A=1
	for B in C(2,n+1):A*=B
	return A
def F(n,r):return B(n)//B(r)//B(n-r)
def G(n,i):
	if i==0 or i==n:return 1
	return F(n,i)
def E(n):return[str(G(n,A))for A in C(n+1)]
def H(string,length):C=string;B=length-len(C);return A*(B//2)+C+A*(B-B//2)
def I(n):
	B=A.join(E(n));F=len(B)
	for G in C(n):I=A.join(E(G));D(H(I,F))
	D(B)
J=int(input('Number of lines: '))
D()
I(J)