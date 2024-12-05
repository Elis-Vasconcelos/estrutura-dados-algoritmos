class No:

  def __init__(self, v):
    self.valor = v
    self.prox = None

  def imprimir(self):
    return (f"{self.valor}")


class new_list:
  def __init__(self):
    self.inicio = None
    self.fim = None

  def append(self, n):
    if self.inicio is None:
      self.inicio = n
      self.fim = n
    else:
      self.fim.prox = n
      self.fim = n

  def detectar_plagio(self, plagio):
    pos = 0
    atual = self.inicio
    plagio_atual = plagio.inicio
    encontrei = self.inicio
    verificando = False
    while atual is not None and plagio_atual is not None:
      if atual.valor == plagio_atual.valor:
        if verificando is False:
          encontrei = atual
        verificando = True
        if plagio_atual.prox is None:
          return (f"Plagio encontrado na posicao {pos}!")
        atual = atual.prox
        plagio_atual = plagio_atual.prox
        continue
      else:
        if verificando is True:
          atual = encontrei
        pos += 1
        plagio_atual = plagio.inicio
        verificando = False
      atual = atual.prox
    return "Nenhum plagio detectado!"


def main():
  p = new_list()
  for i in input():
    p.append(No(i))

  l = new_list()
  for i in input():
    l.append(No(i))

  print(l.detectar_plagio(p))


if __name__ == "__main__":
  main()
