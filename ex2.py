Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #xの平方根を求める
>>> x = 2
>>> #
>>> rnew = x
>>> #
>>> for i in range(10):
	r1 = rnew
	r2 = x/r1
	rnew = (r1 + r2)/2
	print(r1, rnew, r2)