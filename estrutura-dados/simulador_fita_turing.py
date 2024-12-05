class No:
    def __init__(self, v, d):
        if v == 'b':
          v = ''
        self.valor = v
        self.direcao = d
        self.prox = None
        self.prev = None

    def imprimir(self):
      return (f"{self.valor}")

    def imprimir(self):
        return(f"{self.valor}")

    def __str__(self):
        return str(self.valor)

    def __repr__(self):
        return f"No({self.valor})"

class new_list:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.ponteiro = self.inicio

    def display(self):
      if self.inicio is None:
          print("Lista vazia")
      else:
          temp = self.inicio
          while temp is not None:
              print(temp.imprimir(), end='')
              temp = temp.prox

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

  
    def escrever(self,n):
          self.ponteiro.valor = n.valor
          if n.direcao == 'D':
            if self.ponteiro == self.fim:
              self.append(No('',''))
              self.ponteiro = self.fim
            else:
              self.ponteiro = self.ponteiro.prox
          elif n.direcao == 'E':
            if self.ponteiro == self.inicio:
              self.inserir(No('',''))
              self.ponteiro = self.inicio
            else:
              self.ponteiro = self.ponteiro.prev
            
def main():
  fita = new_list()
  for i in input():
    fita.append(No(i,''))
  fita.ponteiro = fita.inicio
  
  N = int(input())

  for i in range(N):
    e,d = input().split()
    fita.escrever(No(e,d))
    
  fita.display()

if __name__ == "__main__":
    main() 








