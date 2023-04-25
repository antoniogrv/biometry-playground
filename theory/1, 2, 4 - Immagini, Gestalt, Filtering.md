# Principi della Gestalt

L’origine della parola *Gestalt* è tedesca e significa forma. Coniata dallo psicologo tedesco Max Wertheimer nel 1910. Dopo alcuni esperimenti con uno stroboscopio, concluse che l'occhio semplicemente recepisce tutti gli stimoli visivi e che il cervello organizza le sensazioni in un'immagine coerente. Gli psicologi della Gestalt hanno ulteriormente perfezionato il lavoro di Wertheimer per concludere che la percezione visiva era il risultato dell'organizzazione in vari gruppi di elementi o forme sensoriali. **Gli elementi discreti all'interno di una scena sono combinati e compresi dal cervello attraverso una serie di quattro leggi di raggruppamento, secondo le quali "il tutto è diverso dalla somma delle sue parti."**

L'idea di base della psicologia della Gestalt è che le caratteristiche sensoriali (linee, bordi, angoli, colori, ecc.) sono combinate dal cervello per formare un nuovo modello o configurazione, per produrre qualcosa che non esiste nell'insieme delle caratteristiche prese uno per uno.

La Gestalt differenzia sensazione e percezione come segue. 
- *Sensazione*: Il processo attraverso il quale i sensi raccolgono stimoli visivi, uditivi e altri stimoli e li trasmettono al cervello.
- *Percezione*: Il processo mediante il quale le informazioni sensoriali sono organizzate e interpretate attivamente dal cervello.

I principi della psicologia della Gestalt sono i seguenti. 
- **Figure-Ground**: l'organizzazione dipende da ciò che vediamo come figura (oggetto) e da ciò che percepiamo di fondo (contesto). 
- **Legge di prossimità**: gli oggetti vicini nello spazio o nel tempo sono percepiti come appartenenti ad un solo insieme. 
- **Legge della somiglianza**: gli oggetti che hanno caratteristiche simili sono percepiti come unità. 
- **Legge della continuità**: tendiamo a percepire figure o oggetti come appartenenti ad un insieme se sembrano formare un modello continuo. 
- **Legge della chiusura**: rileviamo che le figure con delle lacune siano complete. 

Un'*illusione* è una distorsione di una percezione sensoriale o cognitiva, causata dal modo in cui il cervello è solito organizzare ed interpretare le informazioni che riceve. Le illusioni possono coinvolgere tutti i sensi, ma quelle ottiche sono le più emblematiche e conosciute. Illusioni ben note sono quella di Adelson (scacchiera con due grigi che sembrano uguali ma sono diversi; la causa ricade sulle strategie che il nostro sistema visivo adotta per "allocare" le sfumature definite dalle ombre nella foto) e l'illusione della Thatcher (foto della politica con occhi girati di 180 gradi; girando però la foto il nostro sistema visivo, a causa di uno specifico modulo del sistema cognitivo, non riconosce la malconfigurazione della foto).

# Immagini e digitalizzazione

A partire da un'immagine del mondo reale, applicando una tecnica di Image Processing, si ricava una ulteriore immagine che differisce dalla precedente per una qualche motivazione, provando ad estrarre degli aspetti qualificanti (si pensi alla radiografia in campo medico per evidenziare una anomalia -- però, in questo caso, la rilevazione dell'anomalia è 'automatica', ma non collegata ad un intervento esterno come avviene per la Computer Vision). Quando invece si effettua una operazione di Computer Vision, si collega un qualche aspetto dell’immagine del mondo reale, a qualcosa di più astratto quello che risiede nel mondo della conoscenza. La Computer Vision risulta essere una evoluzione rispetto all’Image Processing, dove quest’ultima non fa nient’altro che trasformare i pixel senza interpretarli. Invece la Computer Vision assegna a questi pixel un significato sulla base di una informazione fornita da un esperto, interpretando il contenuto semantico dell’immagine sulla base di un dominio di competenza. La modellazione geometrica rappresenta oggetti astratti e la Computer Graphics li rende visibili sottoforma di immagine. Da ciò che si è spiegato in precedenza si può capire che l’Image Processing risulta essere un’attività di basso livello, siccome essa non si addentra nella semantica dei pixel. Man mano che ci si muove sulla linea, si va verso la Computer Vision ovvero quelle tecniche di elaborazione che tentano di capire cosa è presente dentro l’immagine, considerata un’attività di alto livello.

