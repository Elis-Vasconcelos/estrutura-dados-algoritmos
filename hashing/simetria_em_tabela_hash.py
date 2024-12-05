import numpy as np
import math as mt

class No:
  def __init__(self, v, b):
      self.valor1 = v
      self.valor2 = b
      self.prox = None
      self.prev = None

  def imprimir(self):
    return (f"{self.valor1} {self.valor2} ")

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
      self.par_simetrico = False

      for i in range(m):
          self.hashing[i] = Lista()

  def insert(self, v, b):
    x = 0
    while True:
        idx = mt.floor(self.m * (((v * b) * 0.61) % 1)) + x
        if self.hashing[idx].inicio:
            comp = self.hashing[idx].inicio
            if v == comp.valor2 and b == comp.valor1:
                self.hashing[idx].inserir(No(v,b))
                if v < b:
                 print(f"{v} {b}")
                else:
                 print(f"{b} {v}")
                self.par_simetrico = True
                return
            x += 1
        else: 
            self.hashing[idx].inserir(No(v,b))
            break

def main():
  N = int(input())
  tadhash = TADHash(N)

  for i in range(N):
    v,b = input().split()
    tadhash.insert(int(v),int(b))

  for i in range(tadhash.m):
    print(f"***Posicao: {i}")
    tadhash.hashing[i].imprimir()

  if tadhash.par_simetrico is False:
    print("nao existe par simetrico")

if __name__ == "__main__":
  main()
