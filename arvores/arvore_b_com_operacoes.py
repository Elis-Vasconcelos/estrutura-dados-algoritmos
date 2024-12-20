class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t
      
    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k[0] < x.keys[i][0]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k[0] < x.keys[i][0]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k[0] > x.keys[i][0]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.leaf:
            z.child = y.child[t: 2 * t]
            y.child = y.child[0: t - 1]

    def print_tree(self, x, l=0):
        print("Level ", l, " ", len(x.keys), end=":")
        for i in x.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(x.child) > 0:
            for i in x.child:
                self.print_tree(i, l)

def main():
    B = BTree(3)

    for i in range(10):
        B.insert((i, 2 * i))

    B.print_tree(B.root)

    operacoes = []
    N = int(input())
    for i in range(N-1):
        linha = input()
        elementos = linha.split()
        operacao = int(elementos[0])
        valor = int(elementos[1])
        operacoes.append((operacao, valor))
    B = int(input())
    arvore = ArvoreB()
    for operacao, valor in operacoes:
        if operacao == 1:
            arvore.inserir(valor)
        elif operacao == 0:
            arvore.remover(valor)
    no, caminho = arvore.buscar(B)
    for no in caminho:
        print(" ".join(map(str, no.registros)))
    if no is not None:
        print(f"O valor {B} foi encontrado na árvore.")
    else:
        print(f"O valor {B} não foi encontrado na árvore.")


if __name__ == '__main__':
    main()