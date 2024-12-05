import numpy as np

class HashTable:
  def __init__(self, tam):
      self.tam = tam
      self.hashing = np.full((tam, 2), -1)

  def hash_func(self, par):
      return (par[0] + par[1]) % self.tam

  def inserir(self, par):
      index = self.hash_func(par)
      while self.hashing[index][0] != -1:
          index = (index + 1) % self.tam
          if index == self.hash_func(par):
              return False
      self.hashing[index] = par
      return True

  def busca(self, par):
      index = self.hash_func(par)
      while self.hashing[index][0] != -1:
          if np.array_equal(self.hashing[index], par):
              return index
          index = (index + 1) % self.tam
          if index == self.hash_func(par):
              return -1
      return -1

N = int(input())
hash_table = HashTable(2 * N + 1)
par_simetrico = None

for _ in range(N):
  par = np.array(input().split(), dtype=int)
  simetrico = np.flip(par)
  index = hash_table.busca(simetrico)
  if index != -1:
      par_simetrico = simetrico
      break
  else:
      hash_table.inserir(par)

if par_simetrico is not None:
    print(min(par_simetrico), max(par_simetrico))
else:
    print("nao existe par simetrico")


