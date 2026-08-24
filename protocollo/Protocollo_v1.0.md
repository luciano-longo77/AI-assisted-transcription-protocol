# Dalla norma editoriale al workflow AI-assistito

**Un modello operativo e replicabile per scalare la trascrizione interpretativa di manoscritti omogenei**

*Protocollo di trascrizione automatizzata · versione consolidata, agosto 2026*

## Abstract

La trascrizione interpretativa dei manoscritti costituisce una delle fasi più onerose e meno formalizzate della pratica filologica, soprattutto quando applicata a corpora ampi, storicamente coerenti e testualmente complessi. Questo contributo propone un modello editoriale operativo AI-assistito concepito per rendere scalabile la trascrizione interpretativa di manoscritti omogenei per periodo e funzione, preservando al contempo il controllo umano sulle decisioni normative, la tracciabilità del processo e la validità filologica dei risultati.

L'obiettivo del lavoro non è dimostrare che l'intelligenza artificiale possa "aiutare" la trascrizione in senso generico, né produrre testi automaticamente normalizzati, ma formalizzare un workflow filologico controllato in cui uno o più Large Language Model operano come acceleratori e stabilizzatori delle decisioni editoriali ricorrenti, sotto supervisione umana esplicita. Il modello si fonda sulla distinzione tra trascrizione diplomatica e interpretativa, sull'esplicitazione preventiva del regime editoriale e su una procedura iterativa che consente di osservare quando e in che misura tali decisioni risultano delegabili.

Applicato in via sperimentale a campioni di manoscritti omogenei ma materialmente differenziati, e confrontando il comportamento di due modelli distinti, il workflow mostra come sia possibile ridurre la ridondanza decisionale e i costi cognitivi dell'editing, senza trasferire l'autorità editoriale alla macchina. Il risultato non è un testo finale né un gold standard, ma un protocollo replicabile, verificabile e trasferibile, pensato come fase preparatoria alla codifica TEI e come fondamento metodologico per progetti di ampia scala, come AURORA.

## 1. Introduzione. Trascrizione interpretativa: un problema pratico, metodologico e scalare

Nel lavoro filologico sui manoscritti, la trascrizione interpretativa rappresenta un momento cruciale e al tempo stesso fragile. A differenza della trascrizione diplomatica, che mira a riprodurre il dato grafico con il massimo grado di fedeltà possibile, la trascrizione interpretativa comporta una serie continua di decisioni normative: scioglimento delle abbreviazioni, gestione delle oscillazioni grafiche, normalizzazione selettiva, trattamento dell'ambiguità, equilibrio tra leggibilità e rispetto della testualità storica.

Queste decisioni sono spesso consolidate nella pratica individuale dell'editore, ma raramente vengono rese completamente esplicite, formalizzate o documentate in modo sistematico. Di conseguenza, la trascrizione interpretativa rimane una pratica ad alta intensità cognitiva, difficilmente trasferibile, poco replicabile e scarsamente compatibile con progetti di larga scala.

Negli ultimi anni, lo sviluppo delle tecnologie di Handwritten Text Recognition (HTR) ha permesso di automatizzare con successo il riconoscimento grafico del manoscritto, contribuendo in modo significativo alla trascrizione diplomatica su grandi volumi di dati. Tuttavia, queste tecnologie non affrontano il problema centrale della trascrizione interpretativa: non decidono come il testo debba essere scritto, ma soltanto come venga letto a livello grafico.

Il presente lavoro nasce da una constatazione pratica: in contesti in cui è necessario trascrivere centinaia di pagine manoscritte in forma interpretativa, il vero collo di bottiglia non è la lettura della grafia, ma la ripetizione non strutturata delle stesse decisioni editoriali. Questa esigenza pratica diventa qui il punto di partenza per una proposta metodologica: come rendere scalabile la trascrizione interpretativa senza rinunciare al controllo filologico.