### Proprietà di un'immagine
- **Intensità dell’immagine**: è l’energia luminosa emessa da un singolo punto dell’immagine e dipende dal dispositivo. 
- **Luminosità dell’immagine**: il dispositivo emette una certa intensità luminosa che viene percepita dal soggetto sotto forma di luminosità. Essa è ciò che viene percepito della luminosità emessa da un singolo pixel. 
- **Contrasto dell'immagine**: dovrebbe fornire una idea di quanto gli elementi presenti in una immagine sono distinti uno dall’altro. 
- **Risoluzione dell'immagine**: la risoluzione lega il campionamento e la dimensione fisica. Va divisa in due elementi: Temporale e Spaziale. 
    - *Temporale* (per i video): definisce il numero di immagini al secondo da usare (FPS). Per la visione umana si usano da 15 a 30 immagini al secondo. Al di sotto di tale valore vi è una bassa risoluzione temporale. 
    - *Spaziale* (singole immagini): definisce il numero di pixel da usare (in alternativa DPI, dot per inch: il numero di pixel al centimetro).

### Legge di Weber
Un altro esempio relativo alla luminosità, ovvero alla capacità umana di percepire variazioni di luminosità è legata alla Legge di Weber. Esso posizionava un utente di fronte a uno schermo, il quale nella porta posteriore (non visibile all’utente) aveva un cannone luminoso che sparava una certa intensità luminosa. Succedeva che lo schermo veniva illuminato con una certa intensità `L` e il centro dello schermo veniva illuminato con `L + δ(L)`. Inizialmente il centro dello schermo aveva la stessa intensità dello sfondo senza esser percepita nessuna differenza. Facendo variare le due intensità, si chiedeva all’utente fin quando fosse stato possibile individuare queste variazioni di intensità. **Weber ha dedotto che l’essere umano possiede una buona capacità di discriminazione quando L è basso, quindi una luminosità scura. Man mano che L cresce la capacità nel notare variazioni di luminosità diventa meno forte.** Quindi se si vuol percepire una variazione di luminosità con un `L` molto grande, deve essere prodotto un `δ(L)` molto grande. Mentre con un `L` molto piccolo si è in grado di percepire una variazione di luminosità anche molto piccola.

## Image Formation
Il processo di digitalizzazione di una immagine risulta essere molto importante in quanto **digitalizzando una immagine o un video si perde inevitabilmente una parte dell’informazione**. Quando si acquisisce una immagine con una singola sorgente (dispositivo) si passa da una rappresentazione tridimensionale ad una rappresentazione bidimensionale, e questo passaggio da 3D a 2D comporta irrimediabilmente una perdita di informazioni. Fondamentalmente, **si può effettuare la digitalizzazione perché si ha una sorgente luminosa che illumina l’oggetto** per effetto della riflessione dei raggi luminosi sull’oggetto, **il sensore acquisisce le informazioni di rimbalzo sull’oggetto ottenute e produce una rappresentazione digitalizzata dell’immagine**. Vi è l’oggetto tridimensionale, che viene acquisito dal dispositivo il quale all’interno presenta **una rete** che, in ogni posizione, prevede un sensore incaricato ad acquisire una porzione del mondo reale e **trasformare tale acquisizione in termini numerici, calcolando la quantità di luce che viene riflessa in quella determinata posizione convertendola in numero**, composta da pixel.

Questo processo si divide in due fasi:

- *Campionamento*: Il campionamento è l’operazione attraverso la quale si decide quanti sensori utilizzare nella fase di digitalizzazione. Verranno utilizzati in modo progressivo sempre più sensori risultati della moltiplicazione tra numero di righe e numero di colonne. **Man mano che aumentano i sensori e la porzione di acquisizione di ognuna di essa diventa sempre più piccola, l’immagine assume una qualità migliore.**

- *Quantizzazione*: L’altra fase del processo di digitalizzazione di una immagine, oltre al campionamento, è la quantizzazione. **Mentre il campionamento concerne il numero di sensori (pixel) impegnati nella fase di acquisizione, la quantizzazione è legata al numero di livelli di intensità luminosa (colori) che ogni sensore può produrre**. 

