if __name__=='__main__':
	i=0;j=1;targ=float(input('Target (or type inf):\n'))
	while targ!=i and i<targ:print(i);nth=i+j;i,j=j,nth
	print(i);print(f"{targ} in sequence: {i==targ}")