## 2. Dall'editing assistito al modello editoriale operativo

Le pratiche di editing assistito attualmente diffuse nelle Digital Humanities — inclusi ambienti di trascrizione, strumenti HTR e supporti alla marcatura TEI — condividono un presupposto implicito: il regime editoriale è già noto, stabilizzato e condiviso. L'assistenza tecnologica interviene per accelerare l'esecuzione di tale regime, non per metterlo in discussione o verificarne la coerenza. In questo quadro la tecnologia riduce il tempo di digitazione, segnala incongruenze formali e applica normalizzazioni predefinite.

Ciò che rimane fuori campo è la norma editoriale stessa, che continua a operare come sapere tacito e personale. Il contributo di questo lavoro consiste nello spostare il focus: non l'AI che trascrive, ma il metodo editoriale che governa l'uso dell'AI. In questa prospettiva, il regime editoriale non è il punto di partenza non problematizzato, ma l'oggetto da formalizzare, trasferire e testare. L'intelligenza artificiale viene utilizzata non come soggetto decisionale, ma come strumento di stress test epistemico, capace di rendere visibili incoerenze, limiti e zone di stabilità del metodo umano.

## 3. Il protocollo

Protocollo **versione 1.0 — congelata** (agosto 2026). Riferimento normativo fisso: ogni applicazione dichiara questa versione. Le modifiche a principi, vocabolari, metrica o procedura incrementano la versione e sono tracciate in un changelog. Un'applicazione è conforme se e solo se rispetta i punti seguenti.

### Principi

- **P1 — Separazione dei livelli.** Diplomatica (A) e interpretativa (B) tenute distinte; ogni evento è attribuito a un livello.
- **P2 — Norma prima dell'automazione.** Il regime editoriale è esplicitato prima dell'AI e tradotto in prompt.
- **P3 — Autorità umana sulla norma.** Le decisioni del livello B restano all'editore; l'AI propone, l'editore dispone.
- **P4 — Ogni intervento è un dato.** Ogni scostamento tra output di un modello e forma accolta è registrato nel log, per ciascun modello, non assorbito.
- **P5 — AI come stress-test, non decisore.** I modelli servono a rendere visibili incoerenze, limiti e zone di stabilità del metodo umano.
- **P6 — Tracciabilità e reversibilità.** Ogni trasformazione è documentata e, ove possibile, reversibile (es. scioglimento diplomatico fra parentesi tonde).

### Modalità e procedura

- **Modalità generativa da zero.** Il protocollo si esegue come se non esistessero trascrizioni pregresse: i modelli producono la trascrizione. Una trascrizione preesistente può solo accelerare la validazione umana, senza sostituire o saltare alcuno step.
- **Disegno comparativo a due modelli.** Ogni unità è processata da due modelli distinti (Gemini e Claude), ai due livelli A e B, in modo da osservare e confrontare il comportamento di ciascuno.

Procedura, per ogni unità digitale:

1. Prompt A (skill) su Gemini → registrazione dell'evento nel log (MODELLO = Gemini, LIVELLO = A).
2. Prompt A (skill) su Claude → registrazione dell'evento (MODELLO = Claude, LIVELLO = A).
3. Validazione umana del livello A.
4. Prompt B (skill) su Gemini e su Claude → registrazione degli eventi (LIVELLO = B) per ciascun modello.
5. Validazione umana del livello B (autorità dell'editore).
6. Arresto e marcatura `non_delegabile` in presenza di ambiguità irriducibile o stratificazione genetica.

### Componenti

- **Prompt A e Prompt B come skill versionate.** I due prompt sono incapsulati come skill (istruzioni persistenti e versionate) in ciascun ambiente-modello (Gemini, Claude), identiche a ogni esecuzione: elimina la deriva del prompt come fonte di variabilità e rende l'ambiente riproducibile.
- **Prompt A (diplomatica).** Fedeltà grafica; abbreviazioni sciolte solo fra parentesi tonde; punteggiatura, maiuscole e unione/separazione originali; lacune con […]; segni materiali conservati.
- **Prompt B (interpretativa).** Scioglimento silenzioso; normalizzazione di grafia, diacritici, maiuscole e unione/separazione; punteggiatura minima; lingua e sintassi storiche conservate; fenomeni genetici riservati all'apparato.
- **Log a 12 campi.** ID_ERRORE, LIVELLO, TESTIMONE, SEGMENTO, TIPO_ERRORE, FORMA_AI, CORREZIONE_UMANA, AZIONE_UMANA, DECISIONE_EDITORIALE, ESITO, MODELLO (Gemini/Claude), NOTE. I campi a vocabolario chiuso sono vincolati da menu.
- **Foglio NORME_EMERGENTI.** AREA, NORMA (impersonale e generale), DERIVATA_DA_ERRORI (ID che devono esistere nel log), STATO.

### Controllo del non-determinismo (loop)

- **Esecuzione in loop.** Ogni unità è processata in loop (K ripetizioni per modello) tramite la skill. Se gli output coincidono, l'esecuzione è deterministica per quell'unità; se divergono, si registra la variabilità e si assume la forma di consenso come FORMA_AI.
- **Decodifica deterministica ove possibile.** Dove l'interfaccia o l'API lo consente, si adotta una decodifica a bassa/nulla temperatura. Il non-determinismo residuo è così misurato e documentato, non rimosso per assunzione.

### Metrica e criterio di stabilizzazione

- **M1 — Denominatore obbligatorio.** Foglio COPERTURA con testimone, riferimento, numero di parole/token e data per ogni unità.
- **M2 — Densità di intervento.** D = interventi ÷ (parole/1000), sul totale, per classe di TIPO_ERRORE e per modello, su finestre progressive.
- **M3 — Soglia dichiarata a priori.** La soglia θ (es. 5 interventi/1000 parole) è fissata prima della sperimentazione.
- **M4 — Criterio.** Una classe è stabilizzata quando D ≤ θ per N carte consecutive senza intervento sistematico; altrimenti è ricorrente.

### Garanzie di validità e affidabilità

- **V1 — Dichiarazione dell'ambiente.** Per ciascun modello: nome, versione, skill/prompt versionati e parametri di decodifica usati, con data.
- **V2 — Affidabilità inter-annotatore.** Un campione è codificato in cieco da un secondo occhio, con misura di accordo.
- **V3 — Controllo della vigilanza calante.** Un tratto dichiarato stabilizzato è ri-validato a freddo.
- **V4 — Baseline.** Un sotto-campione è trascritto in condizione di controllo (manuale, o HTR + manuale) per quantificare il guadagno.
- **V5 — Terminologia dell'evento.** A livello B si registra 'intervento' (scostamento dalla norma), non 'errore' oggettivo; a livello A l'errore paleografico resta oggettivo.
- **V6 — Non-delegabilità come esito valido.** I casi che eccedono la delega si marcano `non_delegabile`: risultati positivi che mappano il confine del metodo.
- **V7 — Controllo del non-determinismo del modello.** Il loop di ripetizioni e la forma di consenso quantificano la variabilità di ciascun modello, rendendola un dato dichiarato.

### Riproducibilità (FAIR)

Rilascio di skill (prompt incapsulati e versionati), schema del log, log popolato, norme, metrica e soglie; identificatori persistenti (DOI), licenze e metadati leggibili dalla macchina; immagini con segnature/rimandi se coperte da diritti; versionamento del protocollo con changelog.

## 4. Il perimetro sperimentale: campioni di due manoscritti

Il perimetro sperimentale di questo studio è volutamente ristretto. Il workflow è testato su campioni di due manoscritti dell'archivio BCP, scelti per rappresentare un gradiente di complessità controllato e per verificare la trasferibilità del regime editoriale da un testimone all'altro:

- **BCP, 2Qq A 31** – *Vita della ven. madre suor Benedetta Riggio*: testo regolare, caso di applicazione principale e sede della prima formalizzazione delle norme.
- **BCP, 3Qq B 49** – secondo testimone del medesimo corpus, materialmente e formalmente differenziato, impiegato come banco di trasferibilità delle norme emerse su A 31. *[Titolo breve e descrizione da inserire.]*

Su ciascun manoscritto la sperimentazione non procede in modo integrale, ma su un campione stratificato — un tratto iniziale di rodaggio, un tratto a regime e alcune carte-limite — sufficiente a osservare la curva di stabilizzazione e i suoi eventuali punti di arresto. L'estensione al resto del corpus omogeneo — tra cui *Il Castello dell'Anima* (2Qq E 29), gli *Effetti del divino amore* (2Qq F 25), il *Dialogo fra l'Anima e l'Angelo Custode* (3Qq B 151) e il quaderno a stratificazione genetica BCRS 3Qq D 69 — è demandata a una fase successiva.

## 5. Osservazioni dai campioni

L'analisi del log sui due campioni è disegnata per isolare tre risultati fondamentali, distinti per modello.

Primo, nei tratti più regolari — segnatamente in A 31 — ci si attende una riduzione rapida della ridondanza decisionale: abbreviazioni e oscillazioni già chiarite tendono a stabilizzarsi dopo poche iterazioni, riducendo l'intervento umano sistematico.

Secondo, dove il testo è strutturalmente più complesso, i modelli non "risolvono" l'ambiguità, ma la segnalano. Questo comportamento è coerente con l'obiettivo del modello: l'AI non sostituisce il giudizio filologico, ma ne evidenzia i punti critici.

Terzo, nelle carte a stratificazione genetica il workflow raggiunge un punto di arresto osservabile: la norma editoriale non è più trasferibile perché il testo richiede interpretazione genetica. Il confronto A 31 → B 49 misura, inoltre, quanto le norme formalizzate sul primo testimone riducano l'intervento sul secondo, e il confronto Gemini/Claude quanto il comportamento sia dipendente dal modello.

## 6. Il guadagno rispetto ai protocolli tradizionali

Il guadagno principale del modello non consiste nell'eliminare il lavoro umano, ma nel ridistribuirlo. L'editore non ripete più continuamente le stesse decisioni, ma governa il sistema che le applica. Ciò comporta una riduzione del tempo di lavoro sulle decisioni ricorrenti, un aumento della tracciabilità del processo editoriale e la possibilità di trasferire il metodo a collaboratori o a nuovi corpora omogenei. Questo rende la trascrizione interpretativa scalabile senza impoverimento.

## 7. LLM e HTR: due livelli diversi del processo editoriale

Il workflow qui proposto non sostituisce i sistemi HTR, ma si colloca a un livello differente. Se l'HTR risponde alla domanda *che cosa è scritto*, il modello editoriale AI-assistito risponde alla domanda *come deve essere scritto*. I due approcci sono complementari e integrabili.

## 8. Integrazione con AURORA

Questo lavoro costituisce una fase preliminare abilitante per il progetto AURORA, poiché stabilizza il passaggio critico dalla trascrizione diplomatica a quella interpretativa, rendendo possibile la codifica TEI multilivello e le analisi comparabili su larga scala.

## Conclusioni

Il lavoro mostra che la trascrizione interpretativa può essere trasformata da pratica tacita a processo controllato e scalabile, senza rinunciare alla responsabilità filologica. L'intelligenza artificiale, utilizzata come acceleratore sotto controllo umano, consente di affrontare la scala come problema scientifico e operativo, non come compromesso metodologico. Il contributo principale non è tecnologico, ma filologico: aver mostrato che la norma editoriale può essere resa operativa, verificabile e trasferibile, aprendo la strada a progetti di ampia dimensione senza perdita di rigore.
