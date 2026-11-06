# Agglomerative Clustering Simulator:Descrizione

**Agglomerative Clustering Simulator** è un progetto Python che implementa da zero l'algoritmo di **Clustering Gerarchico Agglomerativo**, uno dei principali metodi di apprendimento non supervisionato utilizzati nell'ambito del Machine Learning.

L'obiettivo del progetto è mostrare passo dopo passo come un insieme di punti venga progressivamente raggruppato in cluster sempre più grandi utilizzando la **distanza euclidea** come criterio di aggregazione.

Il simulatore è stato sviluppato con finalità didattiche e permette di comprendere in modo pratico il funzionamento del clustering gerarchico, evitando l'utilizzo di librerie di Machine Learning già pronte.

---

## Obiettivi del Progetto

- Implementare il Clustering Gerarchico Agglomerativo.
- Calcolare le distanze euclidee tra i punti.
- Aggregare progressivamente i cluster più vicini.
- Calcolare i centroidi intermedi dei cluster.
- Visualizzare graficamente i dati.
- Generare il dendrogramma finale.
- Comprendere i principi fondamentali del clustering gerarchico.

---

## Dataset Utilizzato

Il simulatore utilizza il seguente insieme di punti bidimensionali:

| Punto | Coordinate |
|---------|---------|
| A | (1, 2) |
| B | (2, 5) |
| C | (3, 5) |
| D | (6, 3) |
| E | (9, 3) |
| F | (10, 4) |

Ogni punto viene inizialmente considerato come un cluster indipendente.

---

## Funzionamento dell'Algoritmo

Il Clustering Gerarchico Agglomerativo segue una strategia **bottom-up**:

1. Ogni elemento rappresenta un cluster.
2. Vengono calcolate le distanze tra tutti i cluster.
3. Si individuano i due cluster più vicini.
4. I cluster vengono uniti.
5. Si ricalcolano centroide e distanze.
6. Il processo continua fino al raggiungimento del numero desiderato di cluster.

---

## Formula della Distanza Euclidea

La distanza tra due punti viene calcolata mediante:

```math
d(p_1,p_2)=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
```

Questa misura rappresenta il criterio utilizzato per decidere quali cluster aggregare durante ogni iterazione.

---

## Evoluzione dei Cluster

### Stato Iniziale

```text
{A}
{B}
{C}
{D}
{E}
{F}
```

---

### Prima Aggregazione

I punti più vicini sono:

```text
B e C
```

Nuovo cluster:

```text
{B,C}
```

---

### Seconda Aggregazione

I punti più vicini successivi sono:

```text
E e F
```

Nuovo cluster:

```text
{E,F}
```

---

### Terza Aggregazione

Il punto A viene aggregato al cluster:

```text
{B,C}
```

ottenendo:

```text
{A,B,C}
```

---

### Quarta Aggregazione

Il punto D viene aggregato al cluster:

```text
{E,F}
```

ottenendo:

```text
{D,E,F}
```

---

## Risultato Finale

Il processo termina con la formazione di due cluster:

```text
Cluster 1 = {A, B, C}

Cluster 2 = {D, E, F}
```

I cluster ottenuti rappresentano la suddivisione finale dei dati in base alla vicinanza spaziale degli elementi.

---

## Struttura del Progetto

```text
Agglomerative-Clustering-Simulator/
│
├── dataset.py
├── distanzaEuclidea.py
├── clustering.py
├── dendogramma.py
├── plot.py
├── main.py
└── README.md
└── Figure1.png
└── Figure2.png
└── Figure3.png
└── Output.png
```

---

## Descrizione dei File

### dataset.py

Contiene il dataset iniziale utilizzato per la simulazione.

### distance.py

Implementa il calcolo della distanza euclidea.

### clustering.py

Gestisce la logica di aggregazione dei cluster e l'aggiornamento dei centroidi.

### dendrogram.py

Genera il dendrogramma che rappresenta la storia delle aggregazioni.

### plot.py

Contiene le funzioni di visualizzazione grafica tramite Matplotlib.

### main.py

Punto di ingresso dell'applicazione.

---

## Tecnologie Utilizzate

- Python 3
- Matplotlib
- NumPy (opzionale)

---

## Output Attesi

Il simulatore produce:

- Visualizzazione dei punti iniziali;
- Calcolo delle distanze tra cluster;
- Evoluzione dei raggruppamenti;
- Visualizzazione dei cluster intermedi;
- Dendrogramma finale;
- Risultato conclusivo del clustering.

---

## Possibili Miglioramenti

- Supporto a dataset caricati da file CSV;
- Scelta del numero finale di cluster;
- Single Linkage;
- Complete Linkage;
- Average Linkage;
- Metodo di Ward;
- Interfaccia grafica;
- Analisi di dataset reali.

---

## Finalità Didattica

Questo progetto è pensato per studenti di **Intelligenza Artificiale**, **Machine Learning** e **Data Mining** che desiderano comprendere nel dettaglio il funzionamento del Clustering Gerarchico Agglomerativo attraverso un'implementazione semplice, modulare e completamente sviluppata in Python.

---

## Autore

Progetto realizzato a scopo didattico per l'approfondimento degli algoritmi di clustering gerarchico e delle tecniche di apprendimento non supervisionato.
