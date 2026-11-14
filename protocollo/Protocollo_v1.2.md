Sì. Esaminando la versione attualmente pubblicata su GitHub, ho individuato alcune incoerenze effettive. Non sono tutte dello stesso tipo: alcune sono contraddizioni documentali, altre riguardano la corrispondenza tra metodo dichiarato e applicazione sperimentale.

La distinzione è importante: non considero contraddittorio un esperimento incompleto quando è dichiarato come tale. Considero invece incoerente una documentazione che attribuisce versioni o condizioni diverse allo stesso elemento.

## 1. Incoerenze accertabili

### 1.1 Versione del Prompt A

Contraddizione documentaleNel README, nella descrizione della struttura, si legge:

- Prompt A v1.3.
- Prompt B v2.1.

In `docs/PARAMETRI.md`, invece, nella sezione dei modelli confrontati:

- Prompt A v1.4.
- Prompt B v2.1.

La versione di Prompt A è quindi discordante tra due documenti che descrivono la configurazione sperimentale corrente.

Non è una differenza interpretativa: è una discrepanza oggettiva.

GitHub

+1

### 1.2 Stato della trascrizione interpretativa

Disallineamento di statoLa Nota al testo, §1, dichiara esplicitamente che `A31_interpretativa.xml` è stato prodotto con un regime editoriale precedente e deve essere rifatto.

Il README, invece, presenta le 72 carte in TEI ai due livelli come parte della prima applicazione archiviata.

Le due affermazioni non sono propriamente incompatibili: le trascrizioni esistono, ma quella interpretativa non è conforme alla Nota attuale.

Il problema è che questa distinzione non è sufficientemente evidente nella presentazione generale dei dati.

Il repository contiene quindi una trascrizione interpretativa che non rappresenta l'applicazione della norma editoriale attualmente vigente.

GitHub

+1

### 1.3 Parametri dichiarati e sperimentazione effettiva

Scostamento operativo dichiarato`PARAMETRI.md` stabilisce:

- θ = 5 interventi per 1000 parole.
- N = 10 facciate consecutive.
- K = 3 ripetizioni.

Lo stesso documento dichiara però che il rodaggio delle unità 1–5 è stato eseguito con K=1 e che K=3 è rinviato.

Non considero questo una contraddizione interna, perché lo scostamento è esplicitamente documentato.

È però importante non descrivere i risultati del rodaggio come risultati ottenuti con il protocollo K=3.

GitHub

## 2. Incoerenze tra protocollo e perimetro sperimentale

### 2.1 Il caso BCP 3 Qq B 49

Incoerenza sostanzialeQuesta è più importante della precedente.

Il protocollo v1.2, §4, afferma:

> Il workflow è testato su campioni di due manoscritti.

Descrive B49 come secondo testimone impiegato per verificare la trasferibilità delle norme.

Anche il §5 parla del confronto A31 → B49 come misura della riduzione degli interventi.

Il README, invece, descrive B49 come banco di trasferibilità in fase successiva e identifica A31 come caso di applicazione principale.

Il changelog documenta inoltre l'archiviazione della prima applicazione su A31, senza documentare una corrispondente applicazione su B49.

Quindi esiste una discrepanza tra:

- La descrizione dello stato sperimentale nel protocollo.
- Lo stato dichiarato nel README.
- I materiali di applicazione effettivamente descritti nell'archivio.

Non posso concludere, sulla sola base di questi documenti, che non esistano prove esterne dell'esperimento B49. Posso però affermare che il repository non documenta in modo coerente il suo stato.

GitHub

+2

### 2.2 Protocollo sperimentale e risultati presentati

Disallineamento espositivoNel protocollo, §5, alcune formulazioni sono assertive:

- Il workflow mostra una riduzione della ridondanza decisionale.
- I modelli segnalano le ambiguità.
- Il confronto tra manoscritti misura la trasferibilità.

Tuttavia, la stessa sezione introduce risultati che dovrebbero derivare da un confronto sperimentale sui due testimoni.

Dato che la documentazione generale dichiara ancora B49 in fase successiva, queste affermazioni non sono adeguatamente distinguibili da risultati già ottenuti.

Il problema non è la formulazione dell'ipotesi scientifica: è la sovrapposizione fra risultati osservati, risultati attesi e obiettivi dell'esperimento.

GitHub

+1

