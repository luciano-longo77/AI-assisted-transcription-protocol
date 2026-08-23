# AI-assisted-transcription-protocol
## Protocollo di trascrizione interpretativa AI-assistita
### AI-assisted interpretive transcription protocol

---

## IT — Che cos'è

Modello editoriale operativo per rendere **scalabile la trascrizione interpretativa** di manoscritti omogenei, mantenendo il controllo umano sulle decisioni normative. Un LLM opera come **acceleratore sotto supervisione**, non come decisore. Il protocollo distingue trascrizione **diplomatica (A)** e **interpretativa (B)**, registra ogni intervento in un **log** e ne astrae le **norme emergenti**.

Perimetro sperimentale: campioni di **BCP 2 Qq A 31** e **BCP 3 Qq B 49** (Biblioteca Comunale di Palermo).

## EN — What it is

An operational editorial model to make **interpretive transcription scalable** for homogeneous manuscript corpora, keeping human authority over normative decisions. An LLM acts as a **supervised accelerator**, not a decision-maker. The protocol separates **diplomatic (A)** and **interpretive (B)** transcription, logs every human intervention, and abstracts the **emerging norms**.

## Struttura / Layout

```
.
├── protocollo/      documento del protocollo (v1.0 congelato) + specifica
├── prompts/         Prompt A e B v1.2 (pronti-skill) — licenza MIT
├── schema/          data dictionary del log (campi + vocabolari controllati)
├── data/            template del log (xlsx + csv) — SENZA dati sperimentali
├── docs/            cronoprogramma, piano attività, setup, decisioni
├── examples/        esempi sintetici (non dati reali)
├── CITATION.cff     metadati di citazione (da completare)
└── .zenodo.json     metadati di deposito (solo alla pubblicazione)
```

## Parametri dichiarati (a priori)

θ = 5 interventi / 1000 parole · N = 10 carte consecutive · K = 3 ripetizioni (loop anti-RNG) · modelli: Gemini + Claude · protocollo **v1.0 (congelato)**.

## Licenza / License

**Doppia licenza**: documenti, schema e paper sotto **CC-BY-4.0**; i prompt in `prompts/` sotto **MIT** (vedi `prompts/LICENSE`). Dettagli in `LICENSE`.

## Stato / Status

Fase di **setup** completata (protocollo, prompt, log, parametri). Prossimo: Fase 1 (A 31) — vedi `docs/CRONOPROGRAMMA.md`.
