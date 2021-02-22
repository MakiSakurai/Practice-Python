Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #xの平方根を求める
>>> x = 2
>>> #
>>> rnew = x
>>> #
>>> while Truw
SyntaxError: invalid syntax
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

	
2 1.5 1.0
1.5 1.4166666666666665 1.3333333333333333
1.4166666666666665 1.4142156862745097 1.411764705882353
1.4142156862745097 1.4142135623746899 1.41421143847487
1.4142135623746899 1.414213562373095 1.4142135623715002
>>> 