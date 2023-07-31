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

    def existe_vertice(self, vertice):
        for v in self.vertices:
            if ((vertice.r == v.r) and (vertice.i == v.i)):
                return True
        return False

    # Exercício 4.1
    def subgrafo(self, vertices, arestas):
        sub_grafo = Grafo(1, len(vertices))

        for i, v in enumerate(vertices):
            if (self.existe_vertice(v)):
                sub_grafo.add_vertice(i, v.r)
            else:
                return print("Não é possivel criar um subgrafo com vertices que nao pertencem ao grafo")

            for a in arestas:
                if (self.verificar_vizinhos(a.v1, a.v2)):
                    if (a.v1 == v.i):
                        a.v1 = i
                    if (a.v2 == v.i):
                        a.v2 = i
                else:
                    return print("Não é possivel criar um subgrafo com arestas que nao pertencem ao grafo")

    
        for a in arestas:
            sub_grafo.add_aresta(a.v1, a.v2)
        
        return sub_grafo
        
    def subgrafo_induzido(self, vertices_s):
        sub_grafo = Grafo(1, len(vertices_s))

        for i, v in enumerate(vertices_s):
            if (self.existe_vertice(v)):
                sub_grafo.add_vertice(i, v.r)
            else:
                return print("Não é possivel criar um subgrafo com vertices que nao pertencem ao grafo")

        for a in self.arestas:
                if (self.verificar_vizinhos(a.v1, a.v2)):
                    if (a.v1 == v.i):
                        a.v1 = i
                    if (a.v2 == v.i):
                        a.v2 = i
                else:
                    return print("Não é possivel criar um subgrafo com arestas que nao pertencem ao grafo")
         
        for a in self.arestas:
            if(a.v1 == 1 and a.v2 == 1):
                sub_grafo.add_aresta(a.v1, a.v2)
        
        return sub_grafo

    # def subtrair(self, vertices_sub):
    #     sub_grafo = Grafo(1, len(vertices_sub))
        
    #     for i, v in enumerate(vertices_sub):
    #         if (self.existe_vertice(v) and v not in vertices_sub):
    #             sub_grafo.add_vertice(i, v.r)
    #         else:
    #             return print("Não é possivel criar um subgrafo com vertices que nao pertencem ao grafo")

    #     for a in self.arestas:
    #             if (self.verificar_vizinhos(a.v1, a.v2)):
    #                 if (a.v1 == v.i):
    #                     a.v1 = i
    #                 if (a.v2 == v.i):
    #                     a.v2 = i
    #             else:
    #                 return print("Não é possivel criar um subgrafo com arestas que nao pertencem ao grafo")
         
    #     for a in self.arestas:
    #         sub_grafo.add_aresta(a.v1, a.v2)
        
    #     return sub_grafo




def main():
    grafo = Grafo(1, 8)
    # Adicionar vértices
    grafo.add_vertice(0, "u")
    grafo.add_vertice(1, "v")
    grafo.add_vertice(2, "y")
    grafo.add_vertice(3, "x")
    grafo.add_vertice(4, "w")

    # Adicionar arestas
    grafo.add_aresta(0, 1) # a
    grafo.add_aresta(1, 4) # b
    grafo.add_aresta(3, 4) # c
    grafo.add_aresta(2, 3) # d
    grafo.add_aresta(0, 2) # e
    grafo.add_aresta(1, 2) # f
    grafo.add_aresta(1, 2) # g
    grafo.add_aresta(2, 4) # h

    # Exercício 4.6 a)
    # vertices_s = [Vertice(0, "u"), Vertice(1, "v"), 
    #               Vertice(2, "y"), Vertice(4, "w")]
    # arestas_s = [Aresta(0, 1), Aresta(1, 2), Aresta(2, 4)]
    # sub_grafo = grafo.subgrafo(vertices_s, arestas_s)

    # for vertice in sub_grafo.vertices:
    #     print(f"Vértice: Índice - {vertice.i} Rotulo - {vertice.r}")
    # for aresta in sub_grafo.arestas:
    #     print(f"Aresta ({aresta.v1}, {aresta.v2})")

    # Exercício 4.6 b)
    print('-=' * 20)
    vertices_g = [Vertice(0, "u"), Vertice(1, "v"), 
                  Vertice(2, "y"), Vertice(4, "w")]
    induzido = grafo.subgrafo_induzido(vertices_g)
    for vertice in induzido.vertices:
        print(f"Vértice: Índice - {vertice.i} Rotulo - {vertice.r}")
    for aresta in induzido.arestas:
        print(f"Aresta ({aresta.v1}, {aresta.v2})")

    # Exercício 4.6 c)
    # print('-=' * 20)
    # induzido = grafo.subgrafo_induzido(vertices_s)
    # for vertice in induzido.vertices:
    #     print(f"Vértice: Índice - {vertice.i} Rotulo - {vertice.r}")
    # for aresta in induzido.arestas:
    #     print(f"Aresta ({aresta.v1}, {aresta.v2})")

main()
