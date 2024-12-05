import string

class Elemento:
    def __init__(self, a, v):
        self.alfa = a
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
        temp = self.inicio
        while temp is not None:
            print(f"{temp.alfa} {temp.valor}")
            temp = temp.prox

    def ordem_term(self,max_exe_time,save_time):
        ordem_term = Fila()
        reenfileirar = Fila() 
        tempo_atual = 0
    
        while self.inicio is not None: 
            e = self.desenfileirar() 
    
            if e.valor <= max_exe_time:
                tempo_atual += e.valor
                e.valor = tempo_atual
                ordem_term.enfileirar(e)
            else:
                tempo_atual += max_exe_time + save_time
                e.valor -= max_exe_time
                reenfileirar.enfileirar(e) 
    
        while reenfileirar.inicio is not None: 
            e = reenfileirar.desenfileirar() 
    
            if e.valor <= max_exe_time:
                tempo_atual += e.valor
                e.valor = tempo_atual
                ordem_term.enfileirar(e)
            else:
                tempo_atual += max_exe_time + save_time
                e.valor -= max_exe_time
                reenfileirar.enfileirar(e)
    
        return ordem_term


def main():
    f = Fila()
    max_exe_time, save_time = map(int, input().split())

    j = 0
    for i in input().split():
        f.enfileirar(Elemento(string.ascii_uppercase[j], int(i)))
        j += 1

    ordem = f.ordem_term(max_exe_time, save_time)
    ordem.imprimir()


if __name__ == "__main__":
    main()