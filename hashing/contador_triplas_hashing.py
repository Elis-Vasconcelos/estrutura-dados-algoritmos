import numpy as np

def hash_func(chave, tam):
  return chave % tam

def conte_triplas(array):
  n = len(array)
  m = n
  hashing = np.full(m, None)
  count = 0
  for x in array:
    i = hash_func(x, m)
    while hashing[i] is not None:
      if hashing[i][0] == x:
        hashing[i][1] += 1
        if hashing[i][1] == 3:
          count += 1
        elif hashing[i][1] > 3:
          count -= 1
        break
      else:
        i = (i + 1) % m
    else:
      hashing[i] = np.array([x, 1])
  return count

n = int(input())
array = np.array(input().split(), dtype=int)
resultado = conte_triplas(array)
print(resultado)
