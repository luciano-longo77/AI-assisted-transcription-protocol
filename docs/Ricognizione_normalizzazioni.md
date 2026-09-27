# Ricognizione delle normalizzazioni in edizioni critiche digitali open source

**Documento di supporto alla *Nota al testo* 1.0** · 2026-09-27

Scopo: verificare quali classi di normalizzazione la pratica corrente delle edizioni digitali
ad accesso aperto prevede, per misurare la copertura della *Nota al testo* di questo progetto e
individuarne le lacune. Non è una rassegna bibliografica: è un **controllo di completezza**.

---

## 0. Metodo e limiti dichiarati

La ricognizione è stata condotta dall'ambiente cloud di questo progetto, la cui rete in uscita è
filtrata da una policy di *egress*. Ne segue un limite che va dichiarato perché incide sul grado di
affidabilità di ogni riga che segue:

| fonte | come è stata letta | affidabilità |
|---|---|---|
| `luciano-longo77/castello-dell-anima-edizione` | **clone diretto del repository**, lettura integrale dei documenti di criteri | **piena, verificata** |
| `tei/A31_*.xml` di questo repository | lettura diretta e spoglio automatico | **piena, verificata** |
| Red CHARTA, MENOTA, DTABf, Vespasiano da Bisticci, ARTESIA, OVI/TLIO, Codice Pelavicino, Tanzlingher, EDV, CoDiSV, Gargnano | **ricerca web con restituzione sintetica**: le pagine dei criteri non sono raggiungibili da questo ambiente | **indiretta**: da riverificare sulle fonti primarie prima di citarle in pubblicazione |

Le righe marcate **indiretta** sono utilizzabili per orientare le scelte, **non** per essere citate come
testimonianze puntuali. La verifica diretta è un compito aperto (v. § 7).

---

## 1. Tre architetture, non tre livelli di severità

Il primo risultato della ricognizione non riguarda *quanto* si normalizza, ma **dove si mette la
normalizzazione**. Le edizioni censite si distribuiscono su tre architetture, e la scelta
dell'architettura precede e vincola la scelta dei criteri.

### A. Livelli paralleli dentro la stessa codifica

Un solo documento porta due o più livelli simultanei; nessun livello sostituisce l'altro.

- **MENOTA** (Medieval Nordic Text Archive) formalizza **tre livelli** con elementi propri,
  estensione di TEI: `<me:facs>` (lettera per lettera, con caratteristiche paleografiche e
  abbreviazioni conservate), `<me:dipl>` (abbreviazioni sciolte e identificate), `<me:norm>`
  (ortografia normalizzata). L'editore sceglie quanti livelli attivare: uno, due o tutti e tre.
- **TEI P5** offre il meccanismo generale: `<choice>` con le coppie `<orig>`/`<reg>`,
  `<abbr>`/`<expan>`, `<sic>`/`<corr>`.
- **Vespasiano da Bisticci Letters** (Bologna, /DH.arc) adotta la trascrizione diplomatica
  «con tutta l'informazione di normalizzazione risolta dentro la marcatura», per non alterare il testo.
- **`castello-dell-anima-edizione`**, il progetto gemello di questo, applica esattamente questa
  architettura: testo base diplomatico-conservativo, e ogni oscillazione resa con
  `<choice><orig>à</orig><reg>a</reg></choice>`, `<choice><orig>poiche</orig><reg>poiché</reg></choice>`,
  `<choice><orig>ed'unirsi</orig><reg>ed unirsi</reg></choice>`.

### B. Presentazioni multiple distinte

Lo stesso testo è pubblicato in più *presentazioni*, ciascuna con criteri propri dichiarati.

- **Red CHARTA** (corpus ispanico, secc. XII–XIX) prescrive una **tripla presentazione**
  obbligatoria: *facsímil*, *transcripción paleográfica*, *presentación crítica*. La motivazione
  dichiarata è che nessuna versione singola può dare tutta l'informazione che uno studioso richiede.
  La formula che regola la terza presentazione è la più vicina al § 2 della nostra Nota:
  **«normalización (no modernización) de los usos gráficos»** e adattamento della punteggiatura.
  La trascrizione paleografica, per contro, è quella che consente lo studio di «usi grafici, livello
  fonetico-fonologico, sistemi antichi di punteggiatura, uso di maiuscole e minuscole, divisione e
  unione delle parole».

### C. File separati per livello

Due file distinti, due regimi, nessun legame formale fra i due.

