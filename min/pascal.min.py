from math import comb
def smart_comb(n,i):
	if i==0 or i==n:return 1
	return comb(n,i)
def line(n):return[str(smart_comb(n,A))for A in range(n+1)]
def pascal(n):
	A=' '.join(line(n));B=len(A)
	for C in range(n):D=' '.join(line(C));print(D.center(B))
	print(A)
if __name__=='__main__':n=int(input('Number of lines: '));print();pascal(n)