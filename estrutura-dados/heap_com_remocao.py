class Elemento:
  def __init__(self, v):
      self.valor = v
      self.prox = None

class Fila:
  def __init__(self):
      self.inicio = None
      self.fim = None

  def enfileirar(self, n):
      if self.inicio is None:
          self.inicio = n
          self.fim = n
      else:
          self.fim.prox = n
          self.fim = n
          n.prox = None

  def desenfileirar(self):
      if self.inicio:
          temp = self.inicio
          self.inicio = self.inicio.prox
          if self.inicio is None:
              self.fim = None
          return temp

  def imprimir(self):
      print("Imprimindo fila...")
      temp = self.inicio
      while temp is not None:
          print(f"{temp.valor.valor}")
          temp = temp.prox

class No:
    def __init__(self, o, v):
        self.ordem = o
        self.valor = v
        self.esq = None
        self.dir = None
        self.pai = None

class Heap:
    def __init__(self):
        self.raiz = None

    def inserir(self, n):
        if self.raiz == None:
            self.raiz = n
        else:
            self.inserir_subarvore(self.raiz, n)

    def inserir_subarvore(self, r, n):
        f = Fila()
        f.enfileirar(Elemento(r))
        procurar = True
        while procurar:
            raiz_temp = (f.desenfileirar()).valor
            if raiz_temp.esq:
                f.enfileirar(Elemento(raiz_temp.esq))
                if raiz_temp.dir:
                    f.enfileirar(Elemento(raiz_temp.dir))
                else: # se direita eh None
                    raiz_temp.dir = n
                    n.pai = raiz_temp
                    self.fix_up(n)
                    procurar = False
            else: # se esquerda eh None
                raiz_temp.esq = n
                n.pai = raiz_temp
                self.fix_up(n)
                procurar = False

    def fix_up(self, n):
        if n.pai and n.valor < n.pai.valor:
          temp, _temp = n.pai.valor, n.pai.ordem
          n.pai.valor, n.pai.ordem = n.valor, n.ordem
          n.valor, n.ordem = temp, _temp
          self.fix_up(n.pai)

    def fix_down(self, n):
        filho = None
        if n.esq and (not n.dir or n.esq.valor < n.dir.valor):
              filho = n.esq
        elif n.dir:
            filho = n.dir
        if filho and n.valor > filho.valor:
          n.valor, filho.valor = filho.valor, n.valor
          n.ordem, filho.ordem = filho.ordem, n.ordem
          self.fix_down(filho)


    def remover_raiz(self,n):
      f = Fila()
      f.enfileirar(Elemento(self.raiz))
      g = f.inicio
      for i in range(n):
          raiz_temp = g.valor
          if raiz_temp.esq:
              f.enfileirar(Elemento(raiz_temp.esq))
              if raiz_temp.dir:
                  f.enfileirar(Elemento(raiz_temp.dir))
          g = g.prox
      f.imprimir()
      print("Final:")
      print(f.fim.valor.valor)
      nova_raiz = f.fim.valor
      if nova_raiz == nova_raiz.pai.esq:
        nova_raiz.pai.esq = None
      else:
        nova_raiz.pai.dir = None
      nova_raiz.pai = None
      if self.raiz.esq:
        self.raiz.esq.pai = nova_raiz
        nova_raiz.esq = self.raiz.esq
        self.raiz.esq = None
      if self.raiz.dir:
        self.raiz.dir.pai = nova_raiz
        nova_raiz.dir = self.raiz.dir
        self.raiz.dir = None
      self.raiz = nova_raiz
      self.fix_down(self.raiz)

    def preordem(self, r):
        if r:
            print(f"{r.ordem} {r.valor} ")
            self.preordem(r.esq)
            self.preordem(r.dir)

def main():
  h = Heap()
  N, Q = map(int,input().split())
  k = 1
  for i in range(N):
    ordem, valor = input().split()
    h.inserir(No(ordem,int(valor)))
    if (i+1) == (k * Q):
      print("Antes:")
      h.preordem(h.raiz)
      h.remover_raiz(i+1-(k-1))
      print("Depois:")
      h.preordem(h.raiz)
      k += 1
  print("Resultado:")
  h.preordem(h.raiz)


if __name__ == "__main__":
    main()
