# funzione per inserire un oggetto in un menù a tendina non solo una stringa

# esempio per inserire un anno, ma si può esportare a qualsiasi oggetto
    def fillDDYear(self):
        years = self._model.getAllYears()
        for year in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(data = year, text = year, on_click=self.handleDDYearSelection))
        self._view.update_page()

    def handleDDYearSelection(self, e):
        if e.control.data is None:
            self._selectedYear = None
        else:
            self._selectedYear = e.control.data
        print(f"Anno selezionato: {self._selectedYear}")


#funzione per creare il grafo
    def handleCreaGrafo(self,e):
        if parametro is None:
            self._view.txt_result.controls.append(ft.Text("Selezionare parametro!", color='red'))
            self._view.update_page()
            return
        self._model.buildGraph(parametro)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato "))
        nodes, edges = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi:{nodes}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi:{edges}"))
        self._view.update_page()


# funzione per gestire l'input di un parametro da parte dell'utente
# può essere sia per la ricorsione che per il grafo o altre cose

VALORE = self._view.campotestualeperinserirevalore.value
        if K == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione, valore non inserito.", color='red'))
            self._view.update_page()
            return

# se è un valore che deve essere intero:
        try:
            intK = int(K)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(
                ft.Text("Attenzione, il valore inserito non è un intero!", color='red'))
            return
