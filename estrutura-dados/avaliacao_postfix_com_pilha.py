class No:
    def __init__(self, v):
        self.valor = v
        self.prox = None

class Pilha:
    def __init__(self):
        self.topo = None

    def empilhar(self, n):
        if self.topo == None:
            self.topo = n
        else:
            n.prox = self.topo
            self.topo = n

    def desempilhar(self):
        if self.topo:
            temp = self.topo
            self.topo = self.topo.prox
            return temp

    def imprimir(self): 
        temp = self.topo
        while temp:
            print(f'{temp.valor}')
            temp = temp.prox
        

def main():
    p = Pilha() #Cria Pilha
  
    for i in input().split(): #Percorre os elementos
      
      #Se for operador pega os dois últimos números na pilha
      if i == "+" or i == "-" or i == "/" or i == "*":
        n1 = p.desempilhar()
        n2 = p.desempilhar()
        
        #Empilha o resultado da operação correspondente entre eles
        if i == "+":
          p.empilhar(No(int(n2.valor + n1.valor)))
        elif i == "-":
          p.empilhar(No(int(n2.valor - n1.valor)))
        elif i == "/":
          p.empilhar(No(int(n2.valor // n1.valor)))
        elif i == "*": 
          p.empilhar(No(int(n2.valor * n1.valor)))
          
      else: #Se for um número empilha ele
        p.empilhar(No(int(i)))
        
    p.imprimir() #Imprime resultado

if __name__ == "__main__":
    main()


