# Face Recognition

Una volta effettuata l’operazione di detection, ovvero una volta individuato il volto all’interno di un’immagine, successivamente si procede all’estrazione di questo volto dall’immagine, precisamente le caratteristiche del volto che permettono di effettuarne il riconoscimento. Per poter fare il riconoscimento del volto bisogna avere un template, ovvero un modello corrispondente affinché possa essere confrontato e verificato. 

In precedenza, si è accennato che un sistema di riconoscimento biometrico prevede due fasi: Enrollment in cui si crea il template, dove il dato viene acquisito attraverso un sensore e le informazioni estratte con l’image processing vengono catalogate sotto forma di template in un database. Questo processo può essere effettuato singolarmente o in blocco (batch Enrollment). L’altra fase, quella di Testing prevede l’acquisizione nuovamente dei dati attraverso la stessa tipologia di sensore, l’estrazione delle caratteristiche e il recupero del template dal database per il confronto con i dati estratti. Attraverso una soglia di tolleranza si verifica se il matching produce un risultato positivo o negativo.

## Approcci alla Face Recognition

In letteratura esistono svariati approcci di tecniche di face Recognition.

### ICA & PCA

Tra le tecniche più utilizzate soprattutto in passato per il Face Recognition c’è la PCA (Principal Component Analysis) che rientra nella categoria delle Image Based. Tale tecnica sotto alcuni aspetti ricorda la trasformata di Fourier, ma con un approccio totalmente diverso. Piuttosto che considerare i pixel, essi vengono associati a delle variabili geometriche. Vettori (le direzioni) in cui è massima la variazione (varianza) tra i vettori stessi. L’obiettivo principale della PCA è di individuare dei vettori che siano efficienti per rappresentare determinati dati. Si veda in figura, ad esempio si supponga di avere due classi di dati A e B; nella prima rappresentazione non è possibile affermare che il vettore possiede una direzione rappresentativa della classe A o della classe B, infatti la rappresentazione non indica il comportamento delle due classi. 

Esse, pur avendo dati distinti, possiedono delle caratteristiche in comune, ovvero una distribuzione delle informazioni rispetto al piano cartesiano piuttosto simile. Nella seconda rappresentazione invece, il vettore è rappresentativo delle due classi; infatti il vettore e le due classi condividono la direzione e quindi il coefficiente angolare della retta associata. Si assuma di avere delle immagini quadrate di dimensione N, in cui il numero di pixel risulta essere N*N. Con M il numero di immagini del database e P il numero di persone coinvolte all’interno del database; quindi con M diverso da P (per ogni persona si possono avere più immagini nel database). 

L’algoritmo della PCA non fa nient’altro che cercare di individuare all’interno di un insieme di immagini, le immagini più significative; quindi tentare di trovare un numero di immagini molto più piccolo di M tale che queste immagini siano rappresentative di tutto il dataset. Quindi trovare una strategia che in presenza di un dataset molto corposo, possa dare in output un insieme molto più piccolo di immagini significative. Tali immagini significative possono rappresentare tutto il dataset; riassumendo si tenta di ridurre il problema di rappresentazione ad un problema più piccolo trasformando la dimensionalità del problema. 

L’idea è quella di rappresentare ogni volto attraverso la combinazione lineare dei volti più significativi, i cosiddetti Eigenfaces. Quindi ogni volto significativo contribuirà alla rappresentazione di un volto all’interno dell’immagine.

### Eigenfaces

Si prendono in input le immagini e per ognuna di esse si effettua una linearizzazione, ovvero ogni immagine viene rappresentata come vettore, si calcola la media su tutti i quanti i vettori e tale media viene sottratta da ciascun vettore. Quest’ultima operazione fa in modo che venga rimossa la parte in comune tra tutti i volti, ottenendo quindi le immagini che andranno a costituire la base per la matrice di covarianza; si scelgono le immagini meno correlate tra di loro (quelle più vicine ad essere linearmente indipendenti). Una volta individuato l’insieme dei vetri (immagini) meno correlate, è possibile rappresentare tutta la base di dati attraverso una combinazione lineare degli Eigenfaces. Quindi la scelta delle immagini più indipendenti e più significative permette la generazione di tutta quanta la base di dati.

Riassumendo, il principio alla base della PCA è la ricerca all’interno della base di dati delle immagini meno correlate aspettandosi che esse siano dal punto di vista numerico molto inferiore alla dimensione dell’intero database. Quindi, se il database possiede M immagini, si cercano k immagini con k molto piccolo, tale da poter rappresentare tutte le immagini del database attraverso la combinazione lineare delle k scelte. Esse vengono scelte grazie alla matrice di covarianza che permette di stabilire quali immagini risultano essere meno correlate tra esse; meno le immagini sono correlate più sono tra di loro indipendenti. Le immagini vengono assimilate da dei vettori n-dimensionali. La matrice di covarianza permette di stabilire quante sono le immagini. La scelta delle immagini dipende anche dall’accuratezza che si vuol ottenere. Più è piccola la dimensione del set di Eigenfaces scelto, meno è l’accuratezza ottenuta nella rappresentazione delle immagini (maggior errore).

### Neural Networks

Una rete neurale simula il funzionamento dei neuroni nel cervello. Ciascun neurone è rappresentato da una funzione matematica basata sul calcolo delle probabilità. Per il riconoscimento dei volti, l’ottimo sarebbe utilizzare un neurone per ciascun pixel. Questo approccio richiede troppi neuroni. La soluzione consiste nell’utilizzare una rete di neuroni per « riassumere » l’immagine in un vettore più piccolo. Mentre una seconda rete effettua il riconoscimento vero e proprio

### Graph-Based Systems

Attraverso filtri e funzioni di localizzazione vengono localizzati sul volto un insieme di punti di riferimento. Questi punti vengono collegati da archi pesati e si ottiene un grafo. Ad ogni volto è associato un grafo, per cui confrontare due volti significa confrontare due grafi.

### Termogramma

L’immagine del volto viene acquisita mediante un sensore termico. Il sensore rileva le variazione di temperatura dell’epidermide del volto. L’immagine viene segmentata e indicizzata