import copy

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

    def remove_vertice(self, i_v):
        # i_v -> indice do vertice
        if ((i_v >= len(self.vertices) and i_v not in self.estrutura) or i_v < 0):
            return print("Índice inválido. O índice do vértice não existe no grafo.")

        arestas = []
        for a in self.arestas:
            if (not (a.v1 == i_v or a.v2 == i_v)):
                arestas.append(a)
        self.arestas = arestas

        if i_v in self.estrutura:
            adjacentes = self.estrutura[i_v]
            for adj in adjacentes:
                self.estrutura[adj].remove(i_v)
            del self.estrutura[i_v]
        
        i = 0
        while i < len(self.vertices):
            v = self.vertices[i]
            v.grau = 0
            for a in self.arestas:
                if (a.v1 == v.i or a.v2 == v.i):
                    v.grau += 1     
            if (v.i == i_v):
                self.vertices.remove(v)
                i -= 1
            i += 1

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

        if (self.vertices[-1].i == len(self.vertices) - 1): #Grafo Normal
            self.vertices[i_v1].grau += 1
            self.vertices[i_v2].grau += 1
        else: #Subgrafo Induzido
            for i, v in enumerate(self.vertices):
                if (v.i == i_v1):
                    self.vertices[i].grau += 1
                if (v.i == i_v2):
                    self.vertices[i].grau += 1

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
        removed = False
        for a in self.arestas:
            if (a.v1 == i_v1 and a.v2 == i_v2) or (a.v1 == i_v2 and a.v2 == i_v1):
                if not removed:
                    removed = True
                    continue
            arestas.append(a)
        self.arestas = arestas

        self.vertices[i_v1].grau -= 1
        self.vertices[i_v2].grau -= 1

    def calcular_grau(self, i_v):
        # i_v -> indice do vertice
        if self.tipo == 0:
            return self.vertices[i_v].grau
        elif self.tipo == 1:
            if ((i_v in self.estrutura) or (self.vertices[i_v].grau > 0)):
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


            if (self.vertices[-1].i == len(self.vertices) - 1): #Grafo Normal
                for i in self.estrutura:
                    r = self.vertices[i].r
                    adj_r = []
                    for v in self.estrutura[i]:
                        if self.vertices[v].r not in adj_r:
                            adj_r.append(self.vertices[v].r)
                    print(f"{r}: {adj_r}")
            else: #Subgrafo Induzido
                for i, e in enumerate(self.estrutura):
                    r = self.vertices[i].r
                    adj_r = []
                    
                    for e2 in self.estrutura[e]:
                        for v in self.vertices:
                            if ((v.i == e2) and (v.r not in adj_r)):
                                adj_r.append(v.r)
                    print(f"{r}: {adj_r}")
            
        print('-=' * 20)
        print("Grau de cada vertice:")
        for i, vertice in enumerate(self.vertices):
            print(f"{vertice.r}: {self.calcular_grau(i)}")
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

    def busca_em_profundidade(self, v_i): # v_i -> vertice inicial
        if (self.verificar_grafo_simples_e_conexo()):
            v_vi = set() # v_vi -> vertices visitados
            l_v = [] # l_v -> lista de vertices
            self.busca_em_profundidade_recursiva(v_i, v_vi, l_v)

            for a in self.arestas:
                if (a not in self.arestas_arvore and a not in self.arestas_retorno):
                    self.arestas_retorno.append(a)

            print("Busca em Profundidade:")
            for p, v in enumerate(l_v, start=1):
                print(self.vertices[v].r, end=" ")
                self.vertices[v].prof_ent = p
            print()
        else:
            print("A busca em profundidade nao pode ser realizada nesse grafo")   

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
        
        l_p = []  #lista de profundidade
        for p in self.vertices:
            l_p.append(p.prof_sai)
        
        l_p.sort(key=lambda x: -float('inf') if x is None else x)

        if (l_p[-1] == None):
            self.vertices[v].prof_sai = 1
        elif (v in v_vi and self.vertices[v].prof_sai == None):
            self.vertices[v].prof_sai = (l_p[-1]) +1
    
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

    # Exercício 4.2
    def subgrafo_induzido(self, vertices):
        sub_grafo = Grafo(1, len(vertices))

        for i, v in enumerate(vertices):
            if (self.existe_vertice(v)):
                sub_grafo.add_vertice(v.i, v.r)
            else:
                return print("Não é possivel criar um subgrafo com vertices que nao pertencem ao grafo")

        for a in self.arestas:
            i_v1 = i_v2 = -1

            for v in sub_grafo.vertices:
                if (a.v1 == v.i):
                    i_v1 = v.i
                if (a.v2 == v.i):
                    i_v2 = v.i

            if (i_v1 != -1 and i_v2 != -1):
                sub_grafo.add_aresta(i_v1, i_v2)

        return sub_grafo
    
    # Exercício 4.3
    def subtrair_vertices(self, vertices):
        for v in vertices:
            if (self.existe_vertice(v)):
                self.remove_vertice(v.i)
            else:
                return print("Não é possivel remover um vertice que nao pertence ao grafo")

    # Exercício 4.4
    def subgrafo_aresta_induzido(self, arestas):
        sub_grafo = Grafo(1, 0)
        for a in arestas:
            if ((a.v1 not in self.estrutura) or (a.v2 not in self.estrutura) or (a.v1 not in self.estrutura[a.v2]) or (a.v2 not in self.estrutura[a.v1])):
                return print("Não é possivel criar um subgrafo aresta-induzido com arestas que nao pertencem ao grafo")
            else:
                if (a.v1 not in sub_grafo.estrutura):
                    sub_grafo.add_vertice(a.v1, self.vertices[a.v1].r)
                if (a.v2 not in sub_grafo.estrutura):
                    sub_grafo.add_vertice(a.v2, self.vertices[a.v2].r)
                sub_grafo.add_aresta(a.v1, a.v2)
        
        return sub_grafo
    
    # Exercício 4.5
    def subtrair_arestas(self, arestas):
        for a in arestas:
            if (self.verificar_vizinhos(a.v1, a.v2)):
                self.remove_aresta(a.v1, a.v2)
            else:
                return print("Não é possivel remover uma aresta que nao pertence ao grafo")
        
