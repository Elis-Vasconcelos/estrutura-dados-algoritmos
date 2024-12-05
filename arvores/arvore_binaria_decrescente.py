class No:
  def __init__(self, v):
      self.valor = int(v)
      self.esq = None
      self.dir = None
      self.pai = None

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
              n = No(valor)
              r.esq = n
              n.pai = r
          else:
              self._add(valor, r.esq)
      else:
          if r.dir is None:
              n = No(valor)
              r.dir = n
              n.pai = r
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

  def tree_minimum(self,r):
    while r.esq is not None:
      r = r.esq
    return r

  def tree_maximum(self, r):
    while r.dir is not None:
      r = r.dir
    return r

  def transplantar(self, u, v):
    if u.pai is None:
      self.raiz = v
    elif u == u.pai.esq:
      u.pai.esq = v
    else:
      u.pai.dir = v
    if v is not None:
      v.pai = u.pai
  
  def remover(self, z):
    if z.esq is None:
      self.transplantar(z,z.dir)
    elif z.dir is None:
      self.transplantar(z,z.esq)
    else:
      y = self.tree_minimum(z.dir)
      if y.pai != z:
        self.transplantar(y,y.dir)
        y.dir = z.dir
        y.dir.pai = y
      self.transplantar(z,y)
      y.esq = z.esq
      y.esq.pai = y

  def tree_predecessor(self, x): 
    if x.esq is not None:
      return self.tree_maximum(x.esq) 
    y = x.pai
    while y is not None and x == y.esq: 
      x = y
      y = y.pai
    return y

  def print_decres(self):
    s = ""
    r = self.tree_maximum(self.raiz)
    while r is not None:
      s += (f"{r.valor} ")
      temp = r
      r = self.tree_predecessor(r)
      self.remover(temp)
    return print(s)

def main():
  A = new_tree()
  int(input())
  for i in input().split():
    A.add(int(i))
  A.print_decres()

if __name__ == "__main__":
  main()