## Image Processing
Come si è detto in precedenza una immagine è assimilabile a una funzione tridimensionale `f(x,y)`. 

Quando si effettua una operazione di Image Processing, che definisce una nuova immagine `g` in termini di una immagine esistente `f` effettuando una trasformazione `t`, si trasforma un pixel - senza interpretarne il contenuto - trasformandolo in un pixel diverso. 

Fondamentalmente si possono effettuare varie tipologie di trasformazioni sull’immagine, sulla base anche delle immagini che si hanno a disposizioni, come: 
- *Immagini binarie*, ovvero in bianco e nero, con un bit per pixel. 
- *Immagini in scala di grigio*, dove oltre al bianco e il nero vi sono varie sfumature di grigio, e la quantità di sfumature in termini di livelli di grigio, dipendono dalla quantizzazione. Una quantizzazione a 8 bit, si avranno complessivamente 256 colori, dove 0 è nero, 255 bianco e le restanti sono sfumature di grigio. 
- *Immagini a colori*, dove si compone ogni singolo pixel attraverso una serie di componenti che dipendono dal modello di colore che si utilizza. 

## Image Enhancement
Una misura importante che può essere assegnata all’immagine è quella dell’**istogramma**. Non è nient’altro che una rappresentazione statistica dell’immagine, attraverso il quale è possibile avere una **distribuzione dei livelli di grigio**. 

**Si ha il numero di occorrenze per ogni tipologia di colore presente nell’immagine.** Sull’asse delle ascisse viene rappresentato il risultato della quantizzazione, ovvero il numero di colori rappresentabili. L’asse delle ordinate riporta il numero di occorrenze per ognuno dei colori. Ciò significa che **ognuno dei picchi rappresenta quante volte il colore corrispondente è rappresentato nell’immagine**. 

Se una foto è poco contrastata, l’istogramma assumerà la forma di una campana molto stretta concentrata in pochi colori. Quando un istogramma si presenta in questa modalità, si può effettuare una operazione di **Equalizzazione dell’istogramma**, andando a stiracchiare l’istogramma per ottenere una redistribuzione dei colori. Poiché ogni colore rappresenta un certo numero di pixel, la somma delle occorrenze di tutti i colori darà come risultato il numero totale di pixel. L'equalizzazione ha l'obiettivo di rendere l’istogramma il più piatto possibile.

 # Image Filtering
 
 In generale una **trasformazione dell’immagine** è caratterizzata nel seguente modo: `g(x,y) = T[f(x,y)]`, dove: 
 - `f` è l’immagine input 
 - `g` è l’immagine elaborata 
 - `T` è l’operatore di trasformazione applicata ai singoli pixel dell’immagine

L’operatore che si applica all’immagine può avere diverse caratteristiche matematiche. 

Gli operatori lineari godono delle seguenti proprietà:
- **Omogeneità**: `T[αf(x,y)] = αT[f(x,y)]` 
- **Associatività**: `T[f(x,y) + g(x,y)] = T[f(x,y)] + T[g(x,y)]`

Il fatto che un operatore possa essere lineare o meno non ha un impatto sulla tipologia di trasformazione che si va ad applicare. Innanzitutto, va fatta una classificazione delle trasformazioni `T` che possono essere applicate ad una determinata immagine/video: 
- **Tecniche operanti nel dominio spaziale**, ovvero dove vi è una manipolazione diretta dei pixel. 
- **Tecniche operanti nel dominio delle frequenze** (trasformata di Fourier), ovvero vi è una trasformazione dell’immagine nel dominio delle frequenze e conseguente manipolazione di esse. Tali frequenze non agiscono sui pixel ma agiscono su una trasformazione dei pixel. Come si può intuire, tali tecniche implicano un costo computazionale aggiuntivo compensato da una qualità della trasformazione dell’immagine migliore. 
- **Tecniche ibride**, ovvero una combinazione di varie tecniche.

