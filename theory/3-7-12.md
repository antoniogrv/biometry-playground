# Introduzione alla biometria

Dal greco bios (vita) e metros (misura), la **biometria** è basata sul riconoscimento automatico di una persona sulla base di caratteristiche discriminanti. La biometria è la disciplina che si occupa di misurare tratti fisiologici e comportamentali degli esseri viventi, offrendone una rappresentazione quantitativa attraverso modelli matematici e statistici per costruirne un template ed effettuare eventuali confronti. Per poter utilizzare una biometrica nel contesto forense, è necessario che esse rientrino in una normativa, affinché esse siano legalmente valide. L’utilizzo della biometria in un contesto ampio comporta una serie di problemi: utilizzato come strumento di riconoscimento e tracciamento di una persona, può intaccare alcuni aspetti etici e della privacy.

Il problema della biometria, di una certa rilevanza, corrisponde al verificare se l’identità dichiarata corrisponde all’identità reale. I processi di autenticazione di un soggetto possono essere molto diversificati. Ovvero un processo di associazione dell’identità ad un soggetto attraverso un processo di verifica o riconoscimento. Queste metodologie presentano dei limiti come ad esempio, in presenza di un PIN (login e password), è possibile dimenticarlo oppure essere carpito da un impostore. Anche nel caso delle chiavi fisiche (smart card) che si possono rompere o perdere. Questi sistemi non consentono la distinzione tra il reale possessore e un impostore. Per superare i limiti dei sistemi di autenticazione attualmente in uso. Si deve superare il meccanismo di autenticazione tradizionale basato sul concetto che l’utente possiede, spostando l’attenzione su qualcosa che “l’utente è effettivamente”. 

Le tecnologie biometriche costituiscono metodi automatizzati di verifica o riconoscimento dell’identità di una persona, basati sul rilevamento di una o più caratteristiche fisiologiche o comportamentali dell’individuo, oppure il confronto con una immagine precedentemente acquisita. 

I principi portanti (ad alto livello) della biometria sono: 
- Ogni persona è unica, dove alcune biometrie sono più specifiche di altre. 
- Individuazione delle caratteristiche somatiche che rendono unico un individuo. 
- Metodologie per la misurazione e quantificazione di tali caratteristiche. 
- Classificazione degli individui sulla base delle misure effettuate.

I livelli di autenticazione normalmente utilizzati dipendono dal livello di sicurezza che si intende raggiungere.

Partendo dal basso, si individuano i livelli di sicurezza meno forti, come ad esempio quelli legati a qualcosa che si conosce. Un livello superiore è il cosiddetto token, basato su qualcosa che si deve avere. Infine, vi è un’informazione biometrica, fisiologica o comportamentale, quindi qualcosa che realmente “si è”.

Parlando di caratteristiche biometriche è possibile effettuare una classificazione: ci sono le caratteristiche biometriche statiche o fisiologiche e le caratteristiche dinamiche o comportamentali. Le prime, tendenzialmente, hanno una loro stabilità nel tempo ma soprattutto non dipendono dal comportamento della persona e non possono essere variate sulla base di aspetti emotivi. Viceversa, le caratteristiche dinamiche dipendono fortemente dagli aspetti emotivi della persona, e possono essere anche variabili, avendo un impatto sulla base di aspetti emotivi o legati alla salute o stile di vita. 

Un sistema biometrico in grado di operare sulle componenti appena descritte, che possano essere trattate in maniera automatica. Di seguito uno schema di un sistema biometrico generico: Un sensore che sia in grado di trasformare l’informazione biometrica in un segnale digitale. Una volta digitalizzato tale dato, vengono estratte delle caratteristiche, che dipendono dal tipo di biometrica utilizzata. Tali caratteristiche saranno la base della creazione del modello matematico (template). Questo modello diviene il template rispetto al quale, successivamente si faranno operazioni di verifica e riconoscimento. Con la creazione del template, si è in grado di poter riconoscere un determinato individuo, riacquisendolo in maniera analoga a come appena descritto, e una volta creato il template temporaneo verificare se esso è presente nell’archivio per produrre un risultato. 

