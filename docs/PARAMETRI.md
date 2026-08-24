# Parametri dichiarati a priori

**Protocollo:** v1.0 (congelato) · **Parametri fissati il:** 2026-08-23 · **Stato:** attivo

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

calcolata sul totale, per classe `TIPO_ERRORE` e per modello. Il denominatore (parole) è raccolto nel foglio `COPERTURA` del log.

Una classe è **stabilizzata** quando **D ≤ θ per N carte consecutive**.

## Ruolo del loop K

In interfaccia chat la temperatura di decodifica spesso non è impostabile. Il controllo della variabilità (non-determinismo del modello) non è quindi affidato alla temperatura ma al **loop K = 3**: tre passate della stessa unità per modello, dalle quali si ricava la forma di consenso. K non elimina la variabilità: la rende **misurabile**.

## Modelli confrontati

Gemini e Claude, ai livelli A (diplomatico) e B (interpretativo), con gli stessi prompt incapsulati come skill/Gem versionate (Prompt A v1.2, Prompt B v1.2), identici a ogni esecuzione.

## Dove sono registrati anche

- Foglio `PARAMETRI` in `data/LOG_editoriale_AI_template.xlsx`
- `schema/data-dictionary.md` (sezione PARAMETRI e Metrica)
- `.zenodo.json` (metadati di deposito)

## Regola di modifica

I parametri sono **congelati**. Qualsiasi cambiamento di θ, N o K non è una modifica silenziosa: si apre una nuova versione del protocollo (es. v1.1), si annota nel CHANGELOG la motivazione e la data, e si dichiara da quale unità la nuova soglia si applica.

## Stato operativo — rodaggio u.1–5 (2026-08-24)

Il rodaggio di **BCP 2 Qq A 31**, unità 1–5 (carte 1–5, oltre a frontespizio e c. 6r), è stato eseguito con **una passata per modello (K=1)**: Prompt A e Prompt B su Gemini e Claude, con validazione umana ai due livelli e log popolato (49 eventi, 9 norme emergenti). I denominatori sono registrati nel foglio COPERTURA.

Il **loop K=3** — ripetizioni per modello per misurare il non-determinismo e assumere la forma di consenso — è **rinviato (backlog)** e sarà eseguito in una fase successiva. Poiché **K=3 resta il valore dichiarato** del protocollo, questo è uno **scostamento operativo tracciato**, non una modifica del parametro.
