# Changelog

## [0.1.0-setup] — 2026-08
### Aggiunto
- Protocollo v1.0 (congelato): documento in `protocollo/` (`Protocollo_v1.0.md`).
- Prompt A e B v1.2 (pronti-skill) in `prompts/` (licenza MIT).
- Schema del log: `schema/data-dictionary.md`.
- Log editoriale **live** in `data/LOG_editoriale_AI.xlsx` (popolato, aggiornato durante la sperimentazione); template vuoto `data/LOG_editoriale_AI_template.xlsx` e template CSV; esempio sintetico in `examples/`.
- Parametri dichiarati a priori (θ=5/1000, N=10, K=3): `docs/PARAMETRI.md`.
- Edizione TEI (frontespizio–c. 6r) in `tei/`: diplomatica (`A31_diplomatica.xml`) e interpretativa con modulo delle norme (`A31_interpretativa.xml`); validata contro `tei_all.rng`.
- Metadati: `CITATION.cff`, `.zenodo.json` (da completare al deposito).

### Note
- Repository **live/aperto**: il log editoriale viene aggiornato nel repo man mano che la sperimentazione procede. Restano escluse le immagini dei manoscritti (diritti della biblioteca; vedi `.gitignore`).
- Repository pubblico. Deposito Zenodo/DOI (con completamento di ORCID e affiliazione nei metadati) al termine del lavoro.
- Rodaggio A 31, unità 1–5, eseguito a **K=1** (una passata per modello): A e B su Gemini e Claude, validazione umana, log popolato. Loop **K=3** (misura del non-determinismo e forma di consenso) rinviato — *backlog*.
