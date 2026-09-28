# Da dove vengono questi criteri

**Il fondamento delle scelte editoriali di A 31 nella pratica delle edizioni digitali**

2026-09-28 · documento di accompagnamento alla [*Nota al testo*](Nota_al_testo.md) 1.0

---

La [*Nota al testo*](Nota_al_testo.md) dice che cosa è stato fatto al testo. Questa pagina dice **su che cosa poggia**: quali principi l'edizione condivide con la pratica corrente, quali scelte sono sue e su quale argomento si reggono. Serve a chi debba valutare l'edizione, citarla, o riusarne i criteri per un testimone analogo.

## 1. Normalizzare non è modernizzare

Il criterio-limite della Nota — *si normalizza la veste grafica, non si toccano morfologia, lessico, sintassi* — non è una formula d'occasione: è il principio su cui le edizioni documentarie ad accesso aperto convergono, in lingue e tradizioni diverse.

La **Red CHARTA**, che governa il corpus ispanico dei secc. XII–XIX, lo formula per la propria *presentación crítica* come **«normalización (no modernización) de los usos gráficos»**. L'edizione digitale del ***Castello dell'anima*** lo enuncia come statuto del proprio `<reg>`: «regolarizzazione **esclusivamente grafica**; la morfologia dialettale non è regolarizzata, resta la forma d'autrice». Le norme del **TLIO** per l'italiano antico e i livelli di **MENOTA** per il nordico medievale si fermano allo stesso confine.

Quel confine — **la morfologia non si tocca** — non è attraversato da nessuna delle tradizioni esaminate, e non è attraversato da questa edizione. È la ragione per cui `havea` diventa *avea* e non *aveva*, `offitio` diventa *offizio* e non *ufficio*, `dui` e `delli` restano.

La prova di controllo che la Nota aggiunge al principio — *se l'emendamento cambia il numero di sillabe o la qualità di una vocale, non è una normalizzazione grafica* — è un modo di rendere il confine verificabile caso per caso invece di affidarlo al giudizio. Non l'ho trovata formulata altrove in questi termini.

## 2. Perché l'edizione pubblica anche la diplomatica

Le edizioni che normalizzano senza rendere conto della forma originale sono le meno difendibili, e la pratica corrente lo ha risolto in tre modi.

**Livelli paralleli nella stessa codifica.** **MENOTA** formalizza tre livelli con elementi propri: `<me:facs>` lettera per lettera con le abbreviazioni non sciolte, `<me:dipl>` con le abbreviazioni sciolte, `<me:norm>` in ortografia normalizzata. TEI P5 offre il meccanismo generale con `<choice>` e le coppie `<orig>`/`<reg>`, `<abbr>`/`<expan>`, `<sic>`/`<corr>`. Le **Lettere di Vespasiano da Bisticci** trascrivono in diplomatico «con tutta l'informazione di normalizzazione risolta dentro la marcatura». Così l'edizione digitale del *Castello dell'anima*: `<choice><orig>poiche</orig><reg>poiché</reg></choice>`.

**Presentazioni multiple distinte.** **CHARTA** le rende obbligatorie: *facsímil*, *transcripción paleográfica*, *presentación crítica*, perché nessuna versione singola dà tutta l'informazione che uno studioso richiede.

**Due file, due livelli.** È la soluzione di questa edizione: `tei/A31_diplomatica.xml` e `tei/A31_interpretativa.xml`, entrambi pubblicati e citabili.

Le tre soluzioni condividono il principio — **il livello conservativo non si sopprime** — e si distinguono per dove lo collocano. La scelta dei due file separati risponde a un requisito che le altre non hanno: questa edizione nasce dentro un esperimento sull'uso di modelli linguistici come acceleratori sorvegliati, e separare fisicamente i due livelli è ciò che rende ogni intervento del modello un **evento discreto e contabile**, quindi misurabile. Le architetture a livelli paralleli, che tengono la normalizzazione dentro la marcatura, non permetterebbero quel conteggio.

Ne segue un'indicazione pratica per chi legge: **il livello A non è materiale di servizio, è parte dell'edizione.** Il testo interpretativo dà il senso; la forma sta nella diplomatica, e va consultata ogni volta che interessi la lingua e non il contenuto. I luoghi in cui la normalizzazione comporta un'interpretazione e non una regola — le separazioni di parola, le maiuscole istituzionali — sono in apparato, non lasciati al raffronto.

## 3. Le scelte di questa edizione nel quadro delle altre

**N** normalizza · **C** conserva · **M** porta nella marcatura senza toccare il testo base · **—** non dichiarato

