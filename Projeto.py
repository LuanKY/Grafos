class Vertice:
    def __init__(self, i, r):
        self.i = i
        self.r = r

class Aresta:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

class Grafo:
    def __init__(self):
        self.vertices = []
        self.arestas = []
        self.estrutura = {}

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

    def imprimir_grafo(self):
        self.estrutura = dict(sorted(self.estrutura.items()))
        # r -> rotulo | adj -> adjacência
        print('-=' * 50)
        for i in self.estrutura:
            r = self.vertices[i].r
            adj_r = []
            for v in self.estrutura[i]:
                if self.vertices[v].r not in adj_r:
                    adj_r.append(self.vertices[v].r)
            print(f"{r}: {adj_r}")
            print()
        print('-=' * 50)

grafoSergipe = Grafo()

municipiosSergipe = [
    "AQUIDABA", "ARACAJU", "ARAUA", "AREIA BRANCA", "BARRA DOS COQUEIROS",
    "BOQUIM", "BREJO GRANDE", "CAMPO DO BRITO", "CANHOBA", "CANINDE DE SAO FRANCISCO",
    "CAPELA", "CARIRA", "CEDRO DE SAO JOAO", "CRISTINAPOLIS", "CUMBE",
    "DIVINA PASTORA", "ESTANCIA", "FEIRA NOVA", "FREI PAULO", "GARARU",
    "GRACHO CARDOSO", "ILHA DAS FLORES", "INDIAROBA", "ITABAIANA", "ITABAIANINHA",
    "ITABI", "ITAPORANGA D'AJUDA", "JAPARATUBA", "JAPOATA", "LAGARTO", "LARANJEIRAS",
    "MACAMBIRA", "MALHADOR", "MARUIM", "MOITA BONITA", "MONTE ALEGRE DE SERGIPE",
    "MURIBECA", "NEOPOLIS", "NOSSA SENHORA APARECIDA", "NOSSA SENHORA DA GLORIA",
    "NOSSA SENHORA DAS DORES", "NOSSA SENHORA DE LOURDES", "NOSSA SENHORA DO SOCORRO",
    "PACATUBA", "PEDRA MOLE", "PEDRINHAS", "PINHAO", "PIRAMBU", "POCO REDONDO",
    "POCO VERDE", "PORTO DA FOLHA", "PROPRIA", "RIACHAO DO DANTAS", "RIACHUELO",
    "RIBEIROPOLIS", "ROSARIO DO CATETE", "SALGADO", "SANTA LUZIA DO ITANHY",
    "SANTANA DO SAO FRANCISCO", "SANTO AMARO DAS BROTAS", "SAO CRISTOVAO", "SAO FRANCISCO",
    "SAO MIGUEL DO ALEIXO", "SIMAO DIAS", "SIRIRI", "TELHA", "TOBIAS BARRETO",
    "TOMAR DO GERU", "UMBAUBA"
]

for i, municipio in enumerate(municipiosSergipe):
    grafoSergipe.add_vertice(i, municipio)