L’altro elemento che si può aggiungere nell’ottica della classificazione delle tecniche è quello che permette di dividere le tecniche di trasformazione in 4 famiglie. 
- **Point Operations**: il pixel di destinazione dipende solo dal pixel di partenza. 
- **Local Operations**: il pixel di destinazione dipende da un pixel di partenza e da un suo intorno quadrato. 
- **Object Operations**: il pixel di destinazione dipende dal pixel di partenza e da un oggetto che ha un suo significato semantico non di forma regolare. 
- **Global Operations**: ogni pixel dell’immagine di destinazione dipende da tutti i pixel dell’immagine di partenza. 

## Point Operations

Si analizza ora qualche semplice trasformazione partendo con il Point Processing, dove ogni pixel di destinazione dipende solo dal corrispettivo pixel di partenza. 

Sull’asse delle ascisse si hanno i *gray levels* (livelli di grigio dell’immagine di partenza), `r` invece rappresenta il valore output e `T` effettua la trasformazione. 

### Binarizzazione

`T` è una funzione monotona crescente. I valori ottenuti in fase di digitalizzazione, mappati sull’asse delle ascisse, sono valori che devono essere distribuiti soltanto su due colori, ovvero il bianco e il nero. Ottenendo un’immagine di output, appunto, bianco e nera. Oltre alla binarizzazione, agendo sui due cerchi è possibile anche effettuare il *Contrast Stretching* dell’immagine, operando direttamente sull’istogramma per migliorare il contrasto dell’immagine in questione. Questa trasformazione individua una soglia entro 110 (variabile), dove **tutti i colori da 0 fino a 110 diventeranno nero**, e **tutti i colori che partono da 110 fino a 255 diventeranno bianco**. Ottenendo la stessa immagine di partenza, ma binarizzata. 

### Negativo

Per ogni pixel della sorgente, `T` ne ottiene una trasformazione che lo porta ad assumere un nuovo valore lungo la retta `T(s)`. Questa trasformazione che si sta effettuando, `T(s)`, è una trasformazione monotona decrescente, che prende il nome di *negativo*. 

Vi è un'immagine col proprio instagramma. **Produrre il negativo di tale immagine significa associare ad ogni pixel il livello di grigio complementare.** Infatti, tra le due immagini intercorre una differenza specifica: i pixel chiari diventano più scuri e viceversa.

## Local Operations

Andando avanti ci si concentra sulle Local Operations, dove la trasformazione `T` è definita in un intorno predefinito di `(x, y)`. Si possono individuare tre categorie di filtri che si andranno ad applicare alle immagini: 
- **Lowpass** (passa basso): attenua o elimina le alte frequenze, ovvero contorni e dettagli. Si dividono in lineari (es. Media) e non lineare (es. Mediana).
- **Highpass** (passa alto): attenua o elemina le basse frequenze, come contrasto e intensità. 
- **Bandpass** (passa banda): attenua frequenze in una banda predefinita. 

### Filtri Spaziali

I filtri spaziali rientrano nella categoria delle Local Operations dove ogni pixel di destinazione dipende dal pixel di partenza più il suo intorno. Per essere costruiti, in genere vengono create delle mascherine quadrate, generalmente di dimensioni dispari 3x3, 5x5 ecc… e dentro tali mascherine verranno posti dei pesi, che chiaramente andranno a determinare la funzionalità del filtro. Sulla base dei valori dei valori distribuiti all’interno della mascherina si otterrà un risultato diverso. Una volta costruita, essa si sovrapporrà all’immagine centrandola nel pixel `(x, y)` e si effettuerà la moltiplicazione tra ciascuno di questi pesi con il corrispondente valore di luminosità presente nell’immagine.

Questa prima classe di filtri verrà utilizzata per costruire i cosiddetti *Smoothing Filter*, cioè i filtri utilizzati nelle operazioni di preprocessing. Infatti, può capitare che l’immagine contenga del “*rumore*” oppure sia troppo ricca di dettagli. Con tali filtri è possibile intervenire, anche se essi possono produrre un effetto di *Blurring* se l’immagine è troppo ricca di dettagli, e quindi se ne vogliono **rimuovere alcuni dettagli per rendere l’immagine più funzionale per l’estrazione di oggetti**. Oppure l’immagine presenta del rumore che può esser stato introdotto o nella fase di digitalizzazione oppure durante la fase di trasmissione.

