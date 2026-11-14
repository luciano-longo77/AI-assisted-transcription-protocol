# Changelog

## Indice

- [0.8.0-protocollo-v1.2 · 2026-11-14](#080-protocollo-v12--2026-11-14)
- [0.7.0-riordino · 2026-11-01](#070-riordino--2026-11-01)
- [0.6.0-norma · 2026-09-28](#060-norma--2026-09-28)
- [0.5.0-automazione · 2026-09-27](#050-automazione--2026-09-27)
- [0.4.0-protocolloB · 2026-08-25](#040-protocollob--2026-08-25)
- [0.3.0-protocolloA · 2026-08-25](#030-protocolloa--2026-08-25)
- [0.2.0-rodaggio · 2026-08-25](#020-rodaggio--2026-08-25)
- [0.1.0-setup · 2026-08](#010-setup--2026-08)

---

## [0.8.0-protocollo-v1.2] — 2026-11-14
### Aggiunto
- **Protocollo v1.2** in `protocollo/Protocollo_v1.2.md`, con indice. Due modifiche sostanziali rispetto alla v1.0: definizione dell'**unità digitale** e rinvio del regime editoriale del livello B alla norma del testimone. Principi P1–P6, metrica M1–M3, garanzie V1–V7, procedura in sei passi e log a 12 campi invariati; le applicazioni condotte sotto la v1.0 restano conformi.
- **Norma editoriale (Nota al testo)** fra i Componenti del protocollo: documento versionato che fissa il regime del livello B per il testimone, esplicitato prima dell'automazione (P2). I prompt ne sono la forma eseguibile; in caso di divergenza prevale la norma.
- `Casi_dopo_agosto_2026.md`: registro dei dodici casi da settembre a oggi, con quadro d'insieme e stato dei lavori aperti.
### Deciso
- **Unità digitale** = l'immagine, cioè la coppia di facciate affacciate (es. `cc. 9v-10r`), che insiste su due carte. **Unità di misura** = la facciata, perché due immagini contigue condividono una carta e il conteggio per carta si sovrapporrebbe. La finestra vale quindi **N = 10 facciate consecutive** (cinque unità).
- **Log a 12 campi**: respinta l'aggiunta del campo `CLASSE_NOTA` introdotta il 2026-09-28 (cfr. 0.6.0). La densità si misura per `TIPO_ERRORE` e per modello; la stabilizzazione si dichiara per tipo di errore, non per classe editoriale.
- Il protocollo **non riassume più** il regime del livello B: la riga dei Componenti rimanda alla Nota al testo.
### Corretto
- **M4** riformulato in facciate anziché in carte, per coerenza con l'unità di misura.

## [0.7.0-riordino] — 2026-11-01
### Aggiunto
- Cartella **`Archive/`**: vi sono stati spostati i materiali della prima applicazione su BCP 2 Qq A 31 — log popolato (135 eventi, 368 occorrenze) e sue viste CSV, le due trascrizioni TEI (frontespizio–c. 36r), `NORME_EMERGENTI.csv`, `scripts/xlsx_to_csv.py` e il workflow. Tutti i file verificati byte per byte contro le versioni di partenza.
### Nota
- Separazione fra **il protocollo e la sua prima applicazione**: fuori dall'archivio restano metodo, norma, strumenti e vocabolari. Il protocollo diventa così trasferibile a un altro testimone e a un altro ricercatore senza i dati di questo — condizione della replicabilità dichiarata al §Riproducibilità.
- Riportati alla radice quattro file infrastrutturali, che non sono dati: `LICENSE` (un repository pubblico dichiara i termini alla radice), `.gitignore` (tiene fuori dal versionamento le immagini coperte da diritti della biblioteca), `CHANGELOG.md` (il protocollo prescrive che le proprie versioni siano tracciate), `data/LOG_editoriale_AI_template.xlsx` (strumento vuoto: cinque fogli, menu a tendina e vocabolari).
- Restano in `data/` i vocabolari controllati (`LISTE.csv`) e i parametri (`PARAMETRI.csv`), indipendenti dalle carte trascritte.
- Spostare il workflow in `Archive/` lo disattiva: il controllo automatico di allineamento dei CSV non è più in funzione.

## [0.6.0-norma] — 2026-09-28
### Aggiunto
- **`docs/Nota_al_testo.md` v1.0**: il regime editoriale del livello B, che fino a questo momento viveva soltanto dentro il Prompt B. Criterio-limite («si normalizza la veste grafica, non morfologia, lessico, sintassi») con prova di controllo su sillabe e vocali; nove classi `N1`–`N9` con ordine di applicazione; forme che si conservano; segni dell'edizione; apparato; sette casi riservati all'editore. I criteri derivano dalla *Nota al testo* dell'edizione a stampa del *Castello dell'anima* (Casapullo 2015) e la estendono su *h* etimologica, nessi latinizzanti e congiunzione `et`; la maiuscola reverenziale è abolita.
- **`docs/Ricognizione_normalizzazioni.md`**: fondamento comparativo dei criteri rispetto a sei edizioni e corpora ad accesso aperto (Red CHARTA, MENOTA, OVI/TLIO, ARTESIA, *Castello* a stampa e digitale), con appendice sulla corrispondenza fra le classi e i figli di `editorialDecl` in TEI P5.
- **Prompt B v2.0** in `prompts/prompt-B-interpretativa.md`: non un aggiornamento della v1.2 ma un altro regime. Porta le nove classi nell'ordine fissato dalla Nota, l'eccezione di lingua (N3 e N4 non toccano il latino), la tavola di conversione dei marcatori del Prompt A, gli otto casi non delegabili con clausola di chiusura, l'output in due blocchi (testo e registro delle classi contestabili) e dieci regole rafforzate derivate dalle derive misurate sui testi della v1.2.
- Campo **`CLASSE_NOTA`** (14° del foglio LOG_ERRORI) con vocabolario chiuso `N1`–`N9` più `NA_fuori_classe`, per calcolare la densità per classe di normalizzazione. *Decisione revocata il 2026-11-14: cfr. 0.8.0.*
### Corretto
- `docs/PARAMETRI.md`: dichiarata la revisione redazionale con l'avvertenza che θ, N e K sono invariati dal 2026-08-23; nominata la Nota al testo come norma del livello B; distinto, nella regola di modifica, ciò che è parametro da ciò che è versione di uno strumento.
### Nota
- **Decisione sostanziale dichiarata:** il nesso `-tione` si normalizza in `-zione`, con divergenza esplicita rispetto all'edizione digitale del *Castello dell'anima* (ms. BCP 2 Qq E 29), che lo conserva. La regola generale che ne deriva, valida per entrambi i progetti: si normalizza nei testi di lettura, si conserva nelle edizioni documentarie.
- I testi prodotti sotto il Prompt B v1.2 **non sono confrontabili** con quelli prodotti sotto la v2.0. La trascrizione interpretativa in repository resta prodotta sotto il regime precedente e va rifatta.
- Quattro delle norme in `NORME_EMERGENTI` — conservazione del nesso `-tti-`, di `et`, della *h* etimologica e della maiuscola reverenziale — risultano rovesciate dalla Nota 1.0.

## [0.5.0-automazione] — 2026-09-27
### Aggiunto
- **Vista CSV del log** e controllo automatico di allineamento: `scripts/xlsx_to_csv.py` rigenera i sette fogli in `data/csv/`, e il workflow `.github/workflows/csv-dal-log.yml` verifica a ogni push che i CSV corrispondano all'xlsx, in sola lettura e senza scrivere sul repository. I CSV non si modificano a mano: ogni modifica si fa sull'xlsx e lo script riallinea.
- Foglio **DENSITA esteso al blocco cc. 16v–36r**, che mancava pur essendo oltre metà del testo trascritto. Il livello A di Claude scende per la prima volta sotto la soglia θ.
### Corretto
- Prompt A, **regola R7** riformulata per chiarezza sulle lettere dubbie (2026-09-22): si segnala con `[?]` dopo il carattere o la parola incerta, o con `[lettera incerta]` quando il segno non è risolvibile, senza risolvere e senza normalizzare. Il prompt resta alla **v1.3**: chiarimento di formulazione, non regola nuova.
- Una cella del blocco cc. 6v–11r (A Claude, da 9 a 10 occorrenze); l'evento **A-073**, che indica due carte appartenenti a blocchi diversi (c. 10r e c. 16v), è ripartito fra cc. 6v–11r e cc. 16v–36r anziché assegnato a uno solo. Le occorrenze attribuite nel foglio (368) coincidono con quelle registrate nel log.
### Nota
- Per il blocco cc. 16v–36r il denominatore in COPERTURA (1950 e 2000 parole) è una **stima** e non un conteggio sul testo TEI: va ricontato.

## [0.4.0-protocolloB] — 2026-08-25
### Aggiunto
- Protocollo B (interpretativa) esteso su **cc. 16v–36r** (cap. II fine, capp. III–IV, inizio cap. V), confronto Claude/Gemini: `tei/A31_interpretativa.xml` ora **frontespizio–c. 36r**, validato. Livello B di Claude validato senza interventi.
- Log a **135 eventi** (Gemini B B-040→B-048), COPERTURA a 22 righe.
### Nota
- Folio 22 (cc. 21v–22r) recuperato e integrato ai due livelli; toponimo sempre «Riglione»; data 1536.
- Gemini B omette cc. 21v–22r (eseguito prima del recupero del folio 22) e aggiunge un meta-testo che scambia la sovrapposizione delle immagini per duplicazione del testimone (B-047, B-048).

## [0.3.0-protocolloA] — 2026-08-25
### Aggiunto
- Protocollo A (diplomatica) esteso su **cc. 16v–36r** (cap. II fine, cap. III, cap. IV, inizio cap. V), confronto Claude/Gemini: `tei/A31_diplomatica.xml` ora **frontespizio–c. 36r**, validato.
- Log a **126 eventi** (Claude A A-073→A-079; Gemini A A-080→A-087), COPERTURA a 20 righe.
### Corretto
- Data di fondazione della Concettione a **c. 10r** e c. 16v: **1536** (era 1556); nota cronologica in apparato (nascita 1534 + «anni 42» ⇒ 1576).
- Toponimo sempre **«Riglione»**; letture validate: Zizo, accette, fortificò, riceuuta, poterono, corono, uolerle, trascoragine (non_delegabile, c. 29v), «braccia ⟨gap⟩ Croce» (c. 26r).
### Nota
- L'interpretativa (B) resta a **c. 16r**: il livello B su cc. 16v–36r sarà prodotto nella sessione Protocollo B.

## [0.2.0-rodaggio] — 2026-08-25
### Aggiunto
- Esperimento di rodaggio su **BCP 2 Qq A 31, frontespizio–c. 16r** chiuso: dataset simmetrico A/B × Gemini/Claude.
- Edizione TEI estesa a **c. 16r** (diplomatica e interpretativa), validata contro `tei_all.rng`.
- Log editoriale a **111 eventi**; COPERTURA con 4 passate (A/B × 2 modelli) per ogni blocco; **11 norme** in NORME_EMERGENTI.
- Densità D calcolata per passata (θ=5/1000): a livello B, Claude D≈0–1 vs Gemini D≈6–14 (divario ~10×); a livello A entrambi sopra θ.
- Densità **normalizzata per occorrenza**: nuovo foglio `DENSITA` e colonna `OCCORRENZE` in `data/LOG_editoriale_AI.xlsx` (conteggio auditabile, non più per riga di log).
- **Prompt A v1.3** in `prompts/prompt-A-diplomatica.md`: blocco «Regole rafforzate (anti-errori ricorrenti)» derivato dalle norme emerse (solo testo; nessuna aggiunta; accenti fedeli; oscillazioni conservate; «/» unico marcatore di riga; parola piena a inizio carta; lettere dubbie da segnalare, non indovinare). Valido per entrambi i modelli.
- **Loop K (probe)**: foglio `LOOP_K` in `data/LOG_editoriale_AI.xlsx`. Claude ×3 su c. 16r, Gemini ×3 su cc. 9v–10r. Risultato: non-determinismo basso in entrambi, ma errori stabili non corretti dalla ripetizione (il consenso a maggioranza può perfino imporli). Il loop K misura la stabilità, non l'accuratezza. Riga Claude cc. 9v–10r (stessa unità di Gemini) da completare.

### Note
- Toponimo del monastero fissato in **«Riglione»** (iniziale R verificata) in tutto il repo; identificazione «San Giovanni dell'Origlione» solo in apparato.
- Loop **K=3** ancora in *backlog* (rodaggio a K=1). Uniformazione del conteggio della densità (per occorrenza) e Prompt A **v1.3** rinviati.

## [0.1.0-setup] — 2026-08
### Aggiunto
- Protocollo v1.0 (congelato): documento in `protocollo/` (`Protocollo_v1.0.md`).
- Prompt A e B v1.2 (pronti-skill) in `prompts/` (licenza MIT).
- Schema del log: `schema/data-dictionary.md`.
- Log editoriale **live** in `data/LOG_editoriale_AI.xlsx` (popolato, aggiornato durante la sperimentazione); template vuoto `data/LOG_editoriale_AI_template.xlsx` e template CSV; esempio sintetico in `examples/`.
- Parametri dichiarati a priori (θ=5/1000, N=10, K=3): `docs/PARAMETRI.md`.
- Edizione TEI in `tei/`: diplomatica (`A31_diplomatica.xml`) e interpretativa con modulo delle norme (`A31_interpretativa.xml`), entrambe frontespizio–c. 16r; validate contro `tei_all.rng`.
- Metadati: `CITATION.cff`, `.zenodo.json` (da completare al deposito).

### Note
- Repository **live/aperto**: il log editoriale viene aggiornato nel repo man mano che la sperimentazione procede. Restano escluse le immagini dei manoscritti (diritti della biblioteca; vedi `.gitignore`).
- Repository pubblico. Deposito Zenodo/DOI (con completamento di ORCID e affiliazione nei metadati) al termine del lavoro.
- Rodaggio A 31, unità 1–5, eseguito a **K=1** (una passata per modello): A e B su Gemini e Claude, validazione umana, log popolato. Loop **K=3** (misura del non-determinismo e forma di consenso) rinviato — *backlog*.
