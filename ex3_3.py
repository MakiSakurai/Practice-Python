Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #xの平方根を求める
>>> x = 2
>>> #
>>> rnew = x
>>> #
>>> while True:
	r1 = rnew
	r2 = x/r1
	rnew = (r1 + r2)/2
	print(r1, rnew, r2)
	diff = r1 - r2
	if(diff < 0):
		diff = -diff
	if diff <= 1.0E-6:
		break
	
