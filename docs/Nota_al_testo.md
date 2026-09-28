# Nota al testo

**Criteri di trascrizione dell'edizione interpretativa**

| | |
|---|---|
| Testimone | Palermo, Biblioteca Comunale, ms. **2 Qq A 31** |
| Opera | Suor Francesca Benedetta Corvino, *Vita della venerabil madre suor Benedetta Riggio* |
| Porzione edita | frontespizio – c. 36r (capp. I–IV e inizio cap. V) |
| Livello | **B — trascrizione interpretativa**, dal livello A (diplomatica validata) |
| Versione | **1.0** · redazione 2026-09-27, revisione redazionale 2026-09-28 |
| Licenza | CC BY 4.0 |

---

## 1. Che cosa stai leggendo

L'edizione pubblica **due testi dello stesso manoscritto**, entrambi citabili, che non sono due stesure ma due prodotti distinti:

- **Livello A, trascrizione diplomatica** (`tei/A31_diplomatica.xml`). Registra il testimone: grafia, abbreviazioni non sciolte, divisione di riga e di carta, segni materiali, punti dubbi. Non normalizza nulla. È la base di collazione e il luogo dove sopravvive ogni dato linguistico.
- **Livello B, trascrizione interpretativa** (`tei/A31_interpretativa.xml`). Restituisce un testo leggibile. **Questa Nota descrive soltanto il livello B.**

Chi voglia studiare la lingua della scrivente deve usare il livello A. Il livello B è il testo per la lettura, e ogni sua forma è il risultato delle regole dichiarate qui sotto: sono scritte in modo che il lettore possa, in qualunque punto, ricostruire mentalmente che cosa stava sulla carta.

> **Stato del testo.** Il file `tei/A31_interpretativa.xml` attualmente in repository è stato prodotto sotto un regime editoriale **precedente** a questa Nota, che conservava la *h* etimologica, i nessi in *-tione*, la congiunzione *et* e la maiuscola reverenziale. Va rifatto, e fino a quel momento il testo interpretativo pubblicato **non** corrisponde ai criteri descritti in questa Nota. La sua `editorialDecl` dichiara il regime sotto cui è stato prodotto.

## 2. Il criterio, e il suo costo

Per una scrivente di area semicolta il criterio più difendibile sarebbe quello conservativo: gli scarti dalla norma sono spie per valutare le competenze linguistiche di chi scrive, e normalizzare le cancella. Questa edizione sceglie invece di **intervenire moderatamente**, ammodernando e regolarizzando grafia e interpunzione per migliorare la leggibilità, e accetta il costo dichiarandolo: il conflitto non è risolto, è **spostato**. Le spie restano integralmente leggibili nel livello A, che resta pubblicato accanto a questo.

Il limite dell'intervento è fissato da un criterio unico, contro cui si misura ogni caso:

> **Si normalizza la *veste grafica*. Non si toccano morfologia, lessico, sintassi.**

È emendabile ciò che, nel sistema della scrivente, **non corrisponde ad alcun suono** — la *h* di `havea`, la *u* di `haurebbe`, la seconda *t* di `perfettione`, la *i* di `rimedij` — oppure ciò che **rende con altra veste un suono che l'italiano scrive diversamente**: `-tione` per *-zione*, `x` per *s*, `ch` per *c*.

Non è emendabile ciò che implica una forma diversa. La prova di controllo è secca:

> **Se l'emendamento cambia il numero di sillabe o la qualità di una vocale, non è una normalizzazione grafica e non si fa.**

Così `havea` diventa *avea* e non *aveva*; `offitio` diventa *offizio* e non *ufficio*; `Monasterio` perde la maiuscola ma non diventa *monastero*; `dui`, `delli`, `difficultà`, `instituto` restano come sono.

## 3. Che cosa si normalizza

Nove classi, siglate `N1`–`N9`. I conteggi si riferiscono al segmento edito, circa 6.500 parole.

> **Il latino non si normalizza.** Le classi N3 e N4 valgono per il solo testo italiano. `honoratissimi` diventa *onoratissimi*, ma `Honoratissime Pater` resta com'è; `oratione` diventa *orazione*, ma `oratio` resta `oratio`. Restano intatti anche i latinismi lessicali dell'italiano della scrivente: `etiam`, `instituto`, `infancia`, `concurso`.

### N1 · Abbreviazioni