#### Media

Tale filtro non differisce dal concetto di media aritmetica. **Ogni pixel dell’immagine destinazione viene sostituito con la media dei pixel appartenenti ad un’area ben definita dell’immagine**. Piuttosto che prendere soltanto il pixel `(x, y)` nell’immagine input, viene preso la media di tutti i pixel connessi con il pixel `(x, y)`. Effettuando la media (con la divisione per 9) si ottiene il filtro di destinazione. 

**L’applicazione di un filtro media ad un’immagine/video che presenta rumore viene effettuato proprio per eliminare tale rumore prodotto da un determinato motivo, per ricondurre l’immagine ad una qualità migliore.** Il contorno di un oggetto è una transizione, tra un oggetto e un altro, come una sorta di interruzione.

#### Media Adattiva

È possibile modificare il filtro media per ottenere un risultato qualitativamente migliore. **La media adattiva va a risolvere varie problematiche della media, come la confusione dei contorni.** Ogni qual volta essa viene utilizzata, effettua un confronto tra il pixel `(x, y)` e tutti i pixel che sono nel suo intorno. **In presenza di piccole variazioni si applica la media, ma in presenza di grandi variazioni si lasciano invariati i pixel di riferimento.** Essa lavora sui bordi. Applicando un filtro media sempre più grande, l’immagine tende a sfocarsi e perdere rumore ma anche dettagli. Quindi la media adattiva può essere una soluzione che consente di preservare in parte dettagli e i contorni degli oggetti avendo un buon effetto sulla rimozione del rumore.

#### Mediana 

Un’altra possibile soluzione che può essere utilizzata per rimuovere il rumore è il Filtro Mediana. Esso corrisponde esattamente al concetto di mediana statistica per il quale **si considerano i pixel di una regione, li si ordina in maniera crescente e poi ci si posiziona sul valore centrale**. La mediana è proprio tale valore centrale. Rispetto alla media, la mediana non viene influenzata dalle code, ovvero il valore centrale non viene condizionato particolarmente dalla presenza di significativi cambiamenti agli estremi, cosa che avviene nella media.

#### Smoothing Gaussiano

Il funzionamento del Filtro Gaussiano è simile a quello del filtro mediana con la differenza che **il contributo di ciascun pixel limitrofo ha un peso diverso**, definito dalla distribuzione spaziale della gaussiana. Nel campo dell’elaborazione delle immagini la gaussiana viene troncata limitandone l’estensione ad una zona di dimensioni `N * N` (i valori più frequenti per N sono 3, 4 e 5). Si parte dal presupposto che i pixel in prossimità della zona centrale sono quelli più importanti. Quindi se si vuol posizionare la maschera su un pixel `(x, y)`, non si deve assegnare poi lo stesso peso a tutti gli altri pixel ma si cerca di concentrare la maggior parte del peso in prossimità del pixel `(x, y)`, e progressivamente diminuire il peso dei pixel man mano che ci si allontana dal centro. La somma di tutti i pesi sarà sempre uguale a uno. In prossimità del pixel di riferimento, si assegnerà un valore maggiore. Quindi possono essere costruiti nuovi filtri che, fondamentalmente, sono dei Filtri Media pesati. 

**Mentre prima il peso assegnato dalla media era uguale per tutti quanti, ora si adopera una selezione: più ci si è vicini alla posizione `(x, y)` maggiore sarà il peso in quanto maggiore sarà la probabilità che quel pixel appartenga alla regione di interesse**; più ci si allontana dal pixel (x, y) maggiore sarà la probabilità di non appartenere alla regione di interesse e quindi si cerca di contaminare il meno possibile la trasformazione. Con un filtro gaussiano si riesce ad eliminare le zone di rumore e a preservare gli scalini, proprio perché in prossimità di essi i pixel otterranno una distribuzione di pesi differenziata.

#### SUSAN: Smoothing Segment Univalue Assimiliating Values

Tale filtro esaspera il concetto Gaussiano. Infatti, **permane l’idea di Filtro Gaussiano, ma in questo caso i pesi vengono calcolati run-time**. Quindi viene applicata la maschera all’immagine e si va a controllare quali pixel ricadono nella stessa area del pixel centrale. Si assegneranno pesi alti a tutti i pixel che appartengono all’aerea del pixel centrale e si tenderà a dare peso minore ai pixel che si trovano più in lontananza rispetto al centro. Il filtro SUSAN preserva gli scalini, risultando essere un filtro ottimale fornendo output migliori.