### Registrazione di un soggetto 

Detto anche *enrollment*. Si associa un insieme di caratteristiche all’identità di un soggetto, raccogliendo dei dati ed estraendo delle caratteristiche. Il modello estratto (template) è memorizzato in un database o su un supporto portatile (smart card). Questo processo può essere effettuato singolarmente o in blocco (batch Enrollment).

### Verifica e riconoscimento del soggetto

Non sempre una stessa biometrica può essere utilizzata sia verifica che per fare riconoscimento. Dipende dalle condizioni, una delle quali è proprio scegliere se svolgere Verifica o Riconoscimento. 
- Nel caso delle Verifica si parla di confronto Uno a Uno, dove un individuo fornisce la propria identità (mediante carta d’identità, codice utente ecc, in un qualsiasi modo, e il sistema una volta che è stata acquisita l’identità, effettua un match 1 a 1, acquisendo il template della persona in real time, confrontandolo con quello memorizzato, e confermando o negando l’identità dichiarata da un individuo. 
- Nella fase di riconoscimento dove si verifica un confronto Uno a Molti, ovvero quando l’utente non fornisce la propria identità (esempio telecamera al gate aereoportuale). In questo caso si acquisisce il dato biometrico e lo si confronta con quelli memorizzati in vari storage. Quindi si stabilisce l’identità di un soggetto a partire da un insieme di persone registrate.

In un sistema biometrico le fasi di Verifica o Identificazioni sono suddivisibili essenzialmente in quattro moduli:
- Il modulo di acquisizione della specifica biometria
- Il modulo di estrazione delle caratteristiche e creazione del template relativo alla biometria rilevata
- Il modulo di confronto
- Il modulo di decisione

### Formazione delle biometriche

Alcune biometriche risultano essere più discriminanti di altre. Durante la fase di angiogenesi, nel grembo materno impatta maggiormente sulla formazione di due delle biometriche, più discriminanti e stabili nel corso della vita di un utente, ovvero impronta digitale e iride. La fase di angiogenesi è il processo fenotipico di sviluppo di nuovi vasi sanguigni a partire da altri già esistenti. Alcune biometriche individuano tre possibili fattori di caratterizzazione: genotipici, fenotipici e comportamentale. Concentrandosi sui primi due si può evincere che le componenti genotipiche vengono trasmesse direttamente attraverso il genoma dei genitori. La componente randotipica non è condivisa con nessuno ed è strettamente legata all’utente. Quanto più è forte quest’ultima componente tanto più si riesce a differenziare una persona, anche rispetto ai parenti. 

## Proprietà delle caratteristiche biometriche
- **Universalità**: quando si sceglie una biometrica, ogni persona deve possedere tale biometria; 
- **Distintività**: due persone devono essere sufficientemente distinguibili in base a tale biometria; 
- **Stabilità**: la biometria deve rimanere invariante (rispetto ai termini di confronto) nel tempo; 
- **Misurabilità**: essa deve essere misurabile quantitativamente. 
- **Efficacia**: l’acquisizione, l’estrazione delle caratteristiche e il confronto delle entità non devono essere troppo costose in termini di tempo, memoria ed efficienza del sistema; 
- **Accettabilità**: la procedura di acquisizione deve essere tollerata da una vasta porzione della popolazione (utenti a cui viene sottoposta la biometrica); 
- **Eludibilità**: la probabilità che il sistema venga raggirato o indotto in errore deve essere minimizzata. 

Gli utenti sono di tipo *cooperativo* o *non cooperativo*. Inoltre, possono esserea *abituati* (autenticazione biometrica effettuata spesso) o *non abituati* (autenticazione biometrica effettuata raramente). Infine, possono essere *consapevoli* o meno. L'autenticazione in sé può essere *online* (l'utente è in attesa finché il sistema non risponde) oppure *offline* (l'utente viene acquisito dal sistema biometrico ma non attende una risposta immediata).

I dati biometrici a differenza delle tradizionali metodologie di autenticazione non possono essere persi, trasferiti ad altri o dimenticati. L’acquisizione (digitalizzazione dei dati) può determinare una variabilità delle biometrie: 
- **Intra-Classe**, cioè la variabilità delle biometrie per un individuo. (condizionate dal tempo) 
- **Inter-Classe**, cioè la similarità delle biometrie tra individui diversi. (sosia? gemelli?)

Entrambe le variabilità rappresentano elementi di disturbo per il riconoscimento dell’individuo attraverso tecniche biometriche.

### Misure delle prestazioni

Le prestazioni di un sistema biometrico possono essere misurate con diverse modalità, innanzitutto comprendendo il comportamento di tale sistema biometrico. Tendenzialmente ci possono essere quattro possibili casi: 
• L’identità corrisponde ed il soggetto è accettato. 
• L’identità corrisponde ma il soggetto è respinto (errore). 
• Un impostore è accettato (errore). 
• Un impostore è rifiutato. 

Non è possibile riconoscere un individuo senza ammettere una tolleranza d’errore. La soglia di tolleranza è cruciale e dipende fortemente dall’applicazione. Una soglia troppo bassa causa molti errori di Tipo I, rifiuto di soggetti registrati – FRR (False Recognition Rate). Una soglia troppo alta causa molti errori di Tipo II (accettazione di impostori) – FAR (False Acceptance Rate). FAR = FRR. La scelta più utilizzata è Equal Error Rate (EER). Quando si progetta un sistema biometrico, bisogna individuare la soglia ottimale (EER) che incrocia le due curve FRR e FAR. In questa logica si fa lavorare per un certo periodo il sistema biometrico facendo variare la soglia di tolleranza e gli errori mappando le due curve, ed infine si raggiunge all’intersezione delle due, che rappresenta un giusto compromesso.

# Principali biometriche

- **Impronta digitale**: Le caratteristiche globali non sono sufficienti per il riconoscimento, infatti tali caratteristiche vengono utilizzate solo per classificare (clustering) le impronte (divisione in classi). Gli archi sono più rari, mentre sono più frequenti i loop e le spirali. Queste caratteristiche, come in figura, sono macro-caratteristiche quindi possono essere condivise da più di una persona e come tali non consentono la discriminazione della persona stessa. Le caratteristiche locali dette minuzie (singolarità) si utilizzano solo per il riconoscimento all’interno della classe prodotta dalle caratteristiche globali. Queste caratteristiche sono invece estremamente singolari. È possibile trovare due persone con caratteristiche globali praticamente equivalenti ma con caratteristiche locali (minuzie) assolutamente diverse. 

- **Iride**: L’iride ha caratteristiche dal punto di vista fisico, molto simili a quelle delle impronte digitali, come delle minuzie con una distribuzione randomica sulla sua superfice. Essa è la zona colorata intorno alla pupilla e la struttura complessa ne costituisce la chiave di autenticazione. Non è passibile di cambiamenti nel corso del tempo. Non può essere modificata artificialmente. La probabilità di trovare sulla Terra due iridi uguali è praticamente nulla. Ogni iride umano ha infatti una struttura unica, al punto che persino l’iride destra e sinistra della stessa persona sono differenti. - L'iride può essere rivelato in questo modo: Un sensore, collocato a circa 40 centimetri di distanza dalla persona esaminata, inizia a fotografare i margini dell’occhio; quindi, attraverso un certo numero di scansioni successive, si individuano i contorni dell’iride come una corona circolare. • Poi si seleziona un quadratino alla volta di quest’area che rappresenta l’area da decodificare. II disegno di questa regione è convertito in un codice di 512 byte, il cosiddetto Iris Code che, confrontato con quelli archiviati nel database, identifica o meno la persona.

- **Retina**: La retina si trova nella parte interna dell’occhio, e la sua scansione avviene attraverso la mappatura dei capillari sul fondo oculare. È basato sull'acquisizione e la verifica della mappa vascolare della retina dell'occhio umano: ci sono circa 180 caratteristiche misurabili. La forma delle vene nella retina sono uniche per ogni individuo. È situata in una posizione più interna rispetto all’iride, per cui i metodi per la scansione sono più invasivi. Ci sono due metodi differenti di acquisizione della retina: • Metodo attivo: l’utente deve effettuare dei movimenti con la testa (20-40 cm) affinché il dispositivo di scansione possa individuare la posizione corretta; • Metodo passivo: l’utente resta fermo e una serie di dispositivi di scansione in cooperazione individuano la posizione corretta.

- **Geometria della mano**: Consiste nel riconoscimento delle persone mediante la verifica delle misure e della conformazione della mano e consente un discreto coefficiente di univocità. Le misure fisiche della mano sono catturate da un DISPOSITIVO CCD e la sagoma della mano viene memorizzata tridimensionalmente. La mano viene posta su un piano dove vi sono 5 pioli per posizionarla nel modo giusto. Due immagini acquisite: dall'alto e di lato.

- **Firma**: La firma è una biometrica prevalentemente comportamentale, rispetto alle precedenti che risultano essere fisiologiche. È una tecnica riconosciuta ai fini dell’autenticazione. Eccessiva variabilità intra-classe. Può essere dimenticata (a differenza di altre biometriche). Nella modalità di acquisizione offline contano solo le caratteristiche morfologiche (forma geometrica) che sono facili da duplicare. Nella modalità online (più difficile da realizzare mediante hardware speciale) si considerano altre caratteristiche (velocità, accelerazione, inclinazione delle penna…) più difficili da replicare

- **Riconoscimento vocale**: determinazione di un modello acustico dipendente dal linguaggio e dal soggetto. Il modello acustico riflette anatomia e comportamento. Richiede complesse elaborazioni del segnale acustico (analisi di spettro, periodicità, etc.…). Le caratteristiche della voce di un parlante sono dovute sia a differenze fisiologiche, sia al particolare stato d’animo in cui si trova. 

- **Orecchio**: L’acquisizione avviene attraverso una serie di caratteristiche uniche che caratterizzano la morfologia di ciascun orecchio. Essa non muta nel tempo.

- **Volto**: Il volto viene utilizzato sia per la verifica sia per il riconoscimento dell’identità. L'acqusizione del volto avviene tramite face detection (c'è un volto?), face segmentation (dov'è il volto nell'immagine ferma?) e face tracking (dov'è il volto in un video?).


# Sistemi multi-biometrici

L’idea di sistema multi-biometrico nasce dalla necessità di aumentare la sicurezza nel contesto di verifica e 
riconoscimento di una persona. La maggior parte dei sistemi presenti si basa su una singola biometria. Le modalità sono: sistemi multimodal, multibiometric o multiexpert. La combinazione delle diverse biometrie può essere eseguita in ciascuno dei quattro moduli di sistema:

- Biometric Fusion 
    - Before Matching
        - Sensor Level
        - Feature Level: le funzioni che sono state estratte con tecniche possibilmente diverse possono essere fuse per creare un nuovo vettore di caratteristiche per rappresentare l'individuo.
    - After Matching
        - Dynamic Selection
        - Classifier Fusion: i punteggi di diversi classificatori sono considerati funzioni e sono inclusi in un vettore di caratteristiche. Un classificatore binario viene addestrato per discriminare tra vettori di punteggiautentici e impostori (NN-Neural Networks, SVM - Support Vector Machine)
            - Transformation Level: i punteggi di diversi match vengono prima normalizzati (trasformati) in un dominio comune e poi combinati usando le regole di fusione.
            - Decision Level: ogni classificatore emette la propria decisione (accetta / rifiuta per verifica o per identificazione). La decisione finale viene presa combinando le singole decisioni secondo una regola di fusione. (combinazioni seriali di AND, OR...)
            - Score Level: diversi algoritmi di matching restituiscono un insieme di punteggi che sono fusi per generare un singolo punteggio finale.
                - Abstract
                - Rank
                - Measurement


## Scenari di fusione

La scelta del numero e del tipo di biometria da valutare dipende soprattutto dalla natura del sistema. Un sistema governativo ha esigenze di sicurezza e di autenticità dell’utente superiori rispetto ad un sistema commerciale; la scelta di una biometria più affidabile quale l’iride o l’impronta digitale è favorita. Un sistema embedded su telefonini o computer palmari privilegia l’uso di biometrie rilevabili con l’hardware in dotazione al dispositivo, quindi voce, volto o firma.

- Unica biometria e Multiplo sensore: sono combinate le informazioni dello stesso tratto biometrico acquisito però con due tipi di sensori diversi.
- Multipla biometria: sono combinate le caratteristiche di due biometrie diverse, un volto ed un’impronta.
- Unica biometria e Multipla unità: si combinano due elementi diversi appartenenti alla stessa classe biometrica (l’impronta di due dita diverse).
- Unica biometria e Multipla acquisizione: si combinano più sessioni di acquisizione dello stesso tratto biometrico (più impressioni della stessa impronta).

Un sistema multimodale può essere progettato secondo tre distinte architetture:
- In parallelo: le informazioni estratte dalle molteplici biometrie sono utilizzate simultaneamente per realizzare il riconoscimento. Le acquisizioni sono svolte contemporaneamente e le valutazioni delle singole biometrie sono realizzate indipendentemente e poi combinate mediante opportune tecniche difusione. Questa tecnica può essere utilizzata per entrambe le modalità di riconoscimento, verifica e identificazione. Offre vantaggi maggiori nella prima, in quanto garantisce un accertamento dell’individuo più forte basando la decisione su più parametri di valutazione.
- In serie: le valutazioni delle singole biometrie, generalmente due o tre al massimo, sono effettuate in cascata. Questa tecnica può essere utilizzata in entrambe le modalità di riconoscimento. Essa è più vantaggiosa nella modalità di identificazione, poiché può essere utilizzata come strumento di filtraggio dei possibili canditati ad ogni processo di confronto. Solitamente si utilizzano diversi tipi di biometrie, una prima di rapido confronto ma di limitata attendibilità per eseguire una prima selezione di una rosa di candidati, sui quali applicare, quindi, una seconda biometria più lenta ma più affidabile per la decisione finale.
- A livello gerarchico: si usano metodologie di classificazione individuali per le varie biometrie, quindi i risultati sono memorizzati in una struttura ad albero che facilita la decisione finale. Questa modalità è particolarmente utile nel caso di numerose biometrie da integrare.

## Politiche di fusione

Ritardare la fusione risulta sconveniente perché:
- Il modulo decisionale riceve solo una minima parte delle informazioni acquisite e conosce solo 
l’esito del confronto delle singole biometrie
- Comporta l’implementazione e quindi l’elaborazione di due sottosistemi ognuno dedicato alla 
specifica biometria.

Conviene fare uso di una strategia di fusione il prima possibile poiché si conserva una ricchezza di 
informazioni maggiore fornita dai dati acquisiti. Il template derivante dalla fusione può risultare di dimensioni considerevoli, diventando pesante da gestire dal sistema incidendo così sulle performance. Questa strategia non sempre è attuabile in quanto spesso si lavora con sistemi chiusi nei quali non sono note le relazioni tra i dati acquisiti e i template generati oppurepuò essere difficile fondere caratteristiche provenienti da biometrie diverse. La scelta più vantaggiosa resta una fusione al modulo di confronto.

## Strategia di fusione

Al livello decisionale è possibile combinare con una strategia AND/OR:
- Richiedere che siano superate tutte le prove biometriche (AND) oppure solo alcune (OR).
- Esempio (Volto-Impronta-Mano): Impronta AND (Volto OR Mano).

Al livello di confronto è possibile utilizzare una strategia di combinazione pesata:
- Si associa un peso a ciascuna biometria e quindi anche il risultato dei singoli confronti avranno un  peso diverso in fase decisionale.
- Altre strategie utilizzano funzioni di combinazione matematiche come la somma, il prodotto, la media, o il massimo o minimo dei risultati dei confronti, queste tecniche necessitano di un ulteriore processo di normalizzazione dei tali risultati.