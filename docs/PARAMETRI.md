# Parametri dichiarati a priori

**Protocollo:** v1.0 (congelato) · **Parametri fissati il:** 2026-08-23 · **Stato:** attivo · **Ultima revisione redazionale:** 2026-09-28

> I valori di θ, N e K sono invariati dal 23 agosto 2026. Le revisioni successive a quella data riguardano gli strumenti dichiarati e la definizione operativa della metrica, non le soglie.

Questi parametri sono dichiarati **prima** dell'avvio della Fase 1 (verifica sulle immagini) e valgono per l'intero esperimento. La loro dichiarazione anticipata è una scelta metodologica: garantisce che le soglie non siano ritagliate a posteriori sui risultati. Ogni modifica successiva comporta un incremento di versione del protocollo, documentato nel [CHANGELOG](../CHANGELOG.md) con la motivazione.

## Valori

| Parametro | Valore | Definizione operativa |
|-----------|--------|-----------------------|
| **θ** (soglia) | 5 interventi / 1000 parole | Soglia di stabilizzazione: sotto questo valore la densità di intervento è considerata assestata. |
| **N** (finestra) | 10 carte consecutive | Ampiezza su cui la densità deve restare ≤ θ perché una classe sia dichiarata stabilizzata. |
| **K** (loop) | 3 ripetizioni per modello | Numero di esecuzioni della stessa unità per modello, per misurare il non-determinismo e prendere la forma di consenso. |

## Metrica

Densità di intervento:

**D = interventi ÷ (parole / 1000)**

calcolata sul totale, per modello e per classe. Il denominatore (parole) è raccolto nel foglio `COPERTURA` del log.

Il log registra ogni intervento su **due dimensioni distinte**, e la distinzione è necessaria perché non misurano la stessa cosa:

- **`TIPO_ERRORE`** descrive il **modo di fallimento**: lettura errata, omissione di testo, duplicazione, scioglimento errato, stratificazione non segnalata.
- **`CLASSE_NOTA`** indica a quale delle nove **classi di normalizzazione** della [*Nota al testo*](Nota_al_testo.md) l'intervento appartiene: `N1` abbreviazioni, `N2` u/v e i/j, `N3` h etimologica, `N4` nessi latinizzanti, `N5` `et`, `N6` accenti e diacritici, `N7` unione e separazione, `N8` maiuscole, `N9` punteggiatura. Gli eventi che non appartengono ad alcuna classe — gli errori di lettura, che riguardano il livello A — portano `NA_fuori_classe`.

Una **classe di normalizzazione** è **stabilizzata** quando **D ≤ θ per N carte consecutive**. La stabilizzazione si valuta su `CLASSE_NOTA` e non sul totale, perché una classe può essere assestata mentre un'altra non lo è: un dato aggregato nasconderebbe proprio l'informazione che il protocollo cerca.

## Ruolo del loop K

In interfaccia chat la temperatura di decodifica spesso non è impostabile. Il controllo della variabilità (non-determinismo del modello) non è quindi affidato alla temperatura ma al **loop K = 3**: tre passate della stessa unità per modello, dalle quali si ricava la forma di consenso. K non elimina la variabilità: la rende **misurabile**.

## Modelli confrontati

Gemini e Claude, ai livelli A (diplomatico) e B (interpretativo), con gli stessi prompt incapsulati come skill/Gem versionate — **Prompt A v1.3, Prompt B v2.0** — identiche a ogni esecuzione. La versione del prompt è l'unica variabile controllata dell'esperimento.

Il livello B è governato dalla **[*Nota al testo*](Nota_al_testo.md) v1.0**, che è la norma editoriale dell'esperimento: il Prompt B non è una fonte autonoma ma la sua forma eseguibile, e in caso di divergenza prevale la Nota.

**Un cambio di regime editoriale è un cambio di strumento.** Comporta una nuova versione del prompt e l'azzeramento dei contatori di densità per le classi introdotte o modificate: una stabilizzazione acquisita sotto un regime precedente non è trasferibile al nuovo, perché non misurava le stesse classi. È la ragione per cui gli eventi registrati prima del 28 settembre 2026 non portano `CLASSE_NOTA`: sono stati prodotti sotto il Prompt B v1.2, che non conosceva le classi N3, N4 e N5.

## Dove sono registrati anche

- Foglio `PARAMETRI` in `data/LOG_editoriale_AI.xlsx` (log vivo) e in `data/LOG_editoriale_AI_template.xlsx` (modello vuoto)
- `schema/data-dictionary.md` (sezione PARAMETRI e Metrica)
- `.zenodo.json` (metadati di deposito)

## Regola di modifica

I parametri sono **congelati**. Qualsiasi cambiamento di θ, N o K non è una modifica silenziosa: si apre una nuova versione del protocollo (es. v1.1), si annota nel CHANGELOG la motivazione e la data, e si dichiara da quale unità la nuova soglia si applica.

Le **versioni dei prompt e della Nota al testo non sono parametri**: si aggiornano senza aprire una versione del protocollo, ma ogni aggiornamento è datato qui e nel [CHANGELOG](../CHANGELOG.md), e comporta le conseguenze sui contatori dichiarate sopra.

## Stato operativo — rodaggio u.1–5 (2026-08-24)

Il rodaggio di **BCP 2 Qq A 31**, unità 1–5 (carte 1–5, oltre a frontespizio e c. 6r), è stato eseguito con **una passata per modello (K=1)**: Prompt A e Prompt B su Gemini e Claude, con validazione umana ai due livelli e log popolato (49 eventi, 9 norme emergenti). I denominatori sono registrati nel foglio COPERTURA.

Il **loop K=3** — ripetizioni per modello per misurare il non-determinismo e assumere la forma di consenso — è **rinviato (backlog)** e sarà eseguito in una fase successiva. Poiché **K=3 resta il valore dichiarato** del protocollo, questo è uno **scostamento operativo tracciato**, non una modifica del parametro.