### Filtri di Edge Detection 

Si introduce un’altra classe di filtri che hanno come obiettivo quello di trattenere le informazioni che risiedono nelle alte frequenze, lavorando in modo esattamente speculare a quelli precedenti. **Tali filtri quindi trattengono i punti di controllo**, ovvero i dettagli. **Gli Edge Detector sono filtri che hanno la capacità di individuare le aree di transizione tra regioni omogenee:** 
- *Punti isolati*
- *Linee* (orizzontali, verticali, oblique)
- *Contorni* (insieme di punti con inizio e fine coincidenti)

Come detto, gli edge possono avere forme differenziate; tendenzialmente si identificano come una** variazione di una serie di pixel** o anche un singolo pixel, **che ha una caratteristica ben definita**: ovvero si passa da un’area a transizione costante (vicina alla 0) ad un’area in cui c’è una variazione (o perturbazione). Questa variazione può avere varie forme: rampa, scalino, ecc… Tra le possibili situazioni di transizione tipiche vi sono quelle a rampa e scalino. Il contorno a scalino presenta una transizione brusca tra due zone uniformi, invece nella transizione a rampa il passaggio tra le due regioni risulta essere più attenuato. 

**L’obiettivo è quello di individuare una sorta di detector che vada a mettere in evidenza le cime più alte delle variazioni di luminosità.** Si supponga di avere una rappresentazione di un’immagine con una certa variabilità di toni di grigio. Sull’asse dell’ascisse vi sono i pixel e sull’asse delle ordinate i valori di grigio. Se viene calcolato la derivata prima della funzione in questione, si avrà come risultato delle informazioni sulla presenza di variazioni; quindi la derivata prima risulta essere uguale a zero quando non vi sono valori significativi e risulta avere una variazione laddove esiste una variazione dei livelli. 

Ritorna ad esser costante in presenza della zona uniforme, per poi trovare un’altra variazione e terminare in modo uniforme. **Quello che si vuol fare è capire se questi punti di massimo e minimo individuati dalla derivata prima possano essere significativi**. Quindi si vuol individuare una soglia che può dare informazioni circa i punti individuati al fine di comprendere se possono essere variazioni utili ad individuare un passaggio da un’area uniforme ad un’altra. Questi pixel presi singolarmente o in modo aggregato, sono quelli che possono essere potenzialmente etichettati come pixel di transizione ovvero Edge Pixels. **La difficoltà fondamentale è capire la soglia utile, e se essa può essere resa universale oppure deve essere adattata a classi di immagini**, e se viene individuata per classi di immagini si può esser sicuri che questa soglia vada bene per tutta quanta l’immagine. Ovviamente *NO* in quanto la soglia è molto difficile da individuare e non sempre quella individuata per classi di immagini vada bene. 

Spesso tale soglia all’interno della stessa immagine permette sia di individuare pixel significativi ma individua potenziali pixel di contorno che non risultano esserlo. Questo pone un limite dell’applicazione di tali filtri alle immagini digitali. 

#### Punti Isolati

I punti isolati sono le discontinuità più semplici da individuare, in quanto non contribuiscono a definire la morfologia di un oggetto.  Anche in questo caso, quando si individua un punto isolato affinché tale punto possa essere etichettato come punto di discontinuità, deve esserci una soglia `T` che viene individuata. 

Tale soglia `T` deve far sì che una volta applicata la maschera ad una determinata area, ed una volta calcolato il valore `R`, si è in grado di etichettare il pixel a cui corrisponde `R` come pixel di edge, soltanto se il valore è abbastanza significativo. Quindi **il valore di grigio di quel punto isolato deve essere abbastanza differente da quello dei suoi vicini**. Se non vi è tale differenza evidente, non si può etichettare questo come punto isolato.

