# AI-assisted-transcription-protocol
## Protocollo di trascrizione interpretativa AI-assistita
### AI-assisted interpretive transcription protocol

[![protocollo: v1.2](https://img.shields.io/badge/protocollo-v1.2-1f4e79)](protocollo/Protocollo_v1.2.md) [![Nota al testo: v1.0](https://img.shields.io/badge/Nota%20al%20testo-v1.0-2e6da4)](docs/Nota_al_testo.md) [![Prompt A: v1.4](https://img.shields.io/badge/Prompt%20A-v1.4-5b9bd5)](prompts/prompt-A-diplomatica.md) [![Prompt B: v2.1](https://img.shields.io/badge/Prompt%20B-v2.1-5b9bd5)](prompts/prompt-B-interpretativa.md)

---

## Indice

- [IT - Che cos'è](#it---che-cosè)
- [EN - What it is](#en---what-it-is)
- [Struttura / Layout](#struttura--layout)
- [La norma editoriale](#la-norma-editoriale)
- [Parametri dichiarati (a priori)](#parametri-dichiarati-a-priori)
- [Dati](#dati)
- [Licenza / License](#licenza--license)

---

## IT - Che cos'è

Modello editoriale operativo per rendere **scalabile la trascrizione interpretativa** di manoscritti omogenei, mantenendo il controllo umano sulle decisioni normative. Un LLM opera come **acceleratore sotto supervisione**, non come decisore. Il protocollo distingue trascrizione **diplomatica (A)** e **interpretativa (B)**, registra ogni intervento in un **log** e ne astrae le **norme emergenti**.

Perimetro sperimentale: **BCP 2 Qq A 31** (Biblioteca Comunale di Palermo), caso di applicazione principale e sede della formalizzazione delle norme; **BCP 3 Qq B 49** come banco di trasferibilità, in fase successiva.

## EN - What it is

An operational editorial model to make **interpretive transcription scalable** for homogeneous manuscript corpora, keeping human authority over normative decisions. An LLM acts as a **supervised accelerator**, not a decision-maker. The protocol separates **diplomatic (A)** and **interpretive (B)** transcription, logs every human intervention, and abstracts the **emerging norms**.

## Struttura / Layout

```
.
├── protocollo/      documento del protocollo (v1.2) + specifica
├── prompts/         Prompt A v1.4 e Prompt B v2.1 (pronti-skill) — licenza MIT
├── docs/            norma editoriale (Nota al testo), suo fondamento comparativo,
│                    parametri dichiarati a priori
├── schema/          data dictionary del log (campi + vocabolari controllati)
├── data/            strumento vuoto: template del log (xlsx) + vocabolari e parametri (csv)
├── examples/        esempi sintetici (non dati reali)
├── Archive/         prima applicazione su A 31: log popolato, trascrizioni TEI,
│                    viste CSV, automazione, metadati di deposito
├── CHANGELOG.md     storia delle versioni
└── LICENSE          licenza dei documenti e dello schema
```

Il repository distingue il **protocollo** dalla sua **prima applicazione**. Fuori da `Archive/` stanno metodo, norma, strumenti e vocabolari: è l'insieme che si può trasferire a un altro testimone e a un altro ricercatore. Dentro `Archive/` stanno i dati prodotti su A 31 fra agosto e settembre 2026 — 135 eventi di log, 368 occorrenze, 72 carte in TEI ai due livelli — conservati e citabili, ma non necessari a chi voglia riapplicare il metodo.

## La norma editoriale

Il regime del livello B è fissato in [`docs/Nota_al_testo.md`](docs/Nota_al_testo.md): criterio-limite, nove classi di normalizzazione con il loro ordine di applicazione, forme che si conservano, casi riservati all'editore. I prompt ne sono la forma eseguibile; in caso di divergenza prevale la norma. Il fondamento comparativo dei criteri, rispetto ad altre edizioni digitali ad accesso aperto, è in [`docs/Ricognizione_normalizzazioni.md`](docs/Ricognizione_normalizzazioni.md).

## Parametri dichiarati (a priori)

θ = 5 interventi / 1000 parole · N = 10 facciate consecutive · K = 3 ripetizioni (loop anti-RNG) · modelli: Gemini + Claude · protocollo **v1.2**.

Unità di lavorazione: l'immagine, cioè la coppia di facciate affacciate. Unità di misura: la facciata. Dettagli in [`docs/PARAMETRI.md`](docs/PARAMETRI.md).

## Dati

Il log editoriale della prima applicazione è in `Archive/`, con le sue viste CSV. In `data/` resta lo **strumento vuoto** — template del log con i vocabolari e i menu già collegati — pronto per una nuova applicazione. Le immagini dei manoscritti non sono versionate (diritti della biblioteca; vedi `.gitignore`).

## Licenza / License

**Doppia licenza**: documenti, schema e paper sotto **CC-BY-4.0**; i prompt in `prompts/` sotto **MIT** (vedi `prompts/LICENSE`). Dettagli in `LICENSE`.
