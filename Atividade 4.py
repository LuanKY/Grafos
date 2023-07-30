# Exercício 3.3 1/3 
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
    
    def encontrar_vertice_por_indice(self, indice):
        for vertice in self.vertices:
            if vertice.i == indice:
                return vertice
        return None
    
    def existe_vertice(self, vertice):
        return vertice in self.vertices
    
    #Exercício 4.1  
    def subgrafo(self, vertices_s, arestas_s):
        n_Grafo = Grafo(1,8)
        # Adiciona os vértices do subgrafo ao novo grafo
        for vertice in vertices_s:
            n_Grafo.add_vertice(vertice.i, vertice.r)
        # Adiciona as arestas do subgrafo ao novo grafo
        for aresta in arestas_s:
            i_v1 = aresta.v1
            i_v2 = aresta.v2
            n_Grafo.add_aresta(i_v1, i_v2)
        return n_Grafo

    # Exercício 4.2
    def s_induzido(self, vertices_subgrafo):
        n_Grafo = Grafo(1,8)
        # Adiciona os vértices do subgrafo ao novo grafo
        for vertice in vertices_subgrafo:
            n_Grafo.add_vertice(vertice.i, vertice.r)
        # Adiciona as arestas do subgrafo ao novo grafo
        for aresta in self.arestas:
            if aresta.v1 in vertices_subgrafo and aresta.v2 in vertices_subgrafo:
                n_Grafo.add_aresta(aresta.v1.i, aresta.v2.i)
        return n_Grafo
    
    #Exercício 4.3
    def subtrair_vertices(self, vertices_subtrair):
        n_Grafo = Grafo(1,8)
        # Adiciona todos os vértices do grafo original ao novo grafo, exceto os do conjunto vertices_subtrair
        for vertice in self.vertices:
            if vertice not in vertices_subtrair:
                n_Grafo.add_vertice(vertice.i, vertice.r)
        # Adiciona as arestas do grafo original ao novo grafo, mantendo apenas as que ainda têm vértices válidos
        for aresta in self.arestas:
            if aresta.v1 not in vertices_subtrair and aresta.v2 not in vertices_subtrair:
                n_Grafo.add_aresta(aresta.v1.i, aresta.v2.i)

        return n_Grafo

    # Exercício 4.4
    def s_aresta(self, arestas_s):
        n_Grafo = Grafo(1,8)
        # Adiciona os vértices presentes nas arestas do subgrafo ao novo grafo
        # v_p -> vertices presentes; v1 e v2 -> vertice
        v_p = set()
        for aresta in arestas_s:
            v1, v2 = aresta
            v_p.add(v1)
            v_p.add(v2)
        for vertice in v_p:
            n_Grafo.add_vertice(vertice.i, vertice.r)
        # Adiciona as arestas do subgrafo ao novo grafo
        for aresta in arestas_s:
            v1, v2 = aresta
            if self.existe_vertice(v1) and self.existe_vertice(v2):
                n_Grafo.add_aresta(v1.i, v2.i)
        return n_Grafo

    # Exercício 4.5
    def subtrair_arestas(self, arestas_subtrair):
        n_Grafo = Grafo(1,8)
        # Adiciona todos os vértices do grafo original ao novo grafo
        for vertice in self.vertices:
            n_Grafo.add_vertice(vertice.i, vertice.r)
        # Adiciona as arestas do grafo original ao novo grafo, exceto as do conjunto arestas_subtrair
        for aresta in self.arestas:
            if aresta not in arestas_subtrair:
                n_Grafo.add_aresta(aresta.v1.i, aresta.v2.i)
        return n_Grafo

# Exercício 4.6
def main():
    grafo = Grafo(1, 8)
    # Adicionar vértices
    grafo.add_vertice(0, "u")
    grafo.add_vertice(1, "v")
    grafo.add_vertice(2, "y")
    grafo.add_vertice(3, "x")
    grafo.add_vertice(4, "w")

    # Adicionar arestas
    grafo.add_aresta(0, 1)
    grafo.add_aresta(0, 2)
    grafo.add_aresta(1, 2)
    grafo.add_aresta(1, 2)
    grafo.add_aresta(1, 4)
    grafo.add_aresta(2, 3)
    grafo.add_aresta(2, 4)
    grafo.add_aresta(3, 4)



    # 4.6 a)
    vertices_s = {grafo.encontrar_vertice_por_indice(0), grafo.encontrar_vertice_por_indice(1), grafo.encontrar_vertice_por_indice(2)}
    arestas_s = {grafo.arestas[0],grafo.arestas[1]}
    subgrafo = grafo.subgrafo(vertices_s,arestas_s)
    for vertice in subgrafo.vertices:
        print(f"Vértice: Índice - {vertice.i} Rotulo - {vertice.r}")
    for aresta in subgrafo.arestas:
        print(f"Aresta {aresta.v1} - {aresta.v2}")

    # 4.6 b)
    print('-=' * 20)
    vertices_subgrafo = {grafo.encontrar_vertice_por_indice(0), grafo.encontrar_vertice_por_indice(1), grafo.encontrar_vertice_por_indice(2)}
    s_induzido = grafo.s_induzido(vertices_subgrafo)
    for vertice in s_induzido.vertices:
        print(f"Vértice {vertice.r}")
    for aresta in s_induzido.arestas:
        print(f"Aresta {aresta.v1.r} - {aresta.v2.r}")

    # 4.6 c)
    vertices_subgrafo = {grafo.encontrar_vertice_por_indice(1), grafo.encontrar_vertice_por_indice(2), grafo.encontrar_vertice_por_indice(3), grafo.encontrar_vertice_por_indice(0)}
    s_induzido = grafo.s_induzido(vertices_subgrafo)
    for vertice in s_induzido.vertices:
        print(f"Vértice {vertice.r}")
    for aresta in s_induzido.arestas:
        print(f"Aresta {aresta.v1.r} - {aresta.v2.r}")

    # 4.6 d)
    print('-=' * 20)
    vertices_subtrair = {grafo.encontrar_vertice_por_indice(0), grafo.encontrar_vertice_por_indice(4)}
    subgrafo = grafo.subtrair_vertices(vertices_subtrair)
    for vertice in subgrafo.vertices:
        print(f"Vértice {vertice.r}")
    for aresta in subgrafo.arestas:
        print(f"Aresta {aresta.v1.r} - {aresta.v2.r}")

    # 4.6 e)
    print('-=' * 20)
    arestas_s = {(grafo.encontrar_vertice_por_indice(0), grafo.encontrar_vertice_por_indice(1)),
                    (grafo.encontrar_vertice_por_indice(3), grafo.encontrar_vertice_por_indice(4)),
                    (grafo.encontrar_vertice_por_indice(0),grafo.encontrar_vertice_por_indice(2)),
                    (grafo.encontrar_vertice_por_indice(2),grafo.encontrar_vertice_por_indice(3))}
    s_aresta = grafo.s_aresta(arestas_s)
    for vertice in s_aresta.vertices:
        print(f"Vértice {vertice.r}")
    for aresta in s_aresta.arestas:
        print(f"Aresta {aresta.v1} - {aresta.v2}")

main()
