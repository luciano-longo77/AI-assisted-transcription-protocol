# Changelog

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
