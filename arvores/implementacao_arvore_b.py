import numpy as np

class Pagina:
    def __init__(self, m):
        self.n = 0
        self.m = m
        self.req = np.zeros(self.m*2+1, dtype=int)
        self.filho = np.zeros(self.m*2+1, dtype=object)
        self.folha = True

    def inserir_na_pag(self, valor):
        if self.n == 0:
            self.req[0] = valor
            self.n += 1
        else:
            for i in range(self.n):
                if valor < self.req[i]:
                    self.req[i+1:self.n+1] = self.req[i:self.n]
                    self.req[i] = valor
                    self.n += 1
                    break
            else:
                self.req[self.n] = valor
                self.n += 1 

    def insert_req(self, k):
        if self.folha:
            self.inserir_na_pag(k)
            if self.n > 2*self.m:
                return self.partir()
        else:
            i = 0
            while i < self.n and self.req[i] < k:
                i += 1
            if self.filho[i].n == 2*self.m:
                self.partir(i)
                if self.req[i] < k:
                    i += 1
            return self.filho[i].insert_req(k)

    def partir(self, i=None):
        nova_pag = Pagina(self.m)
      
        meio = ((2 * self.m + 1) // 2)
        nova_pag.req[:self.m] = self.req[meio+1:2*self.m+1]
        self.req[meio:2*self.m+1] = 0
        self.n = meio
      
        if True: 
            nova_pag.filho[:self.m+1] = self.filho[meio+1:2*self.m+2]
            self.filho[meio+1:2*self.m+2] = None
            nova_pag.folha = True
      
        if i is not None:
            self.filho[i+2:2*self.m+2] = self.filho[i+1:2*self.m+1]
            self.filho[i+1] = nova_pag
        return nova_pag, self.req[meio]

    def buscar(self, k, caminho=''):
      caminho += ' -> ' + str(self.req)
      i = 0
      while i < self.n and k > self.req[i]:
          i += 1
      if i < self.n and k == self.req[i]:
          print(caminho + ' -> Encontrado!')
          return True
      elif self.folha:
          print(caminho + ' -> Não encontrado')
          return False
      else:
          return self.filho[i].buscar(k, caminho)


    def remover(self, k):
      i = 0
      while i < self.n and k > self.req[i]:
          i += 1
      if i < self.n and k == self.req[i]:
          if self.folha:
              self.req[i:self.n-1] = self.req[i+1:self.n]
              self.req[self.n-1] = 0
              self.n -= 1
          else:
              if self.filho[i].n > self.m:
                  pred = self.filho[i].buscar_max()
                  self.req[i] = pred
                  self.filho[i].remover(pred)
              elif self.filho[i+1].n > self.m:
                  succ = self.filho[i+1].buscar_min()
                  self.req[i] = succ
                  self.filho[i+1].remover(succ)
              else:
                  self.filho[i].merge(i)
                  self.filho[i].remover(k)
      elif not self.folha:
          self.filho[i].remover(k)
    
    def buscar_max(self):
      if self.folha:
          return self.req[self.n - 1]
      else:
          return self.filho[self.n].buscar_max()

    def buscar_min(self):
      if not self.folha:
          return self.filho[0].buscar_min()
      else:
          return self.req[0]

class ArvoreB:
    def __init__(self, m):
        self.raiz = Pagina(m)

    def inserir(self, v):
      resultado = self.raiz.insert_req(v)
      if resultado is not None:
          nova_pag, req = resultado
          nova_raiz = Pagina(self.raiz.m)
          nova_raiz.folha = False
          nova_raiz.req[0] = req
          nova_raiz.filho[0] = self.raiz
          nova_raiz.filho[1] = nova_pag
          nova_raiz.n = 1
          self.raiz = nova_raiz

    def buscar(self, v):
        return self.raiz.buscar(v)

    def remover(self, v):
        self.raiz.remover(v)
        if self.raiz.n == 0 and not self.raiz.folha:
            self.raiz = self.raiz.filho[0]

def main():
    A = ArvoreB(1)
    N = int(input())
    for i in range(N-1):
        op, valor = map(int, input().split())
        if op == 1:
            A.inserir(valor)
        else:
            A.remover(valor)
    B = int(input())
    print(A.buscar(B))

if __name__ == "__main__":
    main()
