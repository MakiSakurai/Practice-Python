Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a = list(range(10))
>>> print(a)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> for i in["三条","四条",""]
SyntaxError: invalid syntax
>>> for i in["三条","四条","五条"]
SyntaxError: invalid syntax
>>> SyntaxError: invalid syntax
SyntaxError: invalid syntax
>>> for i in["三条","四条","五条"]
SyntaxError: invalid syntax
>>> for i in["三条", "四条", "五条"]:
	for j in["河原町", "烏丸", "堀川"]:
		cross = i+j
		print(cross)

		
三条河原町
三条烏丸
三条堀川
四条河原町
四条烏丸
四条堀川
五条河原町
五条烏丸
五条堀川
>>> 