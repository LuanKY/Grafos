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
  
def sergipe():
    grafo = Grafo() 
    
    municipios = [
        "Aquidaba", "Aracaju", "Araua", "Areia Branca", "Barra Dos Coqueiros",
        "Boquim", "Brejo Grande", "Campo Do Brito", "Canhoba", "Caninde De Sao Francisco",
        "Capela", "Carira", "Cedro De Sao Joao", "Cristinapolis", "Cumbe",
        "Divina Pastora", "Estancia", "Feira Nova", "Frei Paulo", "Gararu",
        "Gracho Cardoso", "Ilha Das Flores", "Indiaroba", "Itabaiana", "Itabaianinha",
        "Itabi", "Itaporanga D'Ajuda", "Japaratuba", "Japoata", "Lagarto", "Laranjeiras",
        "Macambira", "Malhador", "Maruim", "Moita Bonita", "Monte Alegre De Sergipe",
        "Muribeca", "Neopolis", "Nossa Senhora Aparecida", "Nossa Senhora Da Gloria",
        "Nossa Senhora Das Dores", "Nossa Senhora De Lourdes", "Nossa Senhora Do Socorro",
        "Pacatuba", "Pedra Mole", "Pedrinhas", "Pinhao", "Pirambu", "Poco Redondo",
        "Poco Verde", "Porto Da Folha", "Propria", "Riachao Do Dantas", "Riachuelo",
        "Ribeiropolis", "Rosario Do Catete", "Salgado", "Santa Luzia Do Itanhy",
        "Santana Do Sao Francisco", "Santo Amaro Das Brotas", "Sao Cristovao", "Sao Francisco",
        "Sao Miguel Do Aleixo", "Simao Dias", "Siriri", "Telha", "Tobias Barreto",
        "Tomar Do Geru", "Umbauba"
    ]
    for municipio in municipios: 
        grafo.adicionar_vertice(municipio) 
    
    fronteira = [
        ("Aquidaba", [("Muribeca", 0), ("Canhoba", 0)]),
        ("Araua", [("Itabaianinha", 0), ("Estancia", 0)]),
        ("Areia Branca", [("Laranjeiras", 0), ("Riachuelo", 0), ("Malhador", 0), ("Itabaiana", 0)]),
        ("Barra Dos Coqueiros", [("Pirambu", 0), ("Aracaju", 0)]),
        ("Boquim", [("Pedrinhas", 0), ("Salgado", 0), ("Lagarto", 0), ("Araua", 0), ("Itabaianinha", 0)]),
        ("Brejo Grande", [("Pacatuba", 0)]),
        ("Campo Do Brito", [("Lagarto", 0), ("Macambira", 0), ("Itabaiana", 0)]),
        ("Caninde De Sao Francisco", [("Poco Redondo", 0)]),
        ("Capela", [("Siriri", 0), ("Aquidaba", 0), ("Muribeca", 0), ("Japaratuba", 0)]),
        ("Cedro De Sao Joao", [("Telha", 0), ("Propria", 0), ("Sao Francisco", 0), ("Aquidaba", 0)]),
        ("Cristinapolis", [("Itabaianinha", 0), ("Umbauba", 0), ("Tomar Do Geru", 0)]),
        ("Cumbe", [("Feira Nova", 0), ("Aquidaba", 0), ("Capela", 0)]),
        ("Divina Pastora", [("Maruim", 0), ("Riachuelo", 0), ("Siriri", 0)]),
        ("Frei Paulo", [("Ribeiropolis", 0), ("Carira", 0)]),
        ("Gararu", [("Porto Da Folha", 0)]),
        ("Gracho Cardoso", [("Feira Nova", 0), ("Cumbe", 0), ("Aquidaba", 0), ("Itabi", 0), ("Gararu", 0)]),
        ("Ilha Das Flores", [("Brejo Grande", 0), ("Pacatuba", 0), ("Neopolis", 0)]),
        ("Indiaroba", [("Cristinapolis", 0), ("Umbauba", 0), ("Santa Luzia Do Itanhy", 0), ("Estancia", 0)]),
        ("Itabaiana", [("Malhador", 0), ("Ribeiropolis", 0), ("Frei Paulo", 0)]),
        ("Itabi", [("Gararu", 0), ("Canhoba", 0)]),
        ("Itaporanga D'Ajuda", [("Salgado", 0), ("Estancia", 0), ("Aracaju", 0), ("Sao Cristovao", 0), ("Areia Branca", 0), ("Campo Do Brito", 0), ("Lagarto", 0)]),
        ("Japaratuba", [("Pirambu", 0), ("Muribeca", 0)]),
        ("Japoata", [("Neopolis", 0), ("Propria", 0), ("Pirambu", 0), ("Japaratuba", 0)]),
        ("Macambira", [("Pedra Mole", 0), ("Lagarto", 0), ("Frei Paulo", 0), ("Itabaiana", 0)]),
        ("Maruim", [("Laranjeiras", 0)]),
        ("Moita Bonita", [("Riachuelo", 0), ("Malhador", 0), ("Itabaiana", 0), ("Ribeiropolis", 0)]),
        ("Monte Alegre De Sergipe", [("Nossa Senhora Da Gloria", 0)]),
        ("Neopolis", [("Propria", 0)]),
        ("Nossa Senhora Aparecida", [("Carira", 0), ("Frei Paulo", 0), ("Ribeiropolis", 0), ("Sao Miguel Do Aleixo", 0)]),
        ("Nossa Senhora Da Gloria", [("Carira", 0), ("Nossa Senhora Aparecida", 0), ("Sao Miguel Do Aleixo", 0), ("Feira Nova", 0), ("Gracho Cardoso", 0), ("Gararu", 0)]),
        ("Nossa Senhora Das Dores", [("Cumbe", 0), ("Capela", 0), ("Siriri", 0), ("Divina Pastora", 0), ("Riachuelo", 0), ("Moita Bonita", 0), ("Ribeiropolis", 0), ("Sao Miguel Do Aleixo", 0), ("Feira Nova", 0)]),
        ("Nossa Senhora De Lourdes", [("Gararu", 0), ("Itabi", 0), ("Canhoba", 0)]),
        ("Nossa Senhora Do Socorro", [("Sao Cristovao", 0), ("Aracaju", 0), ("Santo Amaro Das Brotas", 0), ("Laranjeiras", 0)]),
        ("Pacatuba", [("Pirambu", 0), ("Japaratuba", 0), ("Neopolis", 0)]),
        ("Pedra Mole", [("Pinhao", 0), ("Lagarto", 0), ("Frei Paulo", 0)]),
        ("Pedrinhas", [("Itabaianinha", 0), ("Araua", 0)]),
        ("Pinhao", [("Frei Paulo", 0), ("Carira", 0)]),
        ("Poco Redondo", [("Porto Da Folha", 0), ("Monte Alegre De Sergipe", 0)]),
        ("Poco Verde", [("Simao Dias", 0)]),
        ("Porto Da Folha", [("Monte Alegre De Sergipe", 0), ("Gararu", 0)]),
        ("Riachao Do Dantas", [("Lagarto", 0), ("Boquim", 0), ("Itabaianinha", 0)]),
        ("Riachuelo", [("Malhador", 0), ("Laranjeiras", 0)]),
        ("Rosario Do Catete", [("Maruim", 0), ("Divina Pastora", 0), ("Siriri", 0), ("Capela", 0), ("Pirambu", 0)]),
        ("Salgado", [("Lagarto", 0), ("Estancia", 0)]),
        ("Santa Luzia Do Itanhy", [("Itabaianinha", 0), ("Araua", 0), ("Estancia", 0)]),
        ("Santana Do Sao Francisco", [("Neopolis", 0)]),
        ("Santo Amaro Das Brotas", [("Laranjeiras", 0), ("Maruim", 0), ("Rosario Do Catete", 0), ("Pirambu", 0), ("Barra Dos Coqueiros", 0)]),
        ("Sao Cristovao", [("Aracaju", 0)]),
        ("Sao Francisco", [("Muribeca", 0), ("Japoata", 0), ("Propria", 0)]),
        ("Sao Miguel Do Aleixo", [("Feira Nova", 0), ("Ribeiropolis", 0)]),
        ("Simao Dias", [("Lagarto", 0), ("Riachao Do Dantas", 0), ("Pedra Mole", 0), ("Pinhao", 0)]),
        ("Telha", [("Canhoba", 0), ("Propria", 0)]),
        ("Tobias Barreto", [("Itabaianinha", 0), ("Riachao Do Dantas", 0), ("Simao Dias", 0), ("Poco Verde", 0)]),
        ("Tomar Do Geru", [("Tobias Barreto", 0), ("Itabaianinha", 0)]),
        ("Umbauba", [("Itabaianinha", 0), ("Santa Luzia Do Itanhy", 0)]),
    ]

    for v1, vizinhos in fronteira:
        for v2, comprimento in vizinhos:
            grafo.adicionar_aresta(v1, v2, comprimento)

    origem = 'Aracaju' 
    destino = 'Propria' 
    
    melhor_caminho, distancia_total = encontrar_menor_caminho(grafo, origem, destino) 
    imprimir_resultado(melhor_caminho, distancia_total)
    print(grafo.arestas)

