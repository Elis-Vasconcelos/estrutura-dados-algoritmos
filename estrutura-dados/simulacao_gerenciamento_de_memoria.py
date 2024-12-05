class No:
    def __init__(self, a, b, c):
        self.uso = a
        self.mem = b
        self.id = c
        self.prox = None

    def imprimir(self):
        return(f"{self.id}")

class new_list:
    def append(self, n):
        if self.inicio is None:
          self.inicio = n
          self.fim = n
        else:
          self.fim.prox = n
          self.fim = n
  
    def __init__(self,tam):
        self.inicio = None
        self.fim = None
        self.append(No(0,tam,"mem_livre"))
        

    def imprimir(self):
        if self.inicio == None:
            print("Lista vazia")
        else:
            output = ""
            temp = self.inicio
            while temp is not None:
              if temp.uso == 0 and temp.mem != 0:
                if output == "" or output[len(output)-1] != "0":
                    output += "0"
              elif temp.uso == 1:
                output += (f"{temp.imprimir()}")
              temp = temp.prox  
            for i in output:
              print(f"{i}", end=" ")

    def inserir(self, n):
        if self.inicio is None:
            self.inicio = n
            self.fim = n
        else:
            n.prox = self.inicio
            self.inicio = n

    def remover_anterior(self,anterior,atual):
        temp = self.inicio
        while temp.prox is not anterior:
          temp = temp.prox
        temp.prox = atual
        del anterior

    def gerenciar_mem(self, e):
        if e.uso == 1:
          if self.inicio is None:
            self.append(e)
          else:
            anterior = None
            atual = self.inicio
            while atual is not None:
              if atual.uso == 0 and atual.mem >= e.mem:
                if anterior is None:
                  self.inserir(e)
                  atual.mem -= e.mem
                  break
                else:
                  e.prox = atual
                  anterior.prox = e
                  atual.mem -= e.mem
                  break
              anterior = atual
              atual = atual.prox     
        if e.uso == 0:
          anterior = None
          atual = self.inicio
          while atual is not None:
            if e.id == atual.id:
              atual.uso = 0
              if atual == self.inicio and atual.prox.uso == 0:
                atual.prox.mem += atual.mem
                atual.mem = 0
                self.inicio = atual.prox
              elif atual == self.fim and anterior.uso == 0:
                atual.mem += anterior.mem
                anterior.mem = 0
                self.remover_anterior(anterior,atual)
                self.fim = atual
              else: 
                if anterior is not None and anterior.uso == 0:
                  atual.mem += anterior.mem
                  anterior.mem = 0
                  self.remover_anterior(anterior,atual)
                elif atual.prox is not None and atual.prox.uso == 0:
                  atual.prox.mem += atual.mem
                  atual.mem = 0
                  self.remover_anterior(atual,atual.prox)
            atual = atual.prox

    def calc_mem_usada(self):
      mem_usada = 0
      atual = self.inicio
      while atual is not None:
        if atual.uso == 1:
          mem_usada += atual.mem
        atual = atual.prox
      return mem_usada
              

def main():
    tam_mem, n = map(int,input().split())
  
    l = new_list(tam_mem)
    for i in range(n):
      a,b,c = input().split()
      e = No(int(a),int(b),c)
      l.gerenciar_mem(e)

    l.imprimir()
    mem_usada = l.calc_mem_usada()
    print(f"\n{mem_usada}")
    print(f"{tam_mem - mem_usada}")

if __name__ == "__main__":
    main()











