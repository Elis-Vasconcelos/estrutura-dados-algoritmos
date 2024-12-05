class No:
  def __init__(self, v):
      self.valor = int(v)
      self.esq = None
      self.dir = None

class new_tree:
  def __init__(self):
      self.raiz = None

  def add(self, valor):
      if self.raiz is None:
          self.raiz = No(valor)
      else:
          self._add(valor, self.raiz)

  def _add(self, valor, r):
      if valor < r.valor:
          if r.esq is None:
              r.esq = No(valor)
          else:
              self._add(valor, r.esq)
      else:
          if r.dir is None:
              r.dir = No(valor)
          else:
              self._add(valor, r.dir)

  def clear_tree(self):
    self.raiz = None

  def busca(self, r, k):
      x = r
      while x is not None and k != x.valor:
        x = x.esq if k < x.valor else x.dir
      return x
    
  def preordem(self, r):
    if r:
        print(f'{r.valor}')
        self.preordem(r.esq)
        self.preordem(r.dir)

  def ancestral_comum_mais_proximo(self, X, Y):
      res_X = self.busca(self.raiz,X)
      res_Y = self.busca(self.raiz,Y)
      if res_X and res_Y:
        x = self.raiz
        while x is not None:
            if X < x.valor and Y < x.valor:
                x = x.esq
            elif X > x.valor and Y > x.valor:
                x = x.dir
            else:
                return x.valor
      elif res_X and res_Y is None:
          return X
      elif res_Y and res_X is None:
          return Y
      else:
          return "NENHUM"

def main():
  A = new_tree()
  N = int(input())
  for i in input().split():
    A.add(int(i))
  X, Y = map(int,input().split())
  print(A.ancestral_comum_mais_proximo(X, Y))

if __name__ == "__main__":
  main()
