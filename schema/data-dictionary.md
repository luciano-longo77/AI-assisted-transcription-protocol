# Data dictionary — LOG_editoriale_AI

Il log registra **ogni intervento** dell'editore sull'output di un modello; il foglio COPERTURA fornisce i **denominatori**; PARAMETRI dichiara le soglie; NORME_EMERGENTI astrae le regole; LISTE contiene i vocabolari controllati.

---

## Indice

- [Foglio `LOG_ERRORI` (una riga per evento, 12 campi)](#foglio-log_errori-una-riga-per-evento-12-campi)
- [Foglio `COPERTURA` (denominatore)](#foglio-copertura-denominatore)
- [Foglio `PARAMETRI` (dichiarati a priori)](#foglio-parametri-dichiarati-a-priori)
- [Foglio `NORME_EMERGENTI`](#foglio-norme_emergenti)
- [Vocabolari controllati (`LISTE`)](#vocabolari-controllati-liste)
- [Metrica](#metrica)
- [Nota sul nome del campo `TIPO_ERRORE`](#nota-sul-nome-del-campo-tipo_errore)

---

## Foglio `LOG_ERRORI` (una riga per evento, 12 campi)

| # | Campo | Descrizione | Vincolo |
|---|-------|-------------|---------|
| 1 | ID_ERRORE | Identificatore univoco (A-001…, B-001…) per livello | manuale, progressivo |
| 2 | LIVELLO | Fase: A (diplomatica) / B (interpretativa) | menu: A, B |
| 3 | TESTIMONE | Manoscritto (segnatura) | testo stabile |
| 4 | SEGMENTO | Localizzazione (carta, riga) | testo |
| 5 | TIPO_ERRORE | Natura del problema | menu (vocabolario) |
| 6 | FORMA_AI | Output grezzo del modello | testo |
| 7 | CORREZIONE_UMANA | Forma accolta dall'editore | testo |
| 8 | AZIONE_UMANA | Tipo di intervento | menu |
| 9 | DECISIONE_EDITORIALE | Norma generale che emerge | testo |
| 10 | ESITO | stabilizzato / ricorrente / non_delegabile | menu |
| 11 | MODELLO | Modello che ha prodotto FORMA_AI | menu: Gemini, Claude |
| 12 | NOTE | Annotazioni libere | testo |

## Foglio `COPERTURA` (denominatore)
TESTIMONE · UNITA · CARTE · PAROLE · DATA · MODELLO · NOTE — una riga per ogni unità processata.

## Foglio `PARAMETRI` (dichiarati a priori)
- **θ (soglia)** = 5 interventi / 1000 parole
- **N (finestra)** = 10 facciate consecutive
- **Unità** = immagine (coppia di facciate affacciate); misura per facciata
- **K (loop)** = 3 ripetizioni per modello
- Modelli = Gemini; Claude · Skill = Prompt A v1.4; Prompt B v2.1 · Protocollo = v1.2 · Decodifica = deterministica ove possibile

## Foglio `NORME_EMERGENTI`
AREA · NORMA (impersonale, generale) · DERIVATA_DA_ERRORI (ID esistenti nel log) · STATO.

## Vocabolari controllati (`LISTE`)

**LIVELLO:** A, B

**TIPO_ERRORE:**
abbreviazione_non_riconosciuta, abbreviazione_espansione_errata, grafia_errata, confusione_grafica, segmentazione_riga_errata, omissione_testo, duplicazione_testo, carattere_non_riconosciuto, illeggibile_non_segnalato, normalizzazione_mancata, normalizzazione_indebita, unione_separazione_errata, accentazione_errata, maiuscola_minuscola_errata, punteggiatura_errata, scioglimento_abbreviazione_errato, scioglimento_abbreviazione_mancato, forma_lessicale_incoerente, ambiguità_non_delegabile, stratificazione_genetica, caso_limite_testuale, latino_normalizzato_indebitamente, lacuna_integrata_indebitamente

**AZIONE_UMANA:** scioglimento, normalizzazione, conservazione, correzione, blocco_intervento, segnalazione

**ESITO:** stabilizzato, ricorrente, non_delegabile

**MODELLO:** Gemini, Claude

## Metrica
Densità di intervento **D = interventi ÷ (parole/1000)**, calcolata sul totale, per classe TIPO_ERRORE e per modello. Una classe è **stabilizzata** quando D ≤ θ per N facciate consecutive senza intervento sistematico; altrimenti è ricorrente. È **sistematico** l'intervento che ricorre nella finestra su più unità con la stessa causa e la stessa correzione; un'occorrenza isolata non lo è. Le due condizioni sono congiuntive: finché un intervento sistematico persiste, la classe resta ricorrente anche con D sotto soglia.

## Nota sul nome del campo `TIPO_ERRORE`
`TIPO_ERRORE` è un nome **convenzionale**, conservato per continuità dello strumento e dei dati già registrati. Al livello A designa effettivamente un errore di lettura, verificabile sull'immagine. Al livello B designa invece uno **scostamento dall'esito atteso secondo la norma editoriale vigente**, non un errore filologico oggettivo: la garanzia V5 del protocollo stabilisce che al livello interpretativo si registra un intervento dell'editore, non il fallimento di una verità. Il campo dice dunque in che modo l'output del modello ha mancato l'esito atteso, e la sua classificazione è subordinata alla norma dichiarata per il testimone.
