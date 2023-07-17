# Exercício 3.3 1/2 
class Vertice:
    def __init__(self, i, r):
        # i -> indice | r -> rotulo
        self.i = i
        self.r = r
        self.grau = 0
        self.prof_ent = None
        self.prof_sai = None

class Aresta:
    # v1 e v2 -> vertice
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class Grafo:
    def __init__(self, tipo, tamanho_max):  
        # Tipo: 0 -> Matriz | 1 -> Estrutura
        self.tipo = tipo
        self.tamanho_max = tamanho_max
        self.vertices = []
        self.arestas = []
        self.arestas_arvore = [] 
        self.arestas_retorno = []

        if self.tipo == 0:
            self.matriz = [[0] * tamanho_max for _ in range(tamanho_max)]
        elif self.tipo == 1:
            self.estrutura = {}

    def add_vertice(self, i, r):
        # i -> indice | r -> rotulo
        vertice = Vertice(i, r)
        self.vertices.append(vertice)

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

    def calcular_grau(self, i_v):
        # i_v -> indice do vertice
        if self.tipo == 0:
            return self.vertices[i_v].grau
        elif self.tipo == 1:
            if i_v in self.estrutura:
                return self.vertices[i_v].grau
            else:
                return 0

    def verificar_vizinhos(self, i_v1, i_v2):
        # i_v1 e i_v2 -> indice do vertice
        if self.tipo == 0:
            return self.matriz[i_v1][i_v2] == 1
        elif self.tipo == 1:
            if i_v1 in self.estrutura:
                return i_v2 in self.estrutura[i_v1]
            else:
                return False

    def imprimir_grafo(self):
        self.estrutura = dict(sorted(self.estrutura.items()))
        # r -> rotulo | adj -> adjacência
        print('-=' * 20)
        print("Numero de vertices:", len(self.vertices))
        print('-=' * 20)
        print("Numero de arestas:", len(self.arestas))
        print('-=' * 20)

        print("Grau total dos vertices:", end=' ')
        grau_tot = 0
        for v in self.vertices:
            grau_tot += v.grau
        print(grau_tot)
        print('-=' * 20)

        grau_par = grau_impar = 0
        for v in self.vertices:
            if (v.grau % 2 == 0):
                grau_par +=1
            else:
                grau_impar +=1
        print("Numero de vertices de grau impar:", grau_impar)
        print('-=' * 20)
        print("Numero de vertices de grau par:", grau_par)
        print('-=' * 20)

        if self.tipo == 0:
            print("Matriz de arestas:")
            for n in range(len(self.matriz)):
                for c in range(len(self.matriz)):
                    print(f'{self.matriz[n][c]:^3}', end='')
                print()
        elif self.tipo == 1:
            print("Estrutura de arestas:")
            for i in self.estrutura:
                r = self.vertices[i].r
                adj_r = []
                for v in self.estrutura[i]:
                    if self.vertices[v].r not in adj_r:
                        adj_r.append(self.vertices[v].r)
                print(f"{r}: {adj_r}")
        print('-=' * 20)
        print("Grau de cada vertice:")
        for vertice in self.vertices:
            print(f"{vertice.r}: {self.calcular_grau(vertice.i)}")
        print('-=' * 20)

    def gerar_grafo_completo(self, n):
        for i in range(n):
            self.add_vertice(i, "V" + str(i))
        for v1 in range(n):
            for v2 in range(v1+1, n):
                self.add_aresta(v1, v2)

    def gerar_grafo_k_regular(self, n, k):
        if (((n * k) % 2 != 0) or (k >= n)):
            print(f"Nao e possivel criar um grafo k-regular com n = {n} e k = {k}")
        else:
            for i in range(n):
                self.add_vertice(i, "V" + str(i))

            for v1 in range(n):
                for v2 in range(n-1, -1, -1):
                    if ((v1 != v2) and (self.verificar_vizinhos(v1, v2) == False) and (self.calcular_grau(v1) < k) and (self.calcular_grau(v2) < k)):
                        self.add_aresta(v1, v2)

            self.estrutura = dict(sorted(self.estrutura.items()))
            if (len(self.arestas) != (n * k)/2):
                self.estrutura = {}
                self.vertices = []
                self.arestas = []
                print(f"Nao e possivel criar um grafo k-regular com n = {n} e k = {k}")

    def verificar_bipartidos(self, x, y):
        for v in self.vertices:
            if v.i in x:
                vizinhos = self.estrutura.get(v.i, [])
                for v2 in vizinhos:
                    if v2 in x:
                        return False
            elif v.i in y:
                vizinhos = self.estrutura.get(v.i, [])
                for v2 in vizinhos:
                    if v2 in y:
                        return False
        return True

    # Exercício 3.1 
    def busca_em_profundidade(self, v_i): # v_i -> vertice inicial
        if (self.verificar_grafo_simples_e_conexo()):
            v_vi = set() # v_vi -> vertices visitados
            l_v = [] # l_v -> lista de vertices
            self.busca_em_profundidade_recursiva(v_i, v_vi, l_v)

            for a in self.arestas:
                if (a not in self.arestas_arvore and a not in self.arestas_retorno):
                    self.arestas_retorno.append(a)

            # print("Busca em Profundidade:")
            # for v in l_v:
            #     print(self.vertices[v].r, end=" ")

            # print("\nArestas da árvore:")
            # for aresta in self.arestas_arvore:
            #     print(f"{aresta.v1} - {aresta.v2}")
            
            # print("Arestas de retorno:")
            # for aresta in self.arestas_retorno:
            #     print(f"{aresta.v1} - {aresta.v2}")
        else:
            print("A busca em profundidade nao pode ser realizada nesse grafo")   

    # Exercício 3.2 
    def busca_em_profundidade_recursiva(self, v, v_vi, l_v):
        v_vi.add(v)
        l_v.append(v)

        for a in self.arestas:  # a -> aresta
            if a.v1 == v and a.v2 not in v_vi:
                if (a not in self.arestas_arvore):
                    self.arestas_arvore.append(a)
                self.busca_em_profundidade_recursiva(a.v2, v_vi, l_v)
            elif a.v2 == v and a.v1 not in v_vi:
                if (a not in self.arestas_arvore):
                    self.arestas_arvore.append(a)
                self.busca_em_profundidade_recursiva(a.v1, v_vi, l_v)
    
    def verificar_grafo_simples_e_conexo(self):
        if len(self.vertices) == 0:
            return False

        for aresta in self.arestas:
            if aresta.v1 == aresta.v2:
                return False

        v_vi = set()
        l_v = []
        self.busca_em_profundidade_recursiva(0, v_vi, l_v)

        return len(v_vi) == len(self.vertices)

# Exercício 3.4 
def main():
    grafo = Grafo(1, 8)

    # Adicionar vértices
    grafo.add_vertice(0, "a")
    grafo.add_vertice(1, "b")
    grafo.add_vertice(2, "c")
    grafo.add_vertice(3, "d")
    grafo.add_vertice(4, "e")
    grafo.add_vertice(5, "f")
    grafo.add_vertice(6, "g")
    grafo.add_vertice(7, "h")

    # Adicionar arestas
    grafo.add_aresta(0, 1)
    grafo.add_aresta(0, 2)
    grafo.add_aresta(0, 4)
    grafo.add_aresta(0, 5)
    grafo.add_aresta(1, 3)
    grafo.add_aresta(1, 4)
    grafo.add_aresta(2, 5)
    grafo.add_aresta(2, 6)
    grafo.add_aresta(2, 7)
    grafo.add_aresta(5, 6)
    grafo.add_aresta(5, 7)
    grafo.add_aresta(6, 7)

    # Realizar busca em profundidade a partir do vértice 0
    grafo.imprimir_grafo()
    grafo.busca_em_profundidade(0)

main()