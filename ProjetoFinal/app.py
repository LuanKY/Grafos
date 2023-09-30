from flask import Flask, render_template, request, jsonify

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
    print(f'Percursos passa por: {" -> ".join(caminho)}') 
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
        "Tomar Do Geru", "Umbauba", "Amparo De Sao Francisco", "Carmopolis", "General Maynard",
        "Malhada Dos Bois", "Santa Rosa De Lima", "Sao Domingos"
    ]
    for municipio in municipios: 
        grafo.adicionar_vertice(municipio) 
    fronteira = [
        ("Amparo De Sao Francisco", [("Canhoba", 9), ("Telha", 11)]),
        ("Aquidaba", [("Muribeca", 22), ("Canhoba", 23)]),
        ("Araua", [("Itabaianinha", 24), ("Estancia", 48)]),
        ("Areia Branca", [("Laranjeiras", 27), ("Riachuelo", 21), ("Malhador", 37), ("Itabaiana", 19)]),
        ("Barra Dos Coqueiros", [("Pirambu", 30), ("Aracaju", 19)]),
        ("Boquim", [("Pedrinhas", 8), ("Salgado", 30), ("Lagarto", 39), ("Araua", 20), ("Itabaianinha", 38)]),
        ("Brejo Grande", [("Pacatuba", 25), ("Ilha Das Flores", 10)]),
        ("Campo Do Brito", [("Lagarto", 30), ("Macambira", 11), ("Itabaiana", 13)]),
        ("Capela", [("Siriri", 15), ("Aquidaba", 33), ("Muribeca", 22), ("Japaratuba", 24)]),
        ("Carmopolis", [("Pirambu", 31), ("Santo Amaro Das Brotas", 25), ("General Maynard", 6), ("Rosario Do Catete", 9), ("Japaratuba", 13)]),
        ("Cedro De Sao Joao", [("Telha", 9), ("Propria", 11), ("Sao Francisco", 20), ("Aquidaba", 18)]),
        ("Cristinapolis", [("Itabaianinha", 30), ("Umbauba", 18), ("Tomar Do Geru", 17)]),
        ("Cumbe", [("Feira Nova", 25), ("Aquidaba", 24), ("Capela", 35)]),
        ("Divina Pastora", [("Maruim", 12), ("Riachuelo", 10), ("Siriri", 11)]),
        ("Frei Paulo", [("Ribeiropolis", 19), ("Carira", 37)]),
        ("Gararu", [("Porto Da Folha", 26)]),
        ("Gracho Cardoso", [("Feira Nova", 14), ("Cumbe", 38), ("Aquidaba", 23), ("Itabi", 19), ("Gararu", 42)]),
        ("Indiaroba", [("Cristinapolis", 46), ("Umbauba", 26), ("Santa Luzia Do Itanhy", 23), ("Estancia", 46)]),
        ("Itabaiana", [("Malhador", 18), ("Ribeiropolis", 22), ("Frei Paulo", 20)]),
        ("Itabi", [("Gararu", 24), ("Canhoba", 26)]),
        ("Itaporanga D'Ajuda", [("Salgado", 22), ("Estancia", 30), ("Aracaju", 42), ("Sao Cristovao", 16), ("Areia Branca", 54), ("Campo Do Brito", 56), ("Lagarto", 48)]),
        ("Japaratuba", [("Pirambu", 21), ("Muribeca", 24)]),
        ("Japoata", [("Neopolis", 36), ("Propria", 45), ("Pirambu", 56), ("Japaratuba", 55)]),
        ("Macambira", [("Pedra Mole", 22), ("Lagarto", 39), ("Frei Paulo", 25), ("Itabaiana", 22)]),
        ("Malhada Dos Bois", [("Muribeca", 14), ("Aquidaba", 27), ("Cedro De Sao Joao", 20), ("Sao Francisco", 13)]),
        ("Maruim", [("Laranjeiras", 10)]),
        ("Moita Bonita", [("Santa Rosa De Lima", 22), ("Malhador", 14), ("Itabaiana", 16), ("Ribeiropolis", 13)]),
        ("Monte Alegre De Sergipe", [("Nossa Senhora Da Gloria", 29), ("Porto Da Folha", 43)]),
        ("Neopolis", [("Propria", 42), ("Santana Do Sao Francisco", 13), ("Ilha Das Flores", 61)]),
        ("Nossa Senhora Aparecida", [("Carira", 115), ("Frei Paulo", 32), ("Ribeiropolis", 13), ("Sao Miguel Do Aleixo", 22)]),
        ("Nossa Senhora Da Gloria", [("Carira", 49), ("Nossa Senhora Aparecida", 35), ("Sao Miguel Do Aleixo", 30), ("Feira Nova", 15), ("Gracho Cardoso", 29), ("Gararu", 71)]),
        ("Nossa Senhora Das Dores", [("Cumbe", 17), ("Capela", 19), ("Siriri", 19), ("Divina Pastora", 30), ("Santa Rosa De Lima", 40), ("Moita Bonita", 26), ("Ribeiropolis", 35), ("Sao Miguel Do Aleixo", 48), ("Feira Nova", 30)]),
        ("Nossa Senhora De Lourdes", [("Gararu", 20), ("Itabi", 13), ("Canhoba", 14)]),
        ("Nossa Senhora Do Socorro", [("Sao Cristovao", 29), ("Aracaju", 26), ("Santo Amaro Das Brotas", 27), ("Laranjeiras", 12)]),
        ("Pacatuba", [("Pirambu", 60), ("Japaratuba", 68), ("Neopolis", 25), ("Ilha Das Flores", 22)]),
        ("Pedra Mole", [("Pinhao", 14), ("Lagarto", 52), ("Frei Paulo", 22)]),
        ("Pedrinhas", [("Itabaianinha", 31), ("Araua", 13)]),
        ("Pinhao", [("Frei Paulo", 27), ("Carira", 37)]),
        ("Poco Redondo", [("Porto Da Folha", 67), ("Monte Alegre De Sergipe", 31), ("Caninde De Sao Francisco", 21)]),
        ("Riachao Do Dantas", [("Lagarto", 23), ("Boquim", 28), ("Itabaianinha", 54)]),
        ("Riachuelo", [("Malhador", 20), ("Laranjeiras", 7)]),
        ("Rosario Do Catete", [("Maruim", 13), ("Divina Pastora", 20), ("Siriri", 10), ("Capela", 25), ("General Maynard", 14)]),
        ("Salgado", [("Lagarto", 26), ("Estancia", 34)]),
        ("Santa Luzia Do Itanhy", [("Itabaianinha", 60), ("Araua", 40), ("Estancia", 24)]),
        ("Santa Rosa De Lima", [("Malhador", 29), ("Riachuelo", 12), ("Divina Pastora", 11)]),
        ("Santo Amaro Das Brotas", [("Laranjeiras", 19), ("Maruim", 8), ("Rosario Do Catete", 20), ("Pirambu", 35), ("Barra Dos Coqueiros", 35), ("General Maynard", 20)]),
        ("Sao Cristovao", [("Aracaju", 20)]),
        ("Sao Domingos", [("Macambira", 22), ("Lagarto", 20), ("Campo Do Brito", 13)]),
        ("Sao Francisco", [("Muribeca", 20), ("Japoata", 29), ("Propria", 23)]),
        ("Sao Miguel Do Aleixo", [("Feira Nova", 21), ("Ribeiropolis", 27)]),
        ("Simao Dias", [("Lagarto", 26), ("Riachao Do Dantas", 48), ("Pedra Mole", 27), ("Pinhao", 28), ("Poco Verde", 46)]),
        ("Telha", [("Propria", 10)]),
        ("Tobias Barreto", [("Itabaianinha", 32), ("Riachao Do Dantas", 31), ("Simao Dias", 78), ("Poco Verde", 56)]),
        ("Tomar Do Geru", [("Tobias Barreto", 46), ("Itabaianinha", 20)]),
        ("Umbauba", [("Itabaianinha", 21), ("Santa Luzia Do Itanhy", 37)])
    ]

    for v1, vizinhos in fronteira:
        for v2, comprimento in vizinhos:
            grafo.adicionar_aresta(v1, v2, comprimento)

    return grafo

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
        ("Rio Branco", [("Sena Madureira", 144), ("Xapuri", 187), ("Bujari", 25), ("Porto Acre", 61), ("Senador Guiomard", 25), ("Capixaba", 82)]),
        ("Cruzeiro do Sul", [("Rodrigues Alves", 14), ("Porto Walter", 68), ("Tarauaca", 228)]),
        ("Tarauaca", [("Feijo", 48), ("Jordao", 169), ("Marechal Thaumaturgo", 237), ("Porto Walter", 217)]),
        ("Brasileia", [("Sena Madureira", 383), ("Epitaciolandia", 42), ("Xapuri", 76), ("Rio Branco", 243)]),
        ("Senador Guiomard", [("Porto Acre", 89), ("Acrelandia", 105), ("Placido de Castro", 72), ("Capixaba", 57)]),
        ("Mancio Lima", [("Rodrigues Alves", 35), ("Cruzeiro do Sul", 35)]),
        ("Xapuri", [("Epitaciolandia", 43), ("Capixaba", 107)]),
        ("Marechal Thaumaturgo", [("Porto Walter", 125)]),
        ("Placido de Castro", [("Acrelandia", 66), ("Capixaba", 110)]),
        ("Bujari", [("Sena Madureira", 120), ("Porto Acre", 77)]),
        ("Manoel Urbano", [("Feijo", 151), ("Sena Madureira", 88)]),
        ("Jordao", [("Feijo", 276), ("Marechal Thaumaturgo", 105)]),
        ("Assis Brasil", [("Sena Madureira", 489), ("Brasileia", 108)]),
        ("Santa Rosa do Purus", [("Feijo", 44), ("Manoel Urbano", 107)])
    ]

    for v1, vizinhos in fronteira:
        for v2, comprimento in vizinhos:
            grafo.adicionar_aresta(v1, v2, comprimento)

    return grafo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular_distancia():
    data = request.get_json()
    print(data)  # Verifica se os dados estão sendo recebidos corretamente
    state = data['state']
    origin = data['origin']
    destination = data['destination']

    grafo = None 

    if state == 'sergipe':
        grafo = sergipe()
    elif state == 'acre':
        grafo = acre()

    melhor_caminho, distancia_total = encontrar_menor_caminho(grafo, origin, destination)

    print(melhor_caminho, distancia_total)  # Verifica os resultados

    return jsonify({'distance': distancia_total, 'path': melhor_caminho})

@app.route('/static/<path:path>')
def serve_static(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run(debug=True)