| | **A 31** | *Castello*, stampa 2015 | *Castello*, ed. digitale | CHARTA, pres. critica | MENOTA `me:norm` | ARTESIA | OVI/TLIO |
|---|---|---|---|---|---|---|---|
| Abbreviazioni | **N** tacite | N tacite | **M** `abbr`/`expan` | N | N | N | N |
| u/v, i/j | **N** | N | **M** `orig`/`reg` | N | N | N | N (`j`>`i`) |
| h etimologica | **N** | — | C | N | N | — | C |
| Nessi `-tione` | **N** | N | C | N | N | — | C |
| `et` | **N** | — | C | N | N | — | C |
| Accenti, diacritici | **N** | N | **M** | N | N | — | C |
| Maiuscole | **N** | N | C | N | N | N | N |
| Punteggiatura | **N** moderata | N | C | N adattata | N | N | N |
| Unione, separazione | **N** | N | C | N | N | N | N |
| Geminate e scempie | **C** salvo `-ttione` | — | C | C | — | — | C |
| **Morfologia** | **C** | **C** | **C** | **C** | — | **C** | **C** |
| Congetture | **N** editore, fra quadre | N | **M** `supplied` con `@resp @cert` | N | — | N | — |

Sulla riga che conta — la morfologia — la colonna è uniforme. Sulle altre, questa edizione sta con le edizioni **di lettura** (la stampa del *Castello*, la presentazione critica di CHARTA, il livello normalizzato di MENOTA) e non con quelle **documentarie**, che conservano o rinviano alla marcatura. È la posizione coerente con il suo scopo: il livello B è un testo da leggere, e il livello A è lì per tutto il resto.

## 4. Le scelte particolari, e l'argomento su cui si reggono

Cinque punti in cui l'edizione decide in modo non ovvio. La Nota li dichiara al § 8; qui si dice contro che cosa sono state prese.

**Il nesso `-tione` si normalizza.** L'edizione digitale del *Castello dell'anima* — stesso curatore, autografo monastico siciliano coevo, stessa biblioteca — dichiara che il nesso **non** si normalizza, e conserva `interpellatione`. Qui si normalizza, per 80 occorrenze. La divergenza è voluta e riposa sulla differenza fra i prodotti: quella è un'edizione documentaria a testo base conservativo, dove l'onere della prova sta su chi normalizza; questa è un testo di lettura, dove sta su chi conserva. L'edizione a stampa del *Castello* (Casapullo 2015), anch'essa di lettura, normalizza. La regola generale che ne risulta, valida per entrambi i progetti: **`-tione` si normalizza nei testi di lettura, si conserva nelle edizioni documentarie.**

**La *h* etimologica e `et` si normalizzano.** La *Nota al testo* del *Castello* a stampa, da cui questi criteri derivano, non le nomina; le norme TLIO, per l'italiano antico, conservano. Qui si normalizzano — 98 e 74 occorrenze — perché il criterio del § 1 le classifica come veste grafica senza riscontro fonologico, e perché il prodotto è di lettura. È l'estensione più consistente rispetto al modello di riferimento, ed è dichiarata come tale.

**La maiuscola reverenziale si abolisce.** `La`, `Le`, `Lei` riferiti alla Madre vanno alla minuscola, e con essi la maiuscola di rispetto sui nomi comuni: `Monasterio`, `Madre`, `Padre`, `Città`, `Religione`. Sono 667 maiuscole interne al periodo su 152 tipi: il fenomeno quantitativamente più massiccio della normalizzazione. Poche edizioni lo nominano esplicitamente e il *Castello* digitale lo conserva; qui si interviene perché nell'uso del testimone la maiuscola è segno di rispetto e di enfasi, non segno grammaticale, e conservarla in un testo di lettura trasmette al lettore moderno un'informazione diversa da quella che portava.

**`ed` davanti a vocale, non `e`.** Contro l'uso italiano corrente, e secondo la prescrizione del modello di riferimento, per continuità fonica del periodo.

**Le oscillazioni non si uniformano.** `Immaculata` accanto a `Immacolata`, `difficultà` accanto a `difficoltà`, `havea` accanto ad `haveva`. È la scelta del *Castello* digitale, che le considera «parte costitutiva dell'italiano regionale dell'autografo», e vale anche per un testo di lettura: uniformare è un intervento sulla lingua, non sulla grafia, e cadrebbe fuori dal criterio del § 1.

## 5. L'ambito dei criteri

Le nove classi della Nota governano la veste grafica. Restano fuori, e sono decisi caso per caso dall'editore con dichiarazione in apparato, i fenomeni in cui la forma del testo dipende da un'interpretazione e non da una regola:

- la **segmentazione** dove la geminazione fonosintattica di un testimone siciliano rende ambigua la divisione delle parole;
- la **paragrafatura**, dove il testimone ha periodi lunghi e paragrafazione debole;
- i **doppioni al confine di carta**, fra i 72 cambi di carta del segmento edito;
- l'**estensione dei passi latini**, che le classi N3 e N4 non toccano;
- i **confini del discorso riportato**, che il testimone non segna;
- **numeri, cifre e date** nelle forme abbreviate.

Su questi punti l'edizione non ha una regola perché una regola darebbe risultati falsi: il criterio è che il luogo sia deciso e dichiarato, non normalizzato in silenzio. È lo stesso principio per cui ARTESIA documenta in nota ogni intervento sulla segmentazione e sulla paragrafatura, e per cui CHARTA li assegna alla presentazione critica e non alla paleografica.

## Appendice · Come dichiarare questi criteri in TEI

Per chi voglia riusarli in una codifica propria. TEI P5 prevede per `<editorialDecl>` un insieme chiuso di figli, ai quali le classi della Nota si mappano senza residui:

| figlio di `editorialDecl` | classi |
|---|---|
| `<normalization>` | N2, N3, N4, N5, N6, N8 |
| `<segmentation>` | N7 |
| `<hyphenation>` | ricomposizione della parola spezzata a fine carta (in N7) |
| `<quotation>` | discorso riportato (in N9) |
| `<interpretation>` | N9, e le identificazioni onomastiche di N8 |

`<normalization>` accetta `@method` con i valori `silent` e `markup`: il caso di questa edizione è `silent`, e sarebbe `markup` in un'architettura a livelli paralleli (§ 2). Lo scioglimento tacito delle abbreviazioni (N1) si dichiara in `<normalization>` con `@method="silent"`.

## Fonti

**Lette direttamente:** [luciano-longo77/castello-dell-anima-edizione](https://github.com/luciano-longo77/castello-dell-anima-edizione), registro delle decisioni editoriali e criteri ecdotici; i file TEI di questa edizione, per i conteggi.

**Consultate attraverso restituzioni sintetiche di ricerca.** Le righe della tavola che le riguardano orientano il confronto ma non sono citabili come testimonianze puntuali: le pagine dei criteri sono pubbliche e vanno consultate direttamente prima di fondarvi un'argomentazione. Il confronto resta più debole proprio con le tradizioni tipologicamente più vicine a questo testimone — ARTESIA, l'Archivio di scritture popolari siciliane, le norme TLIO.

- [Red CHARTA — Criterios de edición](https://www.redcharta.es/criterios-de-edicion/) · [Criterios CHARTA (PDF)](https://corpora.uah.es/shared/resources/Criterios%20CHARTA%2011abr2013.pdf)
- [Menota handbook, cap. 4 — Levels of text representation](https://www.menota.org/HB3_ch4.xml) · [Medieval Nordic Text Archive](https://www.menota.org/EN_forside.xhtml)
- [TEI P5 — The TEI Header](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/HD.html) · [`editorialDecl`](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/examples-editorialDecl.html) · [`normalization`](https://tei-c.org/release/doc/tei-p5-doc/en/html/examples-normalization.html)
- [Vespasiano da Bisticci Letters — Methodology](https://dharc-org.github.io/vespasiano-da-bisticci-letters-de/documentation/methodology.html)
- [ARTESIA — Archivio Testuale del Siciliano Antico](https://www.csfls.it/res/ricerche/artesia/) · [Archivio di scritture popolari siciliane](https://www.csfls.it/res/ricerche/scritture-semicolti/)
- [OVI — Opera del Vocabolario Italiano](http://www.ovi.cnr.it/) · [Norme per la redazione del TLIO (PDF)](https://www.dilass.unich.it/sites/st06/files/normetlio.pdf)
- [Deutsches Textarchiv — DTABf](https://www.deutschestextarchiv.de/doku/basisformat/introduction_en.html)
- [Codice Pelavicino](https://pelavicino.labcd.unipi.it/il-progetto/criteri-di-edizione/) · [Tanzlingher](http://tanzlingher.disll.unipd.it/progetto/criteri-per-ledizione-on-line-del-testo/) · [EDV Sapienza](https://edv.seai.uniroma1.it/it/texts/criteria.html) · [BibTom](https://bibtom.disim.univaq.it/home/trascrizione/criteri)
- [*Una proposta di criteri per l'edizione di carteggi rinascimentali italiani*, «Quaderni di Gargnano»](https://riviste.unimi.it/quadernidigargnano/article/view/10891)
