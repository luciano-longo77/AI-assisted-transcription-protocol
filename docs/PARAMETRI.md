# Parametri dichiarati a priori

**Protocollo:** v1.2 · **Parametri fissati il:** 2026-08-23 · **Stato:** attivo · **Ultima revisione redazionale:** 2026-11-14

> I valori di θ, N e K sono invariati dal 23 agosto 2026. Le revisioni successive a quella data riguardano gli strumenti dichiarati e la definizione operativa della metrica, non le soglie.

Questi parametri sono dichiarati **prima** dell'avvio della Fase 1 (verifica sulle immagini) e valgono per l'intero esperimento. La loro dichiarazione anticipata è una scelta metodologica: garantisce che le soglie non siano ritagliate a posteriori sui risultati. Ogni modifica successiva comporta un incremento di versione del protocollo, documentato nel [CHANGELOG](../CHANGELOG.md) con la motivazione.

---

## Indice

- [Valori](#valori)
- [Metrica](#metrica)
- [Ruolo del loop K](#ruolo-del-loop-k)
- [Modelli confrontati](#modelli-confrontati)
- [Dove sono registrati anche](#dove-sono-registrati-anche)
- [Regola di modifica](#regola-di-modifica)
- [Stato operativo](#stato-operativo)

---

## Valori

| Parametro | Valore | Definizione operativa |
|-----------|--------|-----------------------|
| **θ** (soglia) | 5 interventi / 1000 parole | Soglia di stabilizzazione: sotto questo valore la densità di intervento è considerata assestata. |
| **N** (finestra) | 10 facciate consecutive | Ampiezza su cui la densità deve restare ≤ θ perché una classe sia dichiarata stabilizzata. Si conta in facciate: due immagini contigue condividono una carta. |
| **K** (loop) | 3 ripetizioni per modello | Numero di esecuzioni della stessa unità per modello, per misurare il non-determinismo e prendere la forma di consenso. Valore **dichiarato** del protocollo: un'esecuzione che adotti un K diverso lo dichiara come scostamento tracciato (cfr. *Stato operativo*). |

## Metrica

Densità di intervento:

**D = interventi ÷ (parole / 1000)**

calcolata sul totale, per modello e per classe. Il denominatore (parole) è raccolto nel foglio `COPERTURA` del log.

Il log classifica ogni intervento con **`TIPO_ERRORE`**, che ne descrive il **modo di fallimento**: lettura errata, omissione o duplicazione di testo, scioglimento errato, normalizzazione mancata o indebita, stratificazione non segnalata, latino normalizzato, lacuna integrata. È su questo campo che si calcola la densità per classe.

Le nove classi di normalizzazione della [*Nota al testo*](Nota_al_testo.md) — `N1` abbreviazioni, `N2` u/v e i/j, `N3` h etimologica, `N4` nessi latinizzanti, `N5` `et`, `N6` accenti e diacritici, `N7` unione e separazione, `N8` maiuscole, `N9` punteggiatura — sono il vocabolario con cui l'editore nomina e motiva l'intervento nel campo `DECISIONE_EDITORIALE`, non un asse della misura.

Una **classe** è **stabilizzata** quando **D ≤ θ per N facciate consecutive** senza intervento sistematico; altrimenti è ricorrente. La classe di riferimento è il valore di `TIPO_ERRORE`: la stabilizzazione si dichiara per tipo di errore e per modello, non sul solo totale, perché un tipo può essere assestato mentre un altro non lo è.

È **sistematico** l'intervento che ricorre nella finestra su più unità con la stessa causa e la stessa correzione; un'occorrenza isolata non lo è, quale che ne sia la gravità. Le due condizioni sono congiuntive: finché un intervento sistematico persiste, la classe resta ricorrente anche con D sotto soglia (protocollo, M4).

## Ruolo del loop K

In interfaccia chat la temperatura di decodifica spesso non è impostabile. Il controllo della variabilità (non-determinismo del modello) non è quindi affidato alla temperatura ma al **loop K**: K passate della stessa unità per modello, dalle quali si ricava la forma di consenso. K non elimina la variabilità: la rende **misurabile**.

**Il consenso richiede K dispari.** Con K = 3 la lezione di maggioranza è la forma di consenso e va in `FORMA_AI`; se le tre passate divergono tutte, consenso non c'è e il caso torna all'editore come `non_delegabile`. Con un **K pari** la maggioranza non esiste mai: le passate coincidono — e l'esecuzione è deterministica per quell'unità — oppure divergono, e ogni divergenza è `non_delegabile`. Un K pari misura dunque la stabilità senza delegare alcuna lezione a un voto, al prezzo di non sapere quale forma il modello preferisca.

In nessun caso il consenso misura l'accuratezza: passate concordi possono essere concordemente errate, e la forma accolta resta soggetta alla validazione umana.

## Modelli confrontati

Gemini e Claude, ai livelli A (diplomatico) e B (interpretativo), con gli stessi prompt incapsulati come skill/Gem versionate — **Prompt A v1.4, Prompt B v2.1** — identiche a ogni esecuzione. La versione del prompt è **tenuta costante**, così che l'unica differenza fra le esecuzioni confrontate sia il modello: il prompt è la variabile controllata dell'esperimento, il modello la variabile indipendente.

Il livello B è governato dalla **[*Nota al testo*](Nota_al_testo.md) v1.0**, che è la norma editoriale dell'esperimento: il Prompt B non è una fonte autonoma ma la sua forma eseguibile, e in caso di divergenza prevale la Nota.

**Un cambio di regime editoriale è un cambio di strumento.** Comporta una nuova versione del prompt e l'azzeramento dei contatori di densità: una stabilizzazione acquisita sotto un regime precedente non è trasferibile al nuovo, perché non misurava gli stessi fenomeni. È la ragione per cui gli eventi della prima applicazione, prodotti sotto il Prompt B v1.2 che non conosceva le classi N3, N4 e N5 della Nota, restano in `Archive/` e non alimentano la misura della ripartenza.

## Dove sono registrati anche

- Foglio `PARAMETRI` in `data/LOG_editoriale_AI_template.xlsx` (strumento vuoto); il log popolato della prima applicazione è in `Archive/`
- `schema/data-dictionary.md` (sezione PARAMETRI e Metrica)
- `Archive/.zenodo.json` (metadati di deposito della prima applicazione; il repository attivo non ha ancora metadati di deposito propri)

## Regola di modifica

I parametri sono **congelati**. Qualsiasi cambiamento di θ, N o K non è una modifica silenziosa: si apre una nuova versione del protocollo (es. v1.3), si annota nel CHANGELOG la motivazione e la data, e si dichiara da quale unità la nuova soglia si applica.

Le **versioni dei prompt e della Nota al testo non sono parametri**: si aggiornano senza aprire una versione del protocollo, ma ogni aggiornamento è datato qui e nel [CHANGELOG](../CHANGELOG.md), e comporta le conseguenze sui contatori dichiarate sopra.

## Stato operativo

**Prima applicazione (agosto–settembre 2026): archiviata.** L'applicazione su **BCP 2 Qq A 31**, tratto frontespizio–c. 36r, è stata condotta ai due livelli e con entrambi i modelli sotto le versioni allora vigenti dei prompt, e con **una passata per modello (K = 1)**. I suoi dati — log popolato, denominatori, norme emergenti, trascrizioni TEI — sono conservati e citabili in `Archive/`.

Quei dati **non alimentano la misura della nuova applicazione**. Il livello B è stato prodotto sotto un regime editoriale anteriore alla *Nota al testo* 1.0, che non conosceva le classi `N3`, `N4` e `N5`: non misurava gli stessi fenomeni, e una stabilizzazione acquisita allora non è trasferibile. I contatori di densità **ripartono da zero**; il livello A, che non normalizza, resta valido come trascrizione ma non come misura del regime corrente.

**Nuova applicazione: avviata (novembre 2026).** Sotto il protocollo v1.2 e la *Nota al testo* 1.0 sono state processate le prime **4 unità digitali** — frontespizio e cc. 1r–3r — ai due livelli (livello A il 2026-11-16, livello B il 2026-11-17), con entrambi i modelli e il pilota a K = 2. Esiti validati e committati: `tei/A31_diplomatica.xml`, `tei/A31_interpretativa.xml`, `data/trascrizioni/`, e il log popolato `data/LOG_editoriale_AI.xlsx` (26 eventi A + 6 B). La dichiarazione d'ambiente V1 è compilata nel foglio PARAMETRI del log (versione dei modelli, date, K applicato). La misura di densità non è ancora significativa: la finestra N = 10 facciate non è raggiunta (6 facciate lavorate).

**Valore di K per la nuova applicazione.** **K = 3 resta il valore dichiarato** del protocollo. Ogni esecuzione che adotti un K diverso lo dichiara qui come **scostamento operativo tracciato**, con la sua motivazione e la sua estensione: è ciò che è stato fatto per il rodaggio di agosto, eseguito a K = 1, che ha lasciato non misurata la garanzia V7 sul tratto interessato.

**Pilota: K = 2, dichiarato prima dell'esecuzione.** Il pilota su **BCP 2 Qq A 31** è eseguito a **due passate per modello e per livello**. La scelta è motivata: due passate bastano a distinguere l'unità stabile dall'unità instabile, e quindi a produrre il dato di V7 che manca dal rodaggio, senza il costo di dodici output per unità. L'assenza di maggioranza è deliberata: il probe di agosto aveva mostrato che il consenso a maggioranza può accogliere un errore stabile, e a K = 2 nessuna lezione viene accolta per voto. Il valore applicato è registrato anche nel foglio PARAMETRI dello strumento di log, alla riga `K applicato`. Il K del tratto lungo sarà deciso sui risultati del pilota e dichiarato qui prima di eseguirlo.