def acre():
    grafo = Grafo() 
    
    municipios = [
        "Rio Branco", "Cruzeiro do Sul", "Tarauaca", "Brasileia", "Senador Guiomard",
        "Mancio Lima", "Xapuri", "Marechal Thaumaturgo", "Placido de Castro", "Bujari",
        "Manoel Urbano", "Jordao", "Assis Brasil", "Santa Rosa do Purus", "Epitaciolandia",
        "Porto Acre", "Acrelandia", "Rodrigues Alves", "Feijo", "Porto Walter",
        "Sena Madureira", "Capixaba"
    ]
    for municipio in municipios: 
        grafo.adicionar_vertice(municipio) 
    
    fronteira = [
        ("Rio Branco", [("Sena Madureira", 0), ("Xapuri", 0), ("Bujari", 0), ("Porto Acre", 0), ("Senador Guiomard", 0), ("Capixaba", 0)]),
        ("Cruzeiro do Sul", [("Rodrigues Alves", 0), ("Porto Walter", 0), ("Tarauaca", 0)]),
        ("Tarauaca", [("Feijo", 0), ("Jordao", 0), ("Marechal Thaumaturgo", 0), ("Porto Walter", 0)]),
        ("Brasileia", [("Sena Madureira", 0), ("Epitaciolandia", 0), ("Xapuri", 0), ("Rio Branco", 0)]),
        ("Senador Guiomard", [("Porto Acre", 0), ("Acrelandia", 0), ("Placido de Castro", 0), ("Capixaba", 0)]),
        ("Mancio Lima", [("Rodrigues Alves", 0), ("Cruzeiro do Sul", 0)]),
        ("Xapuri", [("Epitaciolandia", 0), ("Capixaba", 0)]),
        ("Marechal Thaumaturgo", [("Porto Walter", 0)]),
        ("Placido de Castro", [("Acrelandia", 0), ("Capixaba", 0)]),
        ("Bujari", [("Sena Madureira", 0), ("Porto Acre", 0)]),
        ("Manoel Urbano", [("Feijo", 0), ("Sena Madureira", 0)]),
        ("Jordao", [("Feijo", 0), ("Marechal Thaumaturgo", 0)]),
        ("Assis Brasil", [("Sena Madureira", 0), ("Brasileia", 0)]),
        ("Santa Rosa do Purus", [("Feijo", 0), ("Manoel Urbano", 0)])
    ]

    for v1, vizinhos in fronteira:
        for v2, comprimento in vizinhos:
            grafo.adicionar_aresta(v1, v2, comprimento)

    origem = 'Rio Branco' 
    destino = 'Jordao' 
    
    melhor_caminho, distancia_total = encontrar_menor_caminho(grafo, origem, destino) 
    imprimir_resultado(melhor_caminho, distancia_total)
    print(grafo.arestas)

# sergipe()
acre()