### FUNZIONE PER TROVARE CAMMINO DI PESO MASSIMO CON VINCOLO: (IN QUESTO CASO: PESO ARCHI DECRESCENTE)

def getBestPath(self, startStr):
    self._bestPath = []
    self._bestScore = 0

    start = self._idMap[int(startStr)]

    parziale = [start]

    vicini = self._graph.neighbors(start)
    for v in vicini:
        parziale.append(v)
        self.ricorsione(parziale)
        parziale.pop()

    return self._bestPath, self._bestScore


def ricorsione(self, parziale):
    if self.getScore(parziale) > self._bestScore:
        self._bestScore = self.getScore(parziale)
        self._bestPath = copy.deepcopy(parziale)

    for v in self._graph.neighbors(parziale[-1]):
        if (v not in parziale and  # check if not in parziale
                self._graph[parziale[-2]][parziale[-1]]["weight"] >
                self._graph[parziale[-1]][v]["weight"]):  # check if peso nuovo arco è minore del precedente
            parziale.append(v)
            self.ricorsione(parziale)
            parziale.pop()


### CAMMINO DI PESO MASSIMO AVENTE LUNGHEZZA PARI A LUN
def getOptPath(self, source, lun):
    self._bestPath = []
    self._bestCost = 0

    parziale = [source]

    for n in self._graph.neighbors(source):
        if parziale[-0].classification == n.classification:
            parziale.append(n)
            self.ricorsione(parziale, lun)
            parziale.pop()

    return self._bestPath, self._bestCost

def ricorsione(self, parziale, lun):
    if len(parziale) == lun:
        # allora parziale ha la lunghezza desiderata,
        # verifico se è una soluzione migliore,
        # ed in ogni caso esco
        if self.costo(parziale) > self._bestCost:
            self._bestCost = self.costo(parziale)
            self._bestPath = copy.deepcopy(parziale)
        return

    # se arrivo qui, allora parziale può ancora ammettere altri nodi
    for n in self._graph.neighbors(parziale[-1]):
        if parziale[-0].classification == n.classification and n not in parziale:
            parziale.append(n)
            self.ricorsione(parziale, lun)
            parziale.pop()

def costo(self, listObjects):
    totCosto = 0
    for i in range(0, len(listObjects) - 1):
        totCosto += self._graph[listObjects[i]][listObjects[i + 1]]["weight"]
    return totCosto

### insieme di K oggetti
def getDreamTeam(self, k):
    self._bestPath = []
    self._bestScore = 1000

    parziale = []
    self.ricorsione(parziale, k)
    return self._bestPath, self._bestScore


def ricorsione(self, parziale, k):
    if len(parziale) == k:
        if self.getScore(parziale) < self._bestScore:
            self._bestScore = self.getScore(parziale)
            self._bestPath = copy.deepcopy(parziale)
        return

    for n in self._graph.nodes():
        if n not in parziale:
            parziale.append(n)
            self.ricorsione(parziale, k)
            parziale.pop()

def getScore(self, team): # la somma degli oggetti nell'insieme è la somma dei pesi con gli oggetti fuori dall'insieme
        score = 0
        for e in self._graph.edges(data=True):
            if e[0] not in team and e[1] in team:
                score += e[2]["weight"]
        return score

### PERCORSO CHE MASSIMIZZI LA SOMMA DEI PESI TRA DUE NODI
def getCamminoOttimo(self, v0, v1, t):
    self._bestPath = []
    self._bestObjFun = 0

    parziale = [v0]

    self.ricorsione(parziale, v1, t)

    return self._bestPath, self._bestObjFun

def ricorsione(self, parziale, v1, t):
    # Verificare se parziale è una possibile soluzione
    # verificare se parziale è meglio del best
    # esco
    if parziale[-1] == v1:
        if self.getObjFun(parziale) > self._bestObjFun:
            self._bestObjFun = self.getObjFun(parziale)
            self._bestPath = copy.deepcopy(parziale)

    if len(parziale) == t + 1:
        return

    # Posso ancora aggiungere nodi: prendo i vicini e aggiungo un nodo alla volta
    for n in self._graph.neighbors(parziale[-1]):
        if n not in parziale:
            parziale.append(n)
            self.ricorsione(parziale, v1, t)
            parziale.pop()

def getObjFun(self, listOfNodes):
    objval = 0
    for i in range(0, len(listOfNodes) - 1):
        objval += self._graph[listOfNodes[i]][listOfNodes[i + 1]]["weight"]
    return objval

### PERCORSO PIù LUNGO IN TERMINI DI ARCHI (SENZA CONSIDERARE IL PESO)
# SI PUò AGGIUNGERE UN ARCO SOLO SE IL SUO PESO è MAGGIORE DI TUTTI I PESI GIà PRESENTI
def searchPath(self, product_number):
    nodoSource = self.idMap[product_number]
    parziale = []
    self.ricorsione(parziale, nodoSource, 0)
    print("final", len(self._solBest), [i[2]["weight"] for i in self._solBest])

def ricorsione(self, parziale, nodoLast, livello):
    archiViciniAmmissibili = self.getArchiViciniAmm(nodoLast, parziale)

    if len(archiViciniAmmissibili) == 0:
        if len(parziale) > len(self._solBest):
            self._solBest = list(parziale)
            print(len(self._solBest), [ii[2]["weight"] for ii in self._solBest])

    for a in archiViciniAmmissibili:
        parziale.append(a)
        self.ricorsione(parziale, a[1], livello + 1)
        parziale.pop()

def getArchiViciniAmm(self, nodoLast, parziale):
    archiVicini = self._grafo.edges(nodoLast, data=True)
    result = []
    for a1 in archiVicini:
        if self.isAscendent(a1, parziale) and self.isNovel(a1, parziale):
            result.append(a1)
    return result

def isAscendent(self, e, parziale):
    if len(parziale) == 0:
        print("parziale is empty in isAscendent")
        return True
    return e[2]["weight"] >= parziale[-1][2]["weight"]

def isNovel(self, e, parziale):
    if len(parziale) == 0:
        print("parziale is empty in isnovel")
        return True
    e_inv = (e[1], e[0], e[2])
    return (e_inv not in parziale) and (e not in parziale)