- **È l'architettura di questo progetto**: `tei/A31_diplomatica.xml` e `tei/A31_interpretativa.xml`.

### Conseguenza per il protocollo

L'architettura C è la sola che rende **misurabile** l'intervento del modello come evento discreto —
ed è per questo che il protocollo la adotta: la metrica `D = interventi ÷ (parole/1000)` ha bisogno di
un *prima* e di un *dopo* separati e confrontabili. Ma è anche la sola in cui il singolo intervento,
una volta prodotto il file B, **non è più recuperabile dal file**: sopravvive soltanto nel log.

Questo espone il progetto a un rischio preciso: **se il log si stacca dal testo, l'edizione
interpretativa diventa inverificabile**. Le architetture A e B non hanno questo problema perché la
normalizzazione resta nel documento. La raccomandazione del § 6.1 nasce da qui.

---

## 2. Tavola comparativa delle classi

Legenda: **N** normalizza · **C** conserva · **M** porta nella marcatura senza toccare il testo base ·
**—** non dichiarato / non verificato.

| classe | *Nota al testo* 1.0 (questo progetto) | Castello, ed. a stampa 2015 | Castello, ed. digitale MC-1 | CHARTA (pres. critica) | MENOTA `me:norm` | ARTESIA | OVI/TLIO |
|---|---|---|---|---|---|---|---|
| Abbreviazioni | **N** tacito | **N** tacito | **M** `abbr`/`expan` | N | N | N | N |
| u/v, i/j | **N** | N | **M** `orig`/`reg` | N | N | N | N (`j`→`i`) |
| h etimologica | **N** | — | **C** | N | N | — | C |
| Nessi `-tione` | **N** → `-zione` | N | **C** (dichiarato: «non si normalizza») | N | N | — | C |
| `et` | **N** → `e`/`ed` | — | C | N | N | — | C |
| Accenti e diacritici | **N** | N | **M** | N | N | N | **C** (non si aggiungono) |
| Maiuscole | **N** | N | C | N | N | **N** | N |
| Punteggiatura | **N** moderata | N | **C** (originale conservata) | **N** adattata | N | **N** dichiarata in nota | N |
| Unione/separazione | **N** | N | **C** («indizi di scrittura semicolta») | N | N | **N**, con attenzione alla **geminazione fonosintattica** | N |
| Scempie e geminate | **C** (salvo `-ttione`) | — | **C** («non si raddoppia d'ufficio») | C | — | — | C |
| Morfologia | **C** | C | **C** («la morfologia dialettale non è regolarizzata») | C | — | C | C |
| Paragrafatura | **—** | — | — | N | — | **N** dichiarata in nota | — |
| Numeri e cifre | **—** | N | — | — | — | — | — |
| Sillabazione a fine riga | **N** (ricomposizione) | N | M (`lb break="no"`) | N | N | — | — |
| Errori d'autore | **—** | — | **M** `sic`/`corr` con `@resp` | N | — | **N** marcato «A» | — |
| Congetture | **N** editore, `[ ]` | N | **M** `supplied` con `@resp @cert` | N | — | N | — |

Il dato più netto della tavola è che **nessuna delle edizioni censite normalizza meno di questa Nota
sul versante grafico, e nessuna normalizza la morfologia**. Il criterio-limite del § 2 della Nota
(«si normalizza la veste grafica, non morfologia, lessico, sintassi») coincide, nella sostanza e quasi
nella formula, con il principio CHARTA «normalización, no modernización». Su questo la Nota è allineata
alla pratica internazionale.

---

## 3. Classi che la *Nota al testo* 1.0 non prevede

Sono le lacune effettive emerse dal confronto. Ciascuna è una classe che altre edizioni dichiarano
e che il testimone A 31 presenta.

| proposta | classe | perché serve su A 31 | modello |
|---|---|---|---|
| **N10** | **Geminazione fonosintattica e segmentazione** | l'autografo è siciliano: `a llei`, `che ddisse`, `a ccasa` sono attesi, e la loro separazione è una decisione, non un fatto | ARTESIA interviene esplicitamente sulla segmentazione «specialmente per la geminazione fonosintattica», documentandola in nota |
| **N11** | **Paragrafatura e capoversi** | il testimone ha periodi lunghissimi e paragrafazione debole; introdurre capoversi è un intervento editoriale che la Nota 1.0 non nomina, benché il file TEI lo pratichi con `<p>` | ARTESIA e CHARTA la dichiarano |
| **N12** | **Errori d'autore e dittografie** | il progetto gemello ne ha trovate **al confine dei richiami di pagina** (`fw type="catch"`), fenomeno identico in A 31, che ha 72 `pb` | Castello MC-1: due dittografie espunte con `<corr resp="#editor"/>`; ARTESIA marca con «A» |
| **N13** | **Numeri, cifre, date** | ordinali abbreviati, numerali romani, date liturgiche | *Quaderni di Gargnano* (carteggi rinascimentali): cifre riprodotte come scritte, punto fra numero e lettera negli ordinali compositi, maiuscola per i numerali latini |
| **N14** | **Citazioni latine e cambio di lingua** | A 31 alterna italiano e latino (`etiam`, formule liturgiche): il latino **non** va sottoposto a N3 e N4, o si ottengono mostri | TEI `@xml:lang`; Castello MC-1 usa `@xml:lang` su `<expan>` |
| **N15** | **Discorso riportato** | il testimone riporta discorsi diretti senza segni; introdurre virgolette è interpretazione | CHARTA, DTABf |
| **N16** | **Caratteri speciali e segni paleografici** | segni tachigrafici, nota tironiana, titulus | MENOTA (MUFI); DTABf |

**N14 era la lacuna più grave, e in 1.0 è già colmata.** Le classi N3 (h etimologica) e N4 (nessi
latinizzanti) applicate a una citazione latina la distruggono: `honoratissimi` va emendato,
`Honoratissime Pater` no; `oratione` diventa *orazione*, `oratio` resta `oratio`. Un modello che
applichi le regole alla lettera normalizzerà anche il latino. L'eccezione è stata perciò inserita
**in testa a N3, con validità estesa a N4**, e non come classe autonoma in coda: è un limite di
applicabilità delle due classi, non una classe.

Le restanti proposte — **N10, N11, N12, N13, N15, N16** — sono lacune **aperte**: la Nota 1.0 non le
prevede. Nessuna è bloccante per la riscrittura del Prompt B, perché nessuna produce un errore
silenzioso: un fenomeno non previsto ricade nella clausola di chiusura (Nota, § 9.7) e si arresta come
caso non delegabile. Vanno però decise prima di dichiarare stabilizzato il livello B, perché una classe
non prevista non entra nel calcolo della densità e resta invisibile alla metrica.

---

## 4. Il caso `-tione`: una divergenza da ratificare

La ricognizione ha prodotto un riscontro che riguarda direttamente la coerenza fra i progetti di questo
curatore. L'edizione digitale del *Castello dell'anima* dichiara, fra i propri principi applicati:

> «`orig` = forma del manoscritto (dato documentario); `reg` = regolarizzazione **esclusivamente
> grafica**. La morfologia dialettale non è "regolarizzata": resta la forma d'autrice.
> Il nesso latineggiante **`-ti-` (‑*tione*) non si normalizza** in ‑*zione*.
> La **scempia** del testimone si conserva (non si raddoppia d'ufficio).»

La prima e la terza proposizione coincidono con la *Nota al testo* 1.0. **La seconda la contraddice.**
Nel registro delle decisioni, il caso è documentato: a III §36 la forma `interpellatione` è conservata
e il `<choice>` rimosso, «nesso ‑*ti*‑ non normalizzato».

La divergenza è reale e non si risolve dicendo che i testimoni sono diversi, perché sono omogenei: due
autografi siciliani monastici di fine Seicento, entrambi Palermo BCP. Si risolve — se si vuole
risolverla — osservando che i **prodotti** sono diversi:

- il *Castello* digitale è un'edizione **documentaria** a testo base conservativo: il suo `reg` è uno
  strato aggiunto, e l'onere della prova sta su chi normalizza, perciò il caso dubbio si conserva;
- la *Vita* livello B è un **testo di lettura**: l'onere sta su chi conserva, perché ogni forma
  conservata è un ostacolo per il lettore a cui il prodotto è destinato;
- l'edizione a stampa del *Castello* (Casapullo 2015), che è anch'essa un testo di lettura, adotta
  «criteri di trascrizione moderatamente regolarizzati» — ed è la Nota di quell'edizione la fonte dei
  nostri criteri.

Su questa lettura la divergenza è coerente: **lo stesso curatore normalizza `-tione` nei testi di
lettura e lo conserva nelle edizioni documentarie.** Ma è una posizione che va **scritta**, perché un
lettore che confronti i due repository vedrà due trattamenti opposti dello stesso fenomeno nello stesso
anno.

**Decisione del curatore (2026-09-27): `-tione` si normalizza.** La divergenza è quindi ratificata nella
lettura sopra esposta, ed è dichiarata nella Nota al § 10, decisione 11, con la regola generale che ne
deriva per entrambi i progetti: **`-tione` si normalizza nei testi di lettura e si conserva nelle
edizioni documentarie.** L'alternativa scartata era conservare il nesso anche nella *Vita*, riallineando
i due repository al prezzo di 80 occorrenze di minore leggibilità.

---

## 5. Allineamento alla tassonomia TEI

TEI P5 prevede per `<editorialDecl>` un insieme chiuso di figli: `<correction>`, `<normalization>`,
`<hyphenation>`, `<segmentation>`, `<quotation>`, `<interpretation>`, `<stdVals>`. Le classi della Nota
vi si mappano senza residui, e la mappatura è la forma in cui la Nota va riversata nell'header TEI:

| figlio di `editorialDecl` | classi della Nota |
|---|---|
| `<normalization>` | N2, N3, N4, N5, N6, N8 |
| `<correction>` | N12 (proposta) |
| `<hyphenation>` | ricomposizione della parola spezzata a fine carta (in N7) |
| `<segmentation>` | N7, N10, N11 (proposte) |
| `<quotation>` | N15 (proposta) |
| `<interpretation>` | N9, e le identificazioni onomastiche di N8 |
| `<stdVals>` | N13 (proposta) |

`<normalization>` accetta `@method` con i valori `silent` e `markup`: il nostro caso è `silent` per il
livello B e sarebbe `markup` se si adottasse la raccomandazione § 6.1. Lo scioglimento tacito delle
abbreviazioni (N1) si dichiara in `<normalization>` con `@method="silent"`.

---

## 6. Raccomandazioni

### 6.1 Rendere l'intervento recuperabile dal testo, non solo dal log

È la raccomandazione principale, e viene dall'architettura (§ 1). Tutte le edizioni censite in
famiglia A e B conservano nel documento la traccia di ogni normalizzazione. Il livello B di questo
progetto la perde.

Proposta minima, che non cambia l'architettura C e non tocca la metrica: nel file B, marcare con
`<choice><orig>…</orig><reg>…</reg></choice>` **le sole classi contestabili** — N7 (unione e
separazione), N8 limitatamente alle istituzioni e ai toponimi, N12 se adottata — lasciando tacite le
classi meccaniche (N2, N3, N4, N5, N6). Il costo è contenuto perché le classi contestabili sono poche
decine di luoghi; il guadagno è che le decisioni **interpretative** restano verificabili dentro
l'edizione, come nel gemello.

### 6.2 Eccezione per il latino — fatto

Inserita in testa a N3 della Nota 1.0, con validità estesa a N4 (§ 3, N14). Senza di essa il modello
avrebbe normalizzato anche le citazioni latine. Resta da marcare `xml:lang="la"` sui passi latini del
file TEI, che oggi non lo portano.

### 6.3 Divergenza `-tione` — fatto

Decisa in favore della normalizzazione e dichiarata nella Nota, § 10, decisione 11 (§ 4). Resta
opportuno riportare la stessa dichiarazione nel README del progetto gemello, perché la divergenza sia
visibile da entrambi i lati.

### 6.4 Trasferire la Nota nell'`editorialDecl` con la mappatura del § 5

Così la dichiarazione TEI e la Nota non possono divergere: la seconda è la fonte della prima. L'attuale
`editorialDecl` di `A31_interpretativa.xml` dichiara un regime opposto alla Nota su quattro punti
(Nota, § 11): è il caso da evitare, e nasce proprio dall'aver scritto la dichiarazione dopo il testo
invece che prima.

### 6.5 Portare le classi N nel log come vocabolario controllato

Il log ha già il campo della classe di intervento. Usare le sigle `N1`…`N16` come **vocabolario chiuso**
rende la densità `D` calcolabile per classe senza riconciliazioni manuali, e rende verificabile in CI
che nessun evento porti una classe non prevista dalla Nota — lo stesso ruolo che nel gemello svolgono le
guardie Schematron.

---

## 7. Verifiche aperte

Da fare quando la rete lo consenta, prima di citare queste fonti in pubblicazione:

1. leggere il PDF dei **criteri CHARTA** (`corpora.uah.es`) e la *Guía para editar textos CHARTA según
   el estándar TEI*, per confrontare classe per classe la *presentación crítica* con la Nota;
2. leggere il **MENOTA handbook cap. 4** (livelli di rappresentazione) nella versione 3.0;
3. leggere le **norme TLIO** (`normetlio.pdf`) per il trattamento di accenti e `j`, che risultano
   più conservativi dei nostri;
4. leggere i criteri di **Codice Pelavicino**, **Tanzlingher**, **EDV Sapienza**, **BibTom** — quattro
   edizioni italiane ad accesso aperto con criteri pubblicati, tutte non raggiungibili da questo
   ambiente;
5. leggere l'articolo dei ***Quaderni di Gargnano*** sui criteri per i carteggi rinascimentali
   (DOI 10.13130/quadernidigargnano-02-25) per N13;
6. verificare se l'**Archivio di scritture popolari siciliane** del CSFLS pubblica criteri propri: è
   il corpus tipologicamente più prossimo al nostro testimone e la sua assenza da questa tavola è la
   lacuna più sensibile.

---

## Fonti

Lette direttamente:

- [luciano-longo77/castello-dell-anima-edizione](https://github.com/luciano-longo77/castello-dell-anima-edizione) — `Micro-commits/MC-1/docs/Decisioni-editoriali.md`, `Introduzione-III,1-5.md`
- [luciano-longo77/bertolucci-scartafacci-TEI-edition](https://github.com/luciano-longo77/bertolucci-scartafacci-TEI-edition)

Lette tramite restituzione sintetica di ricerca (da riverificare, § 7):

- [Red CHARTA — Criterios de edición](https://www.redcharta.es/criterios-de-edicion/) · [Criterios CHARTA, PDF](https://corpora.uah.es/shared/resources/Criterios%20CHARTA%2011abr2013.pdf)
- [Menota handbook cap. 4 — Levels of text representation](https://www.menota.org/HB3_ch4.xml) · [Medieval Nordic Text Archive](https://www.menota.org/EN_forside.xhtml)
- [TEI P5 — 2 The TEI Header](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html) · [`editorialDecl`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/examples-editorialDecl.html) · [`normalization`](https://tei-c.org/release/doc/tei-p5-doc/en/html/examples-normalization.html)
- [Vespasiano da Bisticci Letters — Methodology](https://dharc-org.github.io/vespasiano-da-bisticci-letters-de/documentation/methodology.html) · [repository](https://github.com/dharc-org/vespasiano-da-bisticci-letters-de)
- [Deutsches Textarchiv — Introduction to the DTABf](https://www.deutschestextarchiv.de/doku/basisformat/introduction_en.html) · [repository](https://github.com/deutschestextarchiv/dtabf)
- [ARTESIA — Archivio Testuale del Siciliano Antico (CSFLS)](https://www.csfls.it/res/ricerche/artesia/) · [Corpus ARTESIA](https://www.cinum.unict.it/corpus-artesia)
- [Archivio di scritture popolari siciliane (CSFLS)](https://www.csfls.it/res/ricerche/scritture-semicolti/)
- [OVI — Opera del Vocabolario Italiano](http://www.ovi.cnr.it/) · [Norme per la redazione del TLIO, PDF](https://www.dilass.unich.it/sites/st06/files/normetlio.pdf)
- [Codice Pelavicino — Criteri di edizione](https://pelavicino.labcd.unipi.it/il-progetto/criteri-di-edizione/)
- [Tanzlingher — Criteri per l'edizione on line del testo](http://tanzlingher.disll.unipd.it/progetto/criteri-per-ledizione-on-line-del-testo/)
- [EDV Sapienza — Criteri di edizione](https://edv.seai.uniroma1.it/it/texts/criteria.html)
- [BibTom — Criteri di trascrizione](https://bibtom.disim.univaq.it/home/trascrizione/criteri)
- [CoDiSV — Corpus Digitale delle Scritture scolastiche d'ambito Valdostano](http://www.codisv.it/)
- [*Una proposta di criteri per l'edizione di carteggi rinascimentali italiani*, «Quaderni di Gargnano»](https://riviste.unimi.it/quadernidigargnano/article/view/10891)
- [*Il momento della trascrizione nel lavoro ecdotico*, «Quaderni di Gargnano»](https://riviste.unimi.it/index.php/quadernidigargnano/article/download/10866/pdf/33045)
- [Wikisource — Convenzioni di trascrizione](https://it.wikisource.org/wiki/Wikisource:Convenzioni_di_trascrizione)