Sciolte **tutte** e **tacitamente**, senza parentesi né corsivo: `d.a` > *detta*, `total.te` > *totalmente*, `final.te` > *finalmente*, `dunq.` > *dunque*, `V.R.` > *Vostra Reverenza*, `S.` + nome di santo > *san*/*santa*, ordinali per esteso. La forma sciolta è poi trattata come ogni altra parola. La stessa abbreviazione riceve sempre la stessa soluzione.

### N2 · u/v, i/j

`u` con valore consonantico > `v` (`haurebbe` > *avrebbe*, `seruitio` > *servizio*); `v` vocalico > `u`; `j` > `i` anche in posizione finale (`rimedij` > *rimedi*, `Monasterij` > *monasteri*, `Novitij` > *novizi*, `negotij` > *negozi*). Sette occorrenze di `-ij` finale, convenzione grafica senza riscontro fonologico.

### N3 · h etimologica

Eliminata dove non è etimologicamente italiana; conservata o introdotta dove l'uso moderno la richiede. **98 occorrenze.**

`havea` > *avea* · `haveano` > *aveano* · `havendo` > *avendo* · `havesse` > *avesse* · `havuto` > *avuto* · `haver` > *aver* · `hebbe` > *ebbe* · `huomo` > *uomo* · `honore` > *onore* · `hora` > *ora* · `humiltà` > *umiltà* · `Christiana` > *cristiana*

Cade la sola *h*, non la forma: il testimone alterna `havea` (18) e `haveva` (6), e l'alternanza **si conserva**, depurata della *h*. Restano intatte `ho`, `hai`, `ha`, `hanno`.

### N4 · Nessi e grafie latinizzanti

| nel testimone | nel testo | occ. |
|---|---|---|
| `-tione`, `-tioni` > `-zione`, `-zioni` | `oratione` > orazione, `devotione` > devozione, `fondatione` > fondazione | 80 (famiglia) |
| `-ttione` > `-zione` | `Concettione` > Concezione, `perfettione` > perfezione, `mortificattione` > mortificazione | 42 |
| `-tio` > `-zio` | `offitio` > offizio, `negotio` > negozio | 4 |
| `ci` per `zi` | `perficione` > perfezione | 2 |
| `x` per `s` | `exortationi` > esortazioni, `exemplare` > esemplare | 5 |
| `ch` per `c` | `Christiana` > cristiana, `charità` > carità | — |

Si normalizza il **nesso**, non la parola. La *tt* di `-ttione` non è una geminata della scrivente: è parte della resa grafica dell'affricata e cade con il nesso. **Fuori da questo contesto le geminate del testimone si conservano**: `Doppo` resta *doppo*.

### N5 · Congiunzione `et`

Davanti a consonante > **e**; davanti a vocale > **ed**: `et parve` > *e parve*, `et emendata` > *ed emendata*. **74 occorrenze.**

### N6 · Accenti, diacritici, apostrofo

Si toglie l'accento superfluo (`quì` > *qui*), si introduce quello mancante (`poiche`, `poi che` > *poiché*; `perche` > *perché*), si scioglie l'apostrofo abusivo (`buon'animo` > *buon animo*; `ed'` + vocale > *ed* + vocale).

Le otto alternanze del testimone hanno soluzione fissa:

| nel testimone | valore | nel testo |
|---|---|---|
| `à` / `hà` / `a` | preposizione | **a** |
| `ò` / `hò` / `o` | congiunzione | **o** |
| `hò` / `ho` / `ò` | verbo | **ho** |
| `quì` | avverbio | **qui** |
| `ne` | congiunzione negativa | **né** |
| `se` / `sè` | pronome tonico | **sé** |
| `si` | avverbio affermativo | **sì** |
| `perche` | congiunzione | **perché** |

La forma `[h]o` compare solo dove la lezione è materialmente incerta fra *ho* e *o*.

### N7 · Unione e separazione delle parole

`inalto` > *in alto* · `nonsapeva` > *non sapeva* · `inquestitempi` > *in questi tempi* · `nelei` > *né lei* · `per che` > *perché* · `egli` (= *e gli*) > *e gli*

L'ordine delle parole non si altera mai. A fine carta la parola spezzata è restituita per intero nella carta in cui comincia, e il richiamo cade.

Alcuni di questi interventi **non sono di grafia ma di lettura**: separare `egli` in *e gli* è un'interpretazione, che il lettore può contestare. Questi luoghi sono segnalati in apparato.

### N8 · Maiuscole e minuscole

Il testimone usa la maiuscola come segno di rispetto e di enfasi, non come segno grammaticale: **667 maiuscole interne al periodo su 152 tipi diversi**. Si riconducono all'uso moderno.

**Alla minuscola:**

| | esempi | occ. |
|---|---|---|
| maiuscola reverenziale | `La`, `Le`, `Lei` riferiti alla Madre | 16 |
| pronome di prima persona | `Io` > io | — |
| nomi comuni di persona religiosa | `Madre` 36, `Padre` 31, `Suoro` 18, `Monache` 14, `Reverenda` 13, `Abbadessa` 10, `Superiora` 4 | 126 |
| nomi comuni di luogo o istituzione non individuata | `Monasterio` 63, `Città` 10, `Regola` 5, `Casa` 4 | 82 |
| nomi astratti e aggettivi | `Religione` 3, `Divina`, `Statua` | — |
| appellativo di santità davanti a nome proprio | `San Giovanni` > *san Giovanni* | — |

**Alla maiuscola, conservata o introdotta:** nomi propri di persona e di luogo (Benedetta Riggio, Palermo, Roma); nomi di Dio e appellativi divini (Dio, Signore, Gesù, Spirito Santo); **denominazioni istituzionali individuate** (Casa Professa, Compagnia di Gesù, San Giovanni dell'Origlione, Santa Croce); titoli di opere.

Il criterio che separa le due liste è **l'individuazione, non la dignità del referente**. *Casa Professa* porta la maiuscola perché è il nome proprio dell'istituzione gesuitica palermitana: renderlo «la casa» falsifica il referente. *Monasterio della Concezione* ha il nome comune minuscolo e la specificazione maiuscola, perché è la specificazione a individuare. `Città` da sola è nome comune e va minuscolo anche dove il contesto renda ovvio che si tratta di Palermo.

Le identificazioni onomastiche e toponimiche sono dichiarate in apparato, non introdotte nel testo.

### N9 · Punteggiatura

Ritoccata **soltanto** dove il segno è obsoleto o dove conservarlo comprometterebbe l'intelligibilità.

I **due punti** del testimone sono segno di pausa media, non di annuncio: resi con virgola, punto e virgola o punto fermo secondo il contesto. Si introducono le virgole indispensabili a incidentali e nessi sintattici, e le maiuscole di inizio periodo che ne conseguono. Il discorso riportato riceve le virgolette basse.

**Il periodo non si semplifica.** Paratassi, anacoluti e concordanze a senso sono fatti stilistici, non errori di punteggiatura: il periodo lungo resta lungo.

## 4. Che cosa si conserva

Questa sezione ha la stessa forza della precedente. La deriva più probabile di un testo interpretativo è la modernizzazione silenziosa oltre il perimetro grafico.

| | esempi nel testimone |
|---|---|
| morfologia verbale | `avea` accanto ad `aveva`, `aveano` |
| morfologia nominale e pronominale | `dui`, `delli`, `dello` |
| lessico e latinismi lessicali | `etiam`, `instituto`, `infancia`, `concurso`, `monasterio`, `offizio` |
| apocopi | `venerabil`, `gentil`, `esser`, `saper` |
| oscillazioni vocaliche | `Immaculata` / `Immacolata`, `difficultà` / `difficoltà`, `Giesù` / `Gesù` |
| geminate e scempie fuori da N4 | `doppo` |
| sintassi | paratassi, anacoluti, concordanze a senso, ripetizioni |
| formule e titolature | *Vostra Reverenza*, *la venerabil madre* |

Nessuna di queste forme è stata corretta, uniformata o resa coerente. **L'oscillazione interna al testimone è un dato del testimone e sopravvive nel testo interpretativo:** dove il testo alterna, alterna il manoscritto.

## 5. I segni dell'edizione

| segno | significato |
|---|---|
| `/` | fine di carta |
| `(c. 3r)` | numero di carta, dopo la barra |
| `[...]` | guasto materiale: lettere o parole illeggibili per danno del supporto |
| `[parola]` | integrazione congetturale dell'editore |
| `‹parola›` | sillabe o parole cassate dalla scrivente — **solo in apparato** |

Le parentesi quadre hanno due valori, distinti dal contenuto: con i punti sospensivi segnalano un guasto del testimone, con del testo segnalano una congettura. La distinzione è sufficiente perché una congettura è sempre testo e un guasto è sempre e solo `[...]`.

Nella codifica TEI il cambio di carta è portato da `<pb/>`: i segni di questa tabella sono la resa a stampa di quella marcatura.

## 6. L'apparato

L'apparato è unico e riunisce tre ordini di informazione, distinti da una sigla:

1. **Genetica.** Cassature entro parentesi uncinate; aggiunte interlineari e marginali; sovrascritture; riscritture; ripensamenti e ogni altra caratteristica notevole dell'autografo.
2. **Filologico-linguistica.** Lezioni incerte; interventi di lettura contestabili, in particolare le separazioni e le unioni di N7; forme che si è scelto di conservare e che il lettore potrebbe credere errori di stampa; identificazioni onomastiche e toponimiche.
3. **Commento.** Realia, riferimenti scritturali e liturgici, contesto storico-istituzionale.

**Nessun fenomeno genetico compare nel testo interpretativo.** Il testo porta una sola lezione, l'ultima voluta dalla scrivente; la stratificazione vive in apparato.

## 7. Ordine di applicazione

Le classi non sono indipendenti: `seruitij` richiede N2 e N4 per dare *servizi*, e `per che` va unito (N7) prima di essere accentato (N6). L'ordine è fissato, e in caso di conflitto **prevale la classe di numero minore**:

**N1** → **N2** → **N3** → **N4** → **N5** → **N7** → **N6** → **N9** → **N8**

N8 viene per ultima perché dipende dalla punteggiatura per le maiuscole di inizio periodo. Il criterio del § 2 prevale su tutte: nessuna classe autorizza un intervento che cambi il numero di sillabe o la qualità di una vocale.

## 8. Decisioni e alternative scartate

Ogni decisione qui elencata era aperta, e ciascuna produce effetti su decine di luoghi. Sono dichiarate perché il lettore possa dissentire con cognizione.

| decisione | ragione | alternativa scartata |
|---|---|---|
| `havea` > **avea** | la *h* è grafica, la desinenza è morfologica | *aveva*, che modernizza la morfologia |
| `Monasterio` > **monasterio** | cade la maiuscola, resta il lessico | *monastero*, che sostituisce la parola |
| **Casa Professa** maiuscolo | nome proprio dell'istituzione | *casa professa*, che falsa il referente |
| `et` + vocale > **ed** | continuità fonica del periodo, come nel modello di riferimento | *e*, secondo l'uso corrente |
| `offitio` > **offizio** | si regolarizza il nesso, non la parola | *ufficio*, forma diversa |
| `difficultà`, `Immaculata`, `Giesù` **conservati** | differenza di vocale, non di veste | uniformazione alle forme moderne |
| `Doppo` > **doppo** | geminata reale: cade solo la maiuscola | *dopo*, che interviene sul consonantismo |
| `-ij` > **-i** | convenzione grafica senza riscontro fonologico | conservazione del segno |
| **`-tione` > `-zione`** | il nesso rende con veste latina un suono che l'italiano scrive `-zi-`: è grafia, non forma | conservazione del nesso |
| oscillazioni **non uniformate** | l'oscillazione è un dato | uniformazione alla forma maggioritaria |

**Sulla decisione `-tione`.** L'edizione digitale del *Castello dell'anima* — altro autografo monastico siciliano di fine Seicento, Palermo BCP 2 Qq E 29, curato dallo stesso editore — dichiara invece che «il nesso latineggiante *-ti-* (‑*tione*) non si normalizza», e conserva `interpellatione`. La divergenza è voluta e riposa sulla differenza fra i due prodotti: quella è un'edizione **documentaria** a testo base conservativo, dove la normalizzazione vive nella marcatura e il caso dubbio si conserva; questa è un **testo di lettura**, dove ogni forma conservata è un ostacolo per il destinatario. L'edizione a stampa del *Castello* (Casapullo 2015), anch'essa testo di lettura, normalizza. La regola che ne risulta, valida per entrambi i progetti: **`-tione` si normalizza nei testi di lettura, si conserva nelle edizioni documentarie.**

## 9. Dove il testo porta una decisione umana

Sette classi di casi non sono state affidate ad alcuna procedura automatica e sono state decise dall'editore, punto per punto. Il lettore che voglia controllare le scelte dell'edizione cominci da qui.

1. **Integrazione congetturale.** Nessuna lacuna è stata riempita automaticamente: `[...]` resta `[...]`, e ogni congettura è dichiarata in apparato.
2. **Stratificazione genetica.** La scelta della lezione a testo fra cancellature, ripensamenti e sovrascritture.
3. **Lezione materialmente incerta.** Quanto il livello A marca come incerto resta incerto, e in particolare non si scioglie l'alternanza `[h]o`.
4. **Maiuscola di istituzioni e toponimi**, che richiede verifica documentaria esterna al testo.
5. **Unione e separazione ambigue**, dove entrambe le segmentazioni danno un senso.
6. **Punteggiatura in luogo sintatticamente ambiguo**, dove la collocazione del segno decide il senso del periodo.
7. **Ogni caso non previsto da questa Nota**, che non si risolve per analogia.

## 10. Rapporto con il protocollo AI-assistito

Questa edizione nasce dentro un esperimento metodologico sull'uso di modelli linguistici come acceleratori sorvegliati nella trascrizione. Il regime descritto in questa Nota è la sua **norma di riferimento**: il prompt che guida il modello al livello B (`prompts/prompt-B-interpretativa.md`) non è una fonte autonoma, ne è la forma eseguibile, e in caso di divergenza prevale la Nota.

Le classi `N1`–`N9` sono anche le unità di misura del protocollo: ogni intervento dell'editore sull'output del modello è registrato con la sua classe nel log editoriale (`data/LOG_editoriale_AI.xlsx`), e la densità di intervento si calcola per classe, perché una classe può essere stabile mentre un'altra non lo è. Parametri, soglie e metodo sono in `protocollo/Protocollo_v1.0.md` e `docs/PARAMETRI.md`.

Ciò che il protocollo non modifica è il § 9: i casi non delegabili restano non delegabili, e nessuna misura di stabilizzazione li rende automatizzabili.

## 11. Fonti dei criteri

I criteri derivano dalla *Nota al testo* premessa all'edizione a stampa del ***Castello dell'anima*** (R. Casapullo, a cura di, Alessandria, Edizioni dell'Orso, 2015), che per un autografo monastico siciliano coevo adotta l'intervento moderato a favore della leggibilità. Il trasferimento a un altro testimone è una scelta dell'editore, qui dichiarata, giustificata dall'omogeneità di tipologia e verificata classe per classe sullo spoglio di A 31.

Rispetto a quel modello questa Nota **estende** il regime in tre direzioni, sulla base dello spoglio: normalizzazione dei nessi latinizzanti (N4), della *h* etimologica (N3) e della congiunzione `et` (N5); e **rivede** il trattamento delle maiuscole, abolendo la reverenziale e la maiuscola di rispetto sui nomi comuni (N8).

Il fondamento di questi criteri nella pratica delle edizioni digitali ad accesso aperto — che cosa condividono, su che cosa si scostano e con quale argomento — è in [`docs/Ricognizione_normalizzazioni.md`](Ricognizione_normalizzazioni.md).

## 12. Versioni

Questa Nota è **versionata e citabile**: una modifica ai criteri è una nuova versione, non una correzione, e il testo interpretativo dichiara sempre sotto quale versione è stato prodotto. Una riscrittura che non tocchi i criteri è invece una **revisione redazionale**, e non cambia il numero di versione: il regime resta lo stesso, e resta valido ogni riferimento a esso.

| | data | |
|---|---|---|
| **1.0** | 2026-09-27 | Prima redazione. Criteri della *Nota al testo* del *Castello dell'anima* trasferiti al testimone A 31 ed estesi con N3 (h etimologica), N4 (nessi latinizzanti), N5 (`et`) e la revisione di N8 (maiuscola reverenziale). Formalizzazione del criterio-limite, dell'ordine di applicazione e dei casi non delegabili. |
| 1.0, rev. | 2026-09-28 | Revisione redazionale: il documento è riscritto per il lettore dell'edizione anziché per il gruppo di lavoro. **Nessun criterio modificato** — regole, esempi, conteggi, decisioni e ordine di applicazione sono invariati. Eliminato il piano di lavoro interno; lo stato del testo interpretativo è dichiarato in apertura; l'eccezione per il latino è in testa alle classi, perché vale per due di esse; le decisioni e la divergenza sul nesso `-tione` sono argomentate anziché tabulate. Restano perciò validi senza modifiche il *Prompt B* 2.0 e la skill che lo incapsula, che dichiarano il regime della Nota **1.0**. |
