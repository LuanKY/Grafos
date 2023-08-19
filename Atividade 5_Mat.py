from collections import deque

class Passeio:
    def __init__(self,grafo):
        self.grafo = grafo

    # Função para criar um passeio
    def criar_passeio(self,v1,v2):
        passeio = []

        # Encontrar vértices iniciais e finais
        v_ini = self.grafo.encontrar_vertice_por_i(v1)
        v_fin = self.grafo.encontrar_vertice_por_i(v2)

        if not v_ini or not v_fin:
            print("Vertice(s) não encontrado(s).")
            return passeio
        
        caminho = self.encontrar_caminho(v1,v2)

        if not caminho:
            print("Caminho não encontrado entre os vértices.")
            return passeio
        
        for i in range (len(caminho) - 1):
            v_atual = caminho[i]
            v_prox = caminho[i + 1]

            aresta = self.grafo.encontrar_aresta_entre_vertices(v_atual,v_prox)
            if aresta:
                self.add_vertice_passeio(passeio,v_atual)
                self.add_aresta_passeio(passeio,aresta)
            else:
                print(f"Aresta entre {v_atual.i} e {v_prox.i} não existe.")

        self.add_vertice_passeio(passeio,v_fin)

        return passeio

    def gerar_trilha(self,v1, v2):
        trilha = []

        # Verificar se os vértices são válidos
        vertice1 = self.grafo.encontrar_vertice_por_i(v1)
        vertice2 = self.grafo.encontrar_vertice_por_i(v2)

        if not vertice1 or not vertice2:
            print("Vértice(s) não encontrado(s).")
            return trilha

        # Verificar se existe uma aresta entre os vértices
        aresta = self.grafo.encontrar_aresta_entre_vertices(vertice1, vertice2)
        if not aresta:
            print("Não existe aresta entre os vértices.")
            return trilha

        trilha.append(('v', vertice1))
        trilha.append(('a', aresta))
        trilha.append(('v', vertice2))

        return trilha
    
    # Encontra um caminho entre 2 vertices
    def encontrar_caminho(self,v_ini,v_fin):
        visitados = set()
        fila = deque()

        fila.append([v_ini])

        while fila:
            caminho = fila.popleft()
            v_atual = caminho[-1]

            if v_atual == v_fin:
                return caminho
            
            if v_atual not in visitados:
                visitados.add(v_atual)

                for vizinho in self.grafo.estrutura.get(v_atual,[]):
                    if vizinho not in visitados:
                        nov_caminho = list(caminho)
                        nov_caminho.append(vizinho)
                        fila.append(nov_caminho)
        return None

    # Função para adicionar um vértice ao passeio
    def add_vertice_passeio(self, passeio, vertice):
        passeio.append(('v', vertice))

    # Função para adicionar uma aresta ao passeio
    def add_aresta_passeio(self, passeio, aresta):
        passeio.append(('a', aresta))

    def imprimir_passeio(self, passeio):
        if len(passeio) == 0:
            print("Passeio vazio")
        else:
            for tipo, elemento in passeio:
                if tipo == 'v':
                    vertice = self.grafo.encontrar_vertice_por_i(elemento)
                    print(f"Vertice: {vertice.i} - Rotulo: {vertice.r}")
                elif tipo == 'a':
                    v1 = self.grafo.encontrar_vertice_por_i(elemento.v1)
                    v2 = self.grafo.encontrar_vertice_por_i(elemento.v2)
                    print(f"Aresta: ({v1.i}, {v2.i})")
            vertice = self.grafo.encontrar_vertice_por_i(passeio[-1])
            print(f"Vertice: {vertice.i} - Rotulo: {vertice.r}")
    
    def imprimir_reverso_passeio(self, passeio):
        if len(passeio) == 0:
            print("Passeio vazio")
        else:
            inverso = passeio[::-1]  # Inverte a ordem do passeio
            for tipo, elemento in inverso:
                if tipo == 'v':
                    vertice = self.grafo.encontrar_vertice_por_i(elemento)
                    print(f"Vertice: {vertice.i} - Rotulo: {vertice.r}")
                elif tipo == 'a':
                    v1 = self.grafo.encontrar_vertice_por_i(elemento.v1)
                    v2 = self.grafo.encontrar_vertice_por_i(elemento.v2)
                    print(f"Aresta: ({v1.i}, {v2.i})")

    def obter_secao(self,passeio,i,j):
        if i < 0 or j < 0 or i >= len(passeio) or j >= len(passeio) or i > j:
            print("Índices inválidos para a seção.")
            return []
        secao = passeio[i:j + 1]
        return secao
    
    def imprimir_secao_do_passeio(self,secao):
        if len(secao) == 0:
            print("Seção do passeio vazia")
        else:
            for tipo, elemento in secao:
                if tipo == 'v':
                    vertice = self.grafo.encontrar_vertice_por_i(elemento)
                    print(f"Vertice: {vertice.i} - Rotulo: {vertice.r}")
                elif tipo == 'a':
                    v1 = self.grafo.encontrar_vertice_por_i(elemento.v1)
                    v2 = self.grafo.encontrar_vertice_por_i(elemento.v2)
                    print(f"Aresta: ({v1.i}, {v2.i})")


class Vertice:
    def __init__(self, i, r):
        self.i = i # i-> Índice
        self.r = r # r -> Rotulo
        self.grau = 0  # Adicionando o atributo grau

class Aresta:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []
        self.estrutura = {}  # Estrutura de adjacência

    def add_vertice(self, i, r):
        vertice = Vertice(i, r)
        self.vertices.append(vertice)

    def add_aresta(self, i_v1, i_v2):
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

    def encontrar_vertice_por_i(self, i):
        for vertice in self.vertices:
            if vertice.i == i:
                return vertice
        return None
    
    def encontrar_aresta_entre_vertices(self, v1, v2):
        for aresta in self.arestas:
            if (aresta.v1 == v1 and aresta.v2 == v2) or \
               (aresta.v1 == v2 and aresta.v2 == v1):
                return aresta
        return None

def main():
    grafo = Grafo()
    # Adicionar vértices
    grafo.add_vertice(0, "u")
    grafo.add_vertice(1, "v")
    grafo.add_vertice(2, "y")
    grafo.add_vertice(3, "x")
    grafo.add_vertice(4, "w")
    grafo.add_vertice(5, "z")

    # Adicionar arestas
    grafo.add_aresta(0, 1)
    grafo.add_aresta(1, 2)
    grafo.add_aresta(1, 2)
    grafo.add_aresta(2, 3)
    grafo.add_aresta(2, 3)
    grafo.add_aresta(3, 4)
    grafo.add_aresta(4, 5)

    passeio = Passeio(grafo)
    n_passeio = passeio.criar_passeio(0,5)
    # secao = passeio.obter_secao(n_passeio,1,3)
    passeio.imprimir_passeio(n_passeio) #Erro não descoberto
    # passeio.imprimir_reverso_passeio(n_passeio) Erro não descoberto 
    

main()