Quindi, **in linea col concetto di derivata prima, questo filtro deve garantire che quando viene applicato all’immagine si dovrà avere che, nelle zone uniformi, il risultato deve essere zero, quindi il pixel kernel non è un pixel candidato.** Quando invece si trovano delle variazioni, esse devono essere evidenziate. Il principio portante di tali maschere, come detto, è che **la somma dei pesi deve essere uguale a zero**, per assicurare il concetto di rapporto incrementale. Quest’ultimo sarà nullo nelle aree in cui non c’è variazione, e **ci sarà un rapporto incrementale evidente positivo o negativo quando esiste una variazione**. 

#### Linee

È possibile costruire dei filtri che sono capaci di individuare non soltanto i punti, ma anche le linee, quindi privilegiare quei **pixel che sono presenti lungo linee uniformi di variazione**. Come il filtro precedente, hanno la caratteristica di avere **pesi negativi e positivi**, e **la somma di tuti i pesi è uguale a zero**. Ognuno dei filtri riesce ad individuare una particolare caratteristica di linea. 

Il primo individua punti di contorno che hanno uno sviluppo orizzontale, il secondo invece punti di contorno che hanno uno sviluppo prevalentemente obliquo, il terzo punti di contorno che hanno uno sviluppo prevalentemente verticale, ed infine il quarto individua punti di contorno che hanno uno sviluppo obliquo ma con un senso rispetto al secondo. 

La prima maschera risponde più intensamente alle linee orizzontali: con uno sfondo costante, il massimo di `R` si ha infatti quando la linea coincide con la riga centrale della maschera.  Analogamente, la seconda maschera risponde meglio a linee orientate a 45°, la terza a linee verticali e la quarta a linee orientate a 45°. Si supponga di passare tutte e quattro le maschere su una immagine, e che in un certo punto si avranno `R1, R2, R3, R4` risposte diverse delle quattro maschere. Per capire se il pixel appartiene potenzialmente ad una maschera bisogna verificare quale valore `Ri` risulta essere più grande rispetto agli altri; una volta individuato tale valore, allora il punto di edge che si sta etichettando è associato alla maschera `Ri` e si trova lungo una linea specifica di quella determinata maschera. 

#### Contorni

L’estrazione dei contorni è sicuramente uno degli argomenti che hanno ricevuto più attenzione nella letteratura sull’image processing. **Il contorno di un oggetto rappresenta infatti la separazione tra l’oggetto e lo sfondo o tra l’oggetto ed altri oggetti**, per cui la sua estrazione è molto spesso il primo passo verso l’individuazione dell’oggetto. Un edge si presenta in una immagine come il confine tra due regioni caratterizzate da proprietà dei livelli di grigio in qualche modo distinguibili. Nel seguito si ipotizzerà che le regioni in questione siano sufficientemente omogenee, di modo che la determinazione della transizione tra le due regioni sia possibile sulla sola base della discontinuità dei valori di grigio. Le prime tecniche di edge detection che verranno analizzate sono basate sull’applicazione di un operatore locale di derivata. 

**Per rendere le regioni sufficientemente omogenee tra loro è possibile applicare uno *Smoothing* in modo che vengano individuate soltanto le variazioni importanti.** Per costruire dei filtri di edge detector basati sul principio di derivata:
- si prende una mascherina di dimensione dispari 3x3, 5x5, ecc… 
- si assegnano i pesi in modo tale che essi siano tra di loro bilanciati con valori positivi e negativi e assicurando che la somma sia uguale a zero. 

**Uno dei problemi che si presenta è quello di stabilire se è necessario introdurre una soglia.** L’introduzione di una soglia è una delle problematiche più importanti nelle fasi di costruzione degli edge detector. 

Un edge detector trasforma un’immagine in una immagine bianca e nera, e quindi con solo due livelli di grigio, in quanto un edge detector deve solo stabilire se ogni pixel di partenza è un pixel di contorno oppure no. Se un pixel non è di contorno viene etichettato come nero (valore 0), se un pixel è di contorno viene etichettato come bianco (valore 255). 