def main():
    grafo = Grafo(1, 5)
    
    grafo.add_vertice(0, "u")
    grafo.add_vertice(1, "v")
    grafo.add_vertice(2, "y")
    grafo.add_vertice(3, "x")
    grafo.add_vertice(4, "w")

    grafo.add_aresta(0, 1) # aresta -> a
    grafo.add_aresta(0, 2) # aresta -> e
    grafo.add_aresta(1, 2) # aresta -> f
    grafo.add_aresta(1, 2) # aresta -> g
    grafo.add_aresta(2, 3) # aresta -> d
    grafo.add_aresta(1, 4) # aresta -> b
    grafo.add_aresta(2, 4) # aresta -> h
    grafo.add_aresta(3, 4) # aresta -> c

    grafo2 = copy.deepcopy(grafo) # Copia desvinculada do grafo original
    grafo3 = copy.deepcopy(grafo) # Copia desvinculada do grafo original

    # Exercício 4.6 a)
    vertices_s = [Vertice(0, "u"), Vertice(1, "v"), 
                  Vertice(2, "y"), Vertice(4, "w")]
    arestas_s = [Aresta(0, 1), Aresta(1, 2), Aresta(2, 4)]

    sub_grafo = grafo.subgrafo(vertices_s, arestas_s)
    print('-=' * 20)
    print(f"{'Subgrafo Proprio':^40}")
    sub_grafo.imprimir_grafo()

    # Exercício 4.6 b)
    sub_grafo_gerador = Grafo(1, 5)
    
    sub_grafo_gerador.add_vertice(0, "u")
    sub_grafo_gerador.add_vertice(1, "v")
    sub_grafo_gerador.add_vertice(2, "y")
    sub_grafo_gerador.add_vertice(3, "x")
    sub_grafo_gerador.add_vertice(4, "w")

    sub_grafo_gerador.add_aresta(0, 1)
    sub_grafo_gerador.add_aresta(1, 2)
    sub_grafo_gerador.add_aresta(2, 3)
    sub_grafo_gerador.add_aresta(3, 4)

    print('-=' * 20)
    print(f"{'Subgrafo Gerador':^40}")
    sub_grafo_gerador.imprimir_grafo()

    # Exercício 4.6 c)
    x1 = [Vertice(0, "u"), Vertice(1, "v"), 
          Vertice(2, "y"), Vertice(4, "w")]
    
    sub_grafo_induzido = grafo.subgrafo_induzido(x1)
    print('-=' * 20)
    print(f"{'G[X1]':^40}")
    sub_grafo_induzido.imprimir_grafo()

    # Exercício 4.6 d)
    x = [Vertice(0, "u"), Vertice(4, "w")]
    grafo2.subtrair_vertices(x)
    print('-=' * 20)
    print(f"{'G - X':^40}")
    grafo2.imprimir_grafo()

    # Exercício 4.6 e)
    e1 = [Aresta(0, 1), Aresta(0, 2), Aresta(1, 2), Aresta(3, 4)]
    sub_grafo_a_i = grafo.subgrafo_aresta_induzido(e1)
    print('-=' * 20)
    print(f"{'G[E1]':^40}")
    sub_grafo_a_i.imprimir_grafo()

    # Exercício 4.6 f)
    e2 = [Aresta(0, 1), Aresta(1, 4), Aresta(1, 2)]
    grafo3.subtrair_arestas(e2)
    print('-=' * 20)
    print(f"{'G - E2':^40}")
    grafo3.imprimir_grafo()

main()
