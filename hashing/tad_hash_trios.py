import numpy as np
import math as mt

class No:
  def __init__(self, v):
      self.valor = v
      self.prox = None
      self.prev = None

  def imprimir(self):
    return (f"{self.valor} ")

class Lista:
  def __init__(self):
      self.inicio = None
      self.fim = None

  def imprimir(self):
    if self.inicio is None:
        print("Lista vazia")
    else:
        temp = self.inicio
        while temp is not None:
            print(temp.imprimir(), end='')
            temp = temp.prox
        print("\n", end='')

  def append(self, n):
    if self.inicio is None:
      self.inicio = n
      self.fim = n
    else:
      self.fim.prox = n
      n.prev = self.fim
      self.fim = n

  def inserir(self, n):
      if self.inicio is None:
          self.inicio = n
          self.fim = n
      else:
          n.prox = self.inicio
          self.inicio.prev = n
          self.inicio = n

class TADHash:
  def __init__(self, m):
      self.m = m
      self.hashing = np.zeros(self.m, dtype=Lista)
      self.trios = 0

      for i in range(m):
          self.hashing[i] = Lista()

  def insert(self, v):
    x = 0
    idx = mt.floor(self.m * ((v * 0.17) % 1))
    while True:
        idx += x
        if self.hashing[idx].inicio:
            if v == self.hashing[idx].inicio.valor:
                self.hashing[idx].inserir(No(v))
                if self.hashing[idx].inicio.prox.prox:
                  self.trios += 1
                return
            x += 1
        else: 
            self.hashing[idx].inserir(No(v))
            break

def main():
  N = int(input())
  tadhash = TADHash(N)

  for i in input().split():
    tadhash.insert(int(i))

  for i in range(tadhash.m):
    print(f"***Posicao: {i}")
    tadhash.hashing[i].imprimir()

  print(tadhash.trios)

if __name__ == "__main__":
  main()