fronteira = [
    ("AQUIDABA", ["MURIBECA", "CANHOBA"]),
    ("ARAUA", ["ITABAIANINHA", "ESTANCIA"]),
    ("AREIA BRANCA", ["LARANJEIRAS", "RIACHUELO", "MALHADOR", "ITABAIANA"]),
    ("BARRA DOS COQUEIROS", ["PIRAMBU", "ARACAJU"]),
    ("BOQUIM", ["PEDRINHAS", "SALGADO", "LAGARTO", "ARAUA", "ITABAIANINHA"]),
    ("BREJO GRANDE", ["PACATUBA"]),
    ("CAMPO DO BRITO", ["LAGARTO", "MACAMBIRA", "ITABAIANA"]),
    ("CANINDE DE SAO FRANCISCO", ["POCO REDONDO"]),
    ("CAPELA", ["SIRIRI", "AQUIDABA", "MURIBECA", "JAPARATUBA"]),
    ("CEDRO DE SAO JOAO", ["TELHA", "PROPRIA", "SAO FRANCISCO", "AQUIDABA"]),
    ("CRISTINAPOLIS", ["ITABAIANINHA", "UMBAUBA", "TOMAR DO GERU"]),
    ("CUMBE", ["FEIRA NOVA", "AQUIDABA", "CAPELA"]),
    ("DIVINA PASTORA", ["MARUIM", "RIACHUELO", "SIRIRI"]),
    ("FREI PAULO", ["RIBEIROPOLIS", "CARIRA"]),
    ("GARARU", ["PORTO DA FOLHA"]),
    ("GRACHO CARDOSO", ["FEIRA NOVA", "CUMBE", "AQUIDABA", "ITABI", "GARARU"]),
    ("ILHA DAS FLORES", ["BREJO GRANDE", "PACATUBA", "NEOPOLIS"]),
    ("INDIAROBA", ["CRISTINAPOLIS", "UMBAUBA", "SANTA LUZIA DO ITANHY", "ESTANCIA"]),
    ("ITABAIANA", ["MALHADOR", "RIBEIROPOLIS", "FREI PAULO"]),
    ("ITABI", ["GARARU", "CANHOBA"]),
    ("ITAPORANGA D'AJUDA", ["SALGADO", "ESTANCIA", "ARACAJU", "SAO CRISTOVAO", "AREIA BRANCA", "CAMPO DO BRITO", "LAGARTO"]),
    ("JAPARATUBA", ["PIRAMBU", "MURIBECA"]),
    ("JAPOATA", ["NEOPOLIS", "PROPRIA", "PIRAMBU", "JAPARATUBA"]),
    ("MACAMBIRA", ["PEDRA MOLE", "LAGARTO", "FREI PAULO", "ITABAIANA"]),
    ("MARUIM", ["LARANJEIRAS"]),
    ("MOITA BONITA", ["RIACHUELO", "MALHADOR", "ITABAIANA", "RIBEIROPOLIS"]),
    ("MONTE ALEGRE DE SERGIPE", ["NOSSA SENHORA DA GLORIA"]),
    ("NEOPOLIS", ["PROPRIA"]),
    ("NOSSA SENHORA APARECIDA", ["CARIRA", "FREI PAULO", "RIBEIROPOLIS", "SAO MIGUEL DO ALEIXO"]),
    ("NOSSA SENHORA DA GLORIA", ["CARIRA", "NOSSA SENHORA APARECIDA", "SAO MIGUEL DO ALEIXO", "FEIRA NOVA", "GRACHO CARDOSO", "GARARU"]),
    ("NOSSA SENHORA DAS DORES", ["CUMBE", "CAPELA", "SIRIRI", "DIVINA PASTORA", "RIACHUELO", "MOITA BONITA", "RIBEIROPOLIS", "SAO MIGUEL DO ALEIXO", "FEIRA NOVA"]),
    ("NOSSA SENHORA DE LOURDES", ["GARARU", "ITABI", "CANHOBA"]),
    ("NOSSA SENHORA DO SOCORRO", ["SAO CRISTOVAO", "ARACAJU", "SANTO AMARO DAS BROTAS", "LARANJEIRAS"]),
    ("PACATUBA", ["PIRAMBU", "JAPOATA", "NEOPOLIS"]),
    ("PEDRA MOLE", ["PINHAO", "LAGARTO", "FREI PAULO"]),
    ("PEDRINHAS", ["ITABAIANINHA", "ARAUA"]),
    ("PINHAO", ["FREI PAULO", "CARIRA"]),
    ("POCO REDONDO", ["PORTO DA FOLHA", "MONTE ALEGRE DE SERGIPE"]),
    ("POCO VERDE", ["SIMAO DIAS"]),
    ("PORTO DA FOLHA", ["MONTE ALEGRE DE SERGIPE", "GARARU"]),
    ("RIACHAO DO DANTAS", ["LAGARTO", "BOQUIM", "ITABAIANINHA"]),
    ("RIACHUELO", ["MALHADOR", "LARANJEIRAS"]),
    ("ROSARIO DO CATETE", ["MARUIM", "DIVINA PASTORA", "SIRIRI", "CAPELA", "PIRAMBU"]),
    ("SALGADO", ["LAGARTO", "ESTANCIA"]),
    ("SANTA LUZIA DO ITANHY", ["ITABAIANINHA", "ARAUA", "ESTANCIA"]),
    ("SANTANA DO SAO FRANCISCO", ["NEOPOLIS"]),
    ("SANTO AMARO DAS BROTAS", ["LARANJEIRAS", "MARUIM", "ROSARIO DO CATETE", "PIRAMBU", "BARRA DOS COQUEIROS"]),
    ("SAO CRISTOVAO", ["ARACAJU"]),
    ("SAO FRANCISCO", ["MURIBECA", "JAPOATA", "PROPRIA"]),
    ("SAO MIGUEL DO ALEIXO", ["FEIRA NOVA", "RIBEIROPOLIS"]),
    ("SIMAO DIAS", ["LAGARTO", "RIACHAO DO DANTAS", "PEDRA MOLE", "PINHAO"]),
    ("TELHA", ["CANHOBA", "PROPRIA"]),
    ("TOBIAS BARRETO", ["ITABAIANINHA", "RIACHAO DO DANTAS", "SIMAO DIAS", "POCO VERDE"]),
    ("TOMAR DO GERU", ["TOBIAS BARRETO", "ITABAIANINHA"]),
    ("UMBAUBA", ["ITABAIANINHA", "SANTA LUZIA DO ITANHY"])
]

for v1, vizinhos in fronteira:
    for v2 in vizinhos:
        i_v1 = municipiosSergipe.index(v1)
        i_v2 = municipiosSergipe.index(v2)
        grafoSergipe.add_aresta(i_v1, i_v2)

grafoSergipe.imprimir_grafo()