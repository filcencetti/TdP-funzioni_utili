# init
    def __init__(self):
        self._nodes = []
        self._graph = nx.Graph()
        self._idMap = {}
        self._bestPath = []
        self._bestScore = 0

#funzione per creare archi che colleghino tutte le coppie distinte di nodi.

# Aggiungo un arco per ogni combinazione di nodi
        myedges = list(itertools.combinations(self.list_with_nodes,
                                              2))  # restituisce una lista di tuple con tutte le combinazioni dei nodi
        self._graph.add_edges_from(myedges)

#funzioni per creare il grafo
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


#creazione grafo con archi aggiunti tramite idMap
    def buildGraph(self, durataMin):
        self._grafo.clear()
        self._allNodi = DAO.getAlbums(durataMin)
        self._grafo.add_nodes_from(self._allNodi)
        self._idMapAlbum = {n.AlbumId: n for n in self._allNodi}
        self._allEdges = DAO.getAllEdges(self._idMapAlbum)
        self._grafo.add_edges_from(self._allEdges)

#altra cosa che si può fare per aggiungere gli archi
    allEdges = DAO.getDriverYearResults(anno, self._idMap)
    for e in allEdges:
        self._graph.add_edge(e[0], e[1], weight=e[2])

#e nel DAO: passare idMap come parametro, nella query restituire nodo1, nodo2, peso e poi:
        for row in cursor:
            results.append((idMap[row["d1"]],idMap[row["d2"]], row["cnt"]))

#schema per la ricorsione
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


