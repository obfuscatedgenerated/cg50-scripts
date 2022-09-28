from math import comb
def line(n):return[str(comb(n,A))for A in range(n+1)]
def pascal(n):
	A=' '.join(line(n));B=len(A)
	for C in range(n):D=' '.join(line(C));print(D.center(B))
	print(A)
if __name__=='__main__':n=int(input('Number of lines: '));print();pascal(n)