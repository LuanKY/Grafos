class Grafo:
    def __init__(self):
        self.vertices = set()
        self.arestas = {}
        
    def adicionar_vertice(self, vertice):
        self.vertices.add(vertice)
        self.arestas[vertice] = []
        
    def adicionar_aresta(self, ori, dest, comp):
        self.arestas[ori].append((dest, comp))
        self.arestas[dest].append((ori, comp))
    
    def obter_vizs(self, vertice):
        return self.arestas[vertice]
        

def dijkstra(grafo, ori):
    dist = {v: float('infinity') for v in grafo.vertices}
    pred = {v: None for v in grafo.vertices}
    dist[ori] = 0
    no_nao_vis = set(grafo.vertices)

    while no_nao_vis:
        no_atual = min(no_nao_vis, key=lambda v: dist[v])
        no_nao_vis.remove(no_atual)

        for viz, comp in grafo.obter_vizs(no_atual):
            n_dist = dist[no_atual] + comp
            if n_dist < dist[viz]:
                dist[viz] = n_dist
                pred[viz] = no_atual

    return dist, pred

def encontrar_m_caminho(grafo, ori, dest):
    dist, pred = dijkstra(grafo, ori)

    caminho = [dest]
    atual = dest
    while pred[atual] is not None:
        caminho.insert(0, pred[atual])
        atual = pred[atual]

    return caminho, dist[dest]

def imprimir_resultado(caminho, dist):
    print(f'Caminho: {" -> ".join(caminho)}')
    print(f'Distância total: {dist} Km')

# Criando o grafo para Sergipe
sergipe = Grafo()

cidades = ['Aracaju', 'Itabaiana', 'Lagarto', 'Estância', 'Propriá']
for cidade in cidades:
    sergipe.adicionar_vertice(cidade)

sergipe.adicionar_aresta('Aracaju', 'Itabaiana', 50)
sergipe.adicionar_aresta('Aracaju', 'Lagarto', 30)
sergipe.adicionar_aresta('Itabaiana', 'Lagarto', 20)
sergipe.adicionar_aresta('Itabaiana', 'Estância', 40)
sergipe.adicionar_aresta('Lagarto', 'Estância', 25)
sergipe.adicionar_aresta('Lagarto', 'Propriá', 35)
sergipe.adicionar_aresta('Estância', 'Propriá', 45)

ori = 'Aracaju'
dest = 'Estância'

m_caminho, dist = encontrar_m_caminho(sergipe, ori, dest)
imprimir_resultado(m_caminho, dist)
