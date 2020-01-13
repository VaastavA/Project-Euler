for x in range(1,1000):
  for y in range(1,x):
    z = 1000-x-y
    if (x**2+y**2) == z**2:
      print(x*y*z)
