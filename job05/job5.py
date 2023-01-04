import math

def nombre_premier(n):
            for i in range(2, int(math.sqrt(n) + 1)):
                  if n % i == 0:
                        return False
            return True


for n in range (2,1000):
      if nombre_premier(n):
            print(n)