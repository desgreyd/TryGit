def d(x):
	if not isinstance(x,(int,float)):
		raise TypeError('sfs')
	return x+1,x+2
print "let's play a game~input a number~"
a=int(input())
r=d(a)
print r
print '\n'
r[0]=100
print r


