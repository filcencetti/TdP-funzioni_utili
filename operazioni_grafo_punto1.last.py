#funzione per ottenere il cammino più lungo partendo da un nodo
    def getBFSNodesFromTree(self, source):
        tree = nx.bfs_tree(self._graph, self._idMap[int(source)])
        archi = list(tree.edges())
        nodi = list(tree.nodes())
        return nodi[1:]

    def getDFSNodesFromTree(self, source):
        tree = nx.dfs_tree(self._graph, source)
        nodi = list(tree.nodes())
        return nodi[1:]

    def getCammino(self, sourceStr):
        source = self._idMap[int(sourceStr)]
        lp = []

        #for source in self._graph.nodes:
        tree = nx.dfs_tree(self._graph, source)
        nodi = list(tree.nodes())

        for node in nodi:
            tmp = [node]

            while tmp[0] != source:
                pred = nx.predecessor(tree, source, tmp[0])
                tmp.insert(0, pred[0])

            if len(tmp) > len(lp):
                lp = copy.deepcopy(tmp)

        return lp

#funzione per visualizzare differenza peso archi uscenti e entranti
    def getBestDriver(self):
        best = 0
        bestdriver = None
        for n in self._graph.nodes:
            score = 0
            for e_out in self._graph.out_edges(n, data=True):
                score += e_out[2]["weight"]
            for e_in in self._graph.in_edges(n, data=True):
                score -= e_in[2]["weight"]

            if score > best:
                 bestdriver = n
                 best = score

        print(f"Best driver: {bestdriver}, with score {best}")
        return bestdriver, best
"""

#funzione per trovare la componente connessa partendo da un nodo
"""
    def getInfoConnessa(self, a1):
        cc = nx.node_connected_component(self._grafo, a1)
        return len(cc), self._getDurataTot(cc)

    #self._getDurataTot(cc) per trovare anche la durate totale in minuti


#funzione per trovare i vicini di un nodo ordinati per il peso
    def getNeighborsSorted(self, source):
        vicini = nx.neighbors(self._graph, source) # [v0, v1, v2, ...]

        #vicini = self._graph.neighbors(source)
        viciniTuple = []

        for v in vicini:
            viciniTuple.append((v, self._graph[source][v]["weight"])) # [ (v0, p0) (v1,p1) () ]

        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple