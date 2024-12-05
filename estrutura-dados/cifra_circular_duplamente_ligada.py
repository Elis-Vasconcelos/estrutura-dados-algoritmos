class No:
    def __init__(self, a, b):
        self.valor0 = a
        self.valor1 = b
        self.prox = self
        self.prev = self


class new_list:
    def __init__(self):
        self.inicio = None

    def display(self):
      if self.inicio is None:
          print("Lista vazia")
      else:
          temp = self.inicio.prox
          while temp != self.inicio:
              print(temp.imprimir(), end='')
              temp = temp.prox

    def append(self, n):
      if self.inicio is None:
        self.inicio = n
      else:
        n.prox = self.inicio
        n.prev = self.inicio.prev
        self.inicio.prev.prox = n
        self.inicio.prev = n
        

    def free_list(self):
        if self.inicio is None:
          print("Erro: Lista vazia")
        else:
          atual = self.inicio
          while atual.prox != self.inicio:
              temp = atual
              atual = atual.prox
              del temp
          del atual
          self.inicio = None

    def decripto(self, palavra_cripto, chave):
        saida = ""
        atual = self.inicio
        for i in range(len(palavra_cripto)):
          while palavra_cripto[i] != atual.valor0:
            atual = atual.prox
          for j in range(chave):
            atual = atual.prev
          saida += atual.valor1
          atual = self.inicio
        return saida

    def encripto(self, palavra_nao_cripto, chave):
        saida = ""
        atual = self.inicio
        for i in range(len(palavra_nao_cripto)):
          while palavra_nao_cripto[i] != atual.valor1:
            atual = atual.prox
          for j in range(chave):
            atual = atual.prox
          saida += atual.valor0
          atual = self.inicio
        return saida


def main():
  l = new_list()
  for i in range(26):
    a,b = input().split()
    l.append(No(a,b))

  chave = int(input())

  palavra_cripto = input()
  palavra_nao_cripto = input()

  print(l.decripto(palavra_cripto, chave))
  print(l.encripto(palavra_nao_cripto, chave))

if __name__ == "__main__":
    main() 











