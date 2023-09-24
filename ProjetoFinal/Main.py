class Grafo: 
    def __init__(self): 
        self.vertices = set() 
        self.arestas = {} 
  
    def adicionar_vertice(self, vertice): 
        self.vertices.add(vertice) 
        self.arestas[vertice] = [] 
  
    def adicionar_aresta(self, origem, destino, comprimento): 
        self.arestas[origem].append((destino, comprimento)) 
        self.arestas[destino].append((origem, comprimento)) 
  
    def obter_vizinhos(self, vertice): 
        return self.arestas[vertice] 
  
  
def dijkstra(grafo, origem): 
    distancias = {v: float('infinity') for v in grafo.vertices} #Crio um dicionario com vertice como chave que define a distancia entre todos vertices menos o inicial como infinita
    predecessores = {v: None for v in grafo.vertices} #Crio outro dicionario para armazenar os vertices predecessores 
    distancias[origem] = 0 
    nos_nao_visitados = set(grafo.vertices) 
  
    while nos_nao_visitados: 
        no_atual = min(nos_nao_visitados, key=lambda v: distancias[v]) # Busco o vertice não visitado com a menor distancia
        nos_nao_visitados.remove(no_atual) #Marco e remove este vertice
  
        for vizinho, comprimento in grafo.obter_vizinhos(no_atual): 
            nova_distancia = distancias[no_atual] + comprimento #Calculo a distancia ate o vizinho
            if nova_distancia < distancias[vizinho]: #Verifico se o caminho passando pelo vertice atual é menor que o do vizinho
                #Se essa distância estimada for menor do que a distância atual atualizo a distância
                distancias[vizinho] = nova_distancia 
                predecessores[vizinho] = no_atual 
  
    return distancias, predecessores 
  
def encontrar_menor_caminho(grafo, origem, destino): 
    distancias, predecessores = dijkstra(grafo, origem) 
  
    caminho = [destino] #Crio um array chamado caminho que armazena o caminho do grafo. OBS: A distancia será encontrada de trás pra frente
    atual = destino # Variável usada pra encontrar o caminho
    while predecessores[atual] is not None: #Rodo um loop enquanto o vertice anterior a o atual não for nulo
        caminho.insert(0, predecessores[atual]) # insiro o predecessor no meu array
        atual = predecessores[atual] 
  
    return caminho, distancias[destino] 
  
def imprimir_resultado(caminho, distancia): 
    # Imprime o caminho e a distância total.
    print(f'Caminho: {" -> ".join(caminho)}') 
    print(f'Distância total: {distancia} Km') 
  
# Grafo Sergipe 
grafo_sergipe = Grafo() 
  
cidades = ['Aracaju', 'Itabaiana', 'Lagarto', 'Estância', 'Propriá'] 
for cidade in cidades: 
    grafo_sergipe.adicionar_vertice(cidade) 
  
grafo_sergipe.adicionar_aresta('Aracaju', 'Itabaiana', 50) 
grafo_sergipe.adicionar_aresta('Aracaju', 'Lagarto', 30) 
grafo_sergipe.adicionar_aresta('Itabaiana', 'Lagarto', 20) 
grafo_sergipe.adicionar_aresta('Itabaiana', 'Estância', 40) 
grafo_sergipe.adicionar_aresta('Lagarto', 'Estância', 25) 
grafo_sergipe.adicionar_aresta('Lagarto', 'Propriá', 35) 
grafo_sergipe.adicionar_aresta('Estância', 'Propriá', 45) 
  
origem = 'Aracaju' 
destino = 'Propriá' 
  
melhor_caminho, distancia_total = encontrar_menor_caminho(grafo_sergipe, origem, destino) 
imprimir_resultado(melhor_caminho, distancia_total)