La scelta della *Threshold* (soglia) è fondamentale per stabilire quali sono i pixel tendenzialmente candidabili a diventare pixel di contorno; quindi una volta stabilita la soglia, tutti i pixel che si trovano al di sopra della soglia sono pixel di contorno, viceversa se si trovano sotto tale soglia non sono pixel di contorno. Infine, c’è una fascia grigia, che potrebbe oscillare tra una soglia troppo bassa o troppo alta. 
- Con **Low Threshold** si individuano potenziali pixel di contorno anche pixel che hanno variazioni piuttosto piccole. Tali variazioni possono introdurre come potenziali pixel di contorno anche pixel che non lo sono.
- Con **High Threshold** si corre il rischio di ridurre troppo il numero di pixel che vengono etichettati come pixel di contorno, dando come risultato finale una quasi scomparsa totale della morfologia dell’oggetto.

**Il fatto che la derivata prima e la derivata seconda del profilo siano significativamente diverse da 0 soltanto in corrispondenza alle transizioni costituisce la motivazione dell’uso di operatori derivativi per l’estrazione dei contorni.** La derivata prima del profilo è positiva in corrispondenza di una transizione scuro-chiaro, negativa in corrispondenza di una transizione chiaro-scuro, nulla nelle zona a livello di grigio costante. 

La derivata seconda è positiva in prossimità di un contorno, dalla parte scura del contorno stesso, negativa dalla parte chiara del contorno, nulla nelle zone a livello di grigio costante, ed esibisce un passaggio per lo zero (zero crossing) esattamente in corrispondenza delle transizioni. Ovvero, la derivata prima indica la presenza di un massimo, la derivata seconda fornisce l’esatta posizione del massimo, nella posizione in cui il rapporto incrementale smette di crescere per iniziare la decrescita.

**Riassumendo, il valore della derivata prima può essere utilizzato per determinare la presenza di contorni in una immagine. Gli zero crossing della derivata seconda ne possono consentire la precisa localizzazione. Il segno della derivata seconda permette di stabilire l’appartenenza di un pixel al versante scuro o al versante chiaro di un contorno. L’applicazione dei concetti precedentemente illustrati necessita tuttavia di alcune cautele, essenzialmente legate alla natura digitale delle immagini.**

#### Utilizzo del gradiente

Il gradiente rappresenta uno degli strumenti attraverso il quale si può cercare di individuare le zone di transizione. **Del gradiente è possibile calcolare due informazioni: l’entità del gradiente** (la grandezza della variazione) e **la direzione del gradiente** (in che direzione si muove il contorno). La direzione dell’edge è quella perpendicolare rispetto al gradiente.

#### Laplaciano

**Il Laplaciano è una rappresentazione della derivata seconda che, a differenza del gradiente, è caratterizzato dall’avere un pixel centrale positivo, le direzioni principali con valori negativi, e gli altri posti uguali a zero.** Si prendono i coefficienti della derivata seconda della funzione `(x, y)` rispetto a due variabili. Questi, poi, costituiscono i coefficienti che si andranno a riprodurre all’interno della matrice. Questa rappresentazione del Laplaciano è la rappresentazione discreta di una derivata seconda.

### Canny Edge Detector

Uno degli operatori maggiormente utilizzati per estrarre i contorni è l’operatore canny edge detector, il quale si è dimostrato molto efficace. Questo operatore mette insieme tutto ciò che è stato detto finora, e sperimentalmente si è visto che è in grado di produrre risultati molto significativi. Questo perché **il metodo di Canny ha un’elevata possibilità di produrre edge connessi, cioè contorni chiusi o piuttosto continuativi** che sono uno degli obiettivi che si ricercano all’interno delle operazioni di edge detection. L’algoritmo di Canny prevede: 
1. Smoothing gaussiano dell’immagine, per eliminare le piccole transazioni. 
2. Calcolo del gradiente. 
3. Soppressione dei non-massimi in direzione ortogonale all’edge. 
4. Selezione degli edge significativi mediante isteresi. 

La qualità del risultato dell’operatore Canny dipende da: 
- Ampiezza della gaussiana nella prima fase. 
- Dimensione del filtro nella prima fase. 
- Soglie per l’isteresi nell’ultima fase. 

#### Sharpening 

Un’operazione di sharpening tende ad evidenziare i dettagli fini, attraverso un’operazione che prevede prima l’**estrazione dei contorni e poi la sovrapposizione dei contorni con l’immagine originale**. Dopo aver estratto i contorni, essi vengono sovrapposti all’immagine per renderli ancor più evidenti. 