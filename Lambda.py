""" x = lambda a, b, c: a + b + c
print(x(5, 6, 2)) """

""" x = lambda a, b, c, d: a + b + c + d
print(x(15, 25, 20, 11)) """

""" x = lambda a, b, c, d: a * b 
print(x(15, 25, 20, 11)) """

""" x = lambda a, b, c, d: a * d
print(x(15, 25, 20, 11)) """

""" x = lambda a, b, c: a / c
print(x(125, 289, 154)) """

""" x = lambda a, b, c: a - c
print(x(200, 111, 122)) """

""" def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11)) """

""" def myfunc(n):
  return lambda a : a + n

mydoubler = myfunc(5)

print(mydoubler(22)) """

""" def myfunc(n):
  return lambda a : a / n

mydoubler = myfunc(3)

print(mydoubler(21)) """

""" def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(6)
mytripler = myfunc(5)

print(mydoubler(10)) 
print(mytripler(20)) """

def myfunc(n):
  return lambda a : a + n

mydoubler = myfunc(6)
mytripler = myfunc(5)

print(mydoubler(10)) 
print(mytripler(20))

