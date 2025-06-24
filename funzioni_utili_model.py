# init
"""
    def __init__(self):
        self._nodes = []
        self._graph = nx.Graph()
        self._idMap = {}
        self._bestPath = []
        self._bestScore = 0
"""


#funzione per creare archi che colleghino tutte le coppie distinte di nodi.
"""
# Aggiungo un arco per ogni combinazione di nodi
        myedges = list(itertools.combinations(self.list_with_nodes,
                                              2))  # restituisce una lista di tuple con tutte le combinazioni dei nodi
        self._graph.add_edges_from(myedges)
"""
#funzioni per creare il grafo
"""
    def buildGraph(self, year):
        self._graph.clear()
        self._nodes = DAO.getNodes(year)
        for n in self._nodes:
            self._idMap[n.nodeId] = n
        self._graph.add_nodes_from(self._nodes)
        self.addEdges(year)
        return self._graph

    def addEdges(self, year):
        edges = DAO.getEdges(year)  arco formato da nodo1, nodo2, peso
        for edge in edges:
            u = self._idMap[edge.nodo1Id]
            v = self._idMap[edge.nodo2Id]
            self._graph.add_edge(u, v, weight=edge.peso)


    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()
"""


#schema per la ricorsione
"""
def getBestPath(self, k):
    self._bestPath = []
    self._bestScore = 1000

    parziale = []
    self._ricorsione(parziale, k)
    return self._bestPath, self._bestScore

def _ricorsione(self, parziale, k):
    if len(parziale) == k:
        if self.getScore(parziale) < self._bestScore:
            self._bestScore = self.getScore(parziale)
            self._bestPath = copy.deepcopy(parziale)
        return

    for n in self._graph.nodes():
        if n not in parziale:
            parziale.append(n)
            self._ricorsione(parziale, k)
            parziale.pop()

def getScore(self, team):
    score = 0
    for e in self._graph.edges(data=True):
        if e[0] not in team and e[1] in team:
            score += e[2]["weight"]
    return score
"""

