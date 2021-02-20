Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 2
>>> rnew = x
>>> r1 = rnew
>>> r2 = x/r1
>>> rnew = (r1 + r2)/2
>>> print(r1,rnew,r2)
2 1.5 1.0
>>> r1 = rnew
>>> r2 = x/r1
>>> rnew = (r1 + r2)/2
>>> print(r1,rnew, r2)
1.5 1.4166666666666665 1.3333333333333333
>>> r1 = rnew
>>> r2 = x/r1
>>> rnew = (r1 + r2)/2
>>> print(r1,rnew,r2)
1.4166666666666665 1.4142156862745097 1.411764705882353
>>> 