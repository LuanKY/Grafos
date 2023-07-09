# Exercício 1.3 1/2
class Vertice:
    def __init__(self, i, r):
        # i -> indice | r -> rotulo
        self.i = i
        self.r = r
        self.grau = 0

class Aresta:
    # v1 e v2 -> vertice
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class Grafo:
    # Exercício 1.1 e 1.2
    def __init__(self, tipo, tamanho_max):  
        # Tipo: 0 -> Matriz | 1 -> Estrutura
        self.tipo = tipo
        self.tamanho_max = tamanho_max
        self.vertices = []
        self.arestas = []

        if self.tipo == 0:
            self.matriz = [[0] * tamanho_max for _ in range(tamanho_max)]
        elif self.tipo == 1:
            self.estrutura = {}

    # Exercício 1.3 2/2
    def add_vertice(self, i, r):
        # i -> indice | r -> rotulo
        vertice = Vertice(i, r)
        self.vertices.append(vertice)

    # Exercício 1.4 1/2
    def add_aresta(self, i_v1, i_v2):
        # i_v1 e i_v2 -> indice do vertice
        if self.tipo == 0:
            self.matriz[i_v1][i_v2] = 1
            self.matriz[i_v2][i_v1] = 1
        elif self.tipo == 1:
            if i_v1 not in self.estrutura:
                self.estrutura[i_v1] = []
            if i_v2 not in self.estrutura:
                self.estrutura[i_v2] = []

            self.estrutura[i_v1].append(i_v2)
            self.estrutura[i_v2].append(i_v1)

        aresta = Aresta(i_v1, i_v2)
        self.arestas.append(aresta)
        self.vertices[i_v1].grau += 1
        self.vertices[i_v2].grau += 1

    # Exercício 1.4 2/2
    def remove_aresta(self, i_v1, i_v2):
        # i_v1 e i_v2 -> indice do vertice
        if self.tipo == 0:
            self.matriz[i_v1][i_v2] = 0
            self.matriz[i_v2][i_v1] = 0
        elif self.tipo == 1:
            if i_v1 in self.estrutura:
                if i_v2 in self.estrutura[i_v1]:
                    self.estrutura[i_v1].remove(i_v2)
            if i_v2 in self.estrutura:
                if i_v1 in self.estrutura[i_v2]:
                    self.estrutura[i_v2].remove(i_v1)

        # a -> aresta
        arestas = []
        for a in self.arestas:
            if not ((a.v1 == i_v1 and a.v2 == i_v2) or (a.v1 == i_v2 and a.v2 == i_v1)):
                arestas.append(a)
        self.arestas = arestas

        self.vertices[i_v1].grau -= 1
        self.vertices[i_v2].grau -= 1

    # Exercício 1.5
    def calcular_grau(self, i_v):
        # i_v -> indice do vertice
        if self.tipo == 0:
            return self.vertices[i_v].grau
        elif self.tipo == 1:
            if i_v in self.estrutura:
                return self.vertices[i_v].grau
            else:
                return 0

    # Exercício 1.6
    def verificar_vizinhos(self, i_v1, i_v2):
        # i_v1 e i_v2 -> indice do vertice
        if self.tipo == 0:
            return self.matriz[i_v1][i_v2] == 1
        elif self.tipo == 1:
            if i_v1 in self.estrutura:
                return i_v2 in self.estrutura[i_v1]
            else:
                return False

    # Exercício 1.7
    def imprimir_grafo(self):
        # r -> rotulo | adj -> adjacência
        print('-=' * 20)
        print("Número de vértices:", len(self.vertices))
        print('-=' * 20)
        print("Número de arestas:", len(self.arestas))
        print('-=' * 20)

        if self.tipo == 0:
            print("Matriz de adjacência:")
            for n in range(len(self.matriz)):
                for c in range(len(self.matriz)):
                    print(f'{self.matriz[n][c]:^3}', end='')
                print()
        elif self.tipo == 1:
            print("Estrutura de adjacência:")
            for i in self.estrutura:
                r = self.vertices[i].r
                adj_r = []
                for v in self.estrutura[i]:
                    if self.vertices[v].r not in adj_r:
                        adj_r.append(self.vertices[v].r)
                print(f"{r}: {adj_r}")
        print('-=' * 20)
        print("Grau de cada vértice:")
        for vertice in self.vertices:
            print(f"{vertice.r}: {self.calcular_grau(vertice.i)}")
        print('-=' * 20)


# Exercício 1.8 1/2
# Grafo 1 usando Matriz de Adjacência
def grafoM():
    grafo = Grafo(0, 5)

    grafo.add_vertice(0, "V1")
    grafo.add_vertice(1, "V2")
    grafo.add_vertice(2, "V3")
    grafo.add_vertice(3, "V4")
    grafo.add_vertice(4, "V5")

    grafo.add_aresta(0, 1)
    grafo.add_aresta(1, 2)
    grafo.add_aresta(1, 3)
    grafo.add_aresta(1, 4)
    grafo.add_aresta(1, 4)
    grafo.add_aresta(2, 2)
    grafo.add_aresta(2, 3)
    grafo.add_aresta(3, 4)

    print("Grafo 1:")
    grafo.imprimir_grafo()

# Exercício 1.8 2/2
# Grafo 2 usando Estrutura de Adjacência
def grafoE():
    grafo = Grafo(1, 5)

    grafo.add_vertice(0, "V1")
    grafo.add_vertice(1, "V2")
    grafo.add_vertice(2, "V3")
    grafo.add_vertice(3, "V4")
    grafo.add_vertice(4, "V5")

    grafo.add_aresta(0, 1)
    grafo.add_aresta(0, 2)
    grafo.add_aresta(0, 3)
    grafo.add_aresta(0, 4)
    grafo.add_aresta(1, 2)
    grafo.add_aresta(1, 3)
    grafo.add_aresta(1, 4)
    grafo.add_aresta(2, 3)
    grafo.add_aresta(2, 4)
    grafo.add_aresta(3, 4)

    print("Grafo 2:")
    grafo.imprimir_grafo()


grafoM()
grafoE()