## 3. Incoerenze nella norma editoriale

Qui ho esaminato anche il testo della Nota al testo, non soltanto la descrizione generale.

### 3.1 Il criterio delle vocali e la normalizzazione

La Nota stabilisce al §2 che non si interviene quando la modifica cambia la qualità di una vocale.

Al §4 dichiara di conservare:

- `Immaculata` / `Immacolata`
- `difficultà` / `difficoltà`
- `Giesù` / `Gesù`

La regola è coerente con gli esempi.

Non rilevo quindi una contraddizione in questo punto.

### 3.2 La distinzione tra normalizzazione grafica e interpretazione

Qui esiste invece una tensione interna, ma dichiarata.

Il §2 definisce il perimetro come normalizzazione della veste grafica, senza interventi su morfologia, lessico e sintassi.

Il §7 include però tra le operazioni N7 la separazione di `egli` in `e gli`, riconoscendo esplicitamente che si tratta di un'interpretazione e non di una semplice normalizzazione grafica.

La Nota risolve la questione segnalando questi casi in apparato.

Non è una contraddizione irrisolta: è una deroga consapevole al criterio generale, esplicitamente circoscritta.

### 3.3 L'ordine delle classi N1–N9

La Nota stabilisce:

N1 → N2 → N3 → N4 → N5 → N7 → N6 → N9 → N8.

L'ordine è motivato da dipendenze tra trasformazioni.

Non ho individuato una contraddizione evidente tra questa sequenza e la spiegazione delle singole classi.

Anche la distinzione tra latino e italiano è esplicita e coerente con gli esempi riportati.

GitHub

## 4. Incoerenze tra strumenti e documentazione

### 4.1 Data dictionary e parametri

Ho verificato anche direttamente `schema/data-dictionary.md`.

Qui i valori riportati sono:

- θ = 5.
- N = 10.
- K = 3.
- Prompt A v1.4.
- Prompt B v2.1.
- Protocollo v1.2.

Questi dati sono coerenti con `PARAMETRI.md`.

La discrepanza della versione A è quindi circoscritta al README, non all'intera documentazione.

GitHub

+1

### 4.2 Automazione e archivio

Il changelog dichiara che lo spostamento del workflow in `Archive/` ha disattivato il controllo automatico di allineamento dei CSV.

Questo non è contraddittorio con il protocollo: è una conseguenza del riordino documentata esplicitamente.

Anche qui distinguerei un'incoerenza da una funzionalità momentaneamente non attiva.

GitHub

## 5. Quadro riepilogativo

Questa è la classificazione delle discrepanze che ho effettivamente riscontrato.

| Elemento | Tipo | Rilevanza |
| --- | --- | --- |
| Prompt A v1.3 / v1.4 | Contraddizione | Alta |
| Stato della TEI interpretativa | Disallineamento | Alta |
| Stato sperimentale B49 | Contraddizione tra documenti | Molto alta |
| Risultati del §5 del protocollo | Ambiguità espositiva | Alta |
| K=1 rispetto a K=3 | Scostamento dichiarato | Media |
| Criterio grafico e N7 | Deroga dichiarata | Bassa |
| Workflow archiviato | Stato operativo dichiarato | Bassa |

## 6. Giudizio conclusivo

La mia impressione, dopo questa verifica, è che il problema principale del repository non sia la coerenza della sua impostazione filologica.

La Nota al testo è complessivamente coerente e il rapporto tra i due livelli è ben definito.

Le criticità maggiori si trovano nel rapporto tra tre piani:

1. Il protocollo metodologico v1.2.
2. La prima applicazione effettivamente documentata.
3. Lo stato attuale degli strumenti e dei risultati.

In particolare, il caso B49 e la versione di Prompt A sono le due discrepanze documentali che considero più nette.

Non rilevo, invece, una contraddizione fondamentale nei principi scientifici del metodo.

Il punto che merita maggiore attenzione è che il protocollo v1.2, nella sua formulazione attuale, presenta come sperimentato su due manoscritti un workflow che il README descrive ancora come applicato principalmente ad A31, con B49 destinato alla fase successiva.

Questa è la discrepanza scientificamente più importante tra quelle individuate.

Ho limitato la verifica ai documenti accessibili e confrontabili nel repository; non considero verificati i contenuti interni di ogni singolo file TEI e workbook Excel.

GitHub

+3
