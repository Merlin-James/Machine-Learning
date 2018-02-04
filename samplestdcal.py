Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import math
>>> l = [0.36, 0.36, 0.18, 0.1]
>>> c = []
>>> for i in l:
	c.append(-i*math.log(i, c))

	

Traceback (most recent call last):
  File "<pyshell#6>", line 2, in <module>
    c.append(-i*math.log(i, c))
TypeError: a float is required
>>> for i in l:
	c.append(-i*math.log(i, 2))

	
>>> print(c)
[0.5306152277996684, 0.5306152277996684, 0.4453076138998342, 0.33219280948873625]
>>> sum(c)
1.8387308789879073
>>> data = [0.53, 0.53, 0.45, 0.33]
>>> n = len(data)
>>> ss = sum(i**2 for i in data)
>>> var = ss/(n-1)
>>> print(var)
0.291066666667
>>> std = math.sqrt(var)
>>> print(std)
0.539505946832
>>> myMean = lambda MyList : reduce(lambda x, y: x + y, MyList) / float(len(MyList))

>>> myStd = lambda MyList : (reduce(lambda x,y : x + y , map(lambda x: (x-myMean(MyList))**2 , MyList)) / float(len(MyList)))**.5

 
>>> 
>>> 
>>> 
>>> myStd = lambda MyList : (reduce(lambda x,y : x + y , map(lambda x: (x-myMean(MyList))**2 , MyList)) / float(len(MyList)))**.5
>>> print myStd([0.53, 0.53, 0.45, 0.33])
0.0818535277187
>>> 





hihk


;k;k4

4


