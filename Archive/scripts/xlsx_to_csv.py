#!/usr/bin/env python3
"""Rigenera i CSV leggibili a partire dal log editoriale in formato xlsx.

Il file data/LOG_editoriale_AI.xlsx resta l'originale su cui si lavora: conserva i
menu a tendina che vincolano i campi a vocabolario chiuso. I CSV in data/csv/ sono
una vista, utile per due ragioni: GitHub li mostra come tabella direttamente nella
pagina, e il confronto fra due versioni diventa leggibile riga per riga, cosa
impossibile con un file binario.

I CSV non si modificano a mano: ogni modifica si fa sull'xlsx, e questo script li
riallinea.

Uso:
    python3 scripts/xlsx_to_csv.py              # riscrive i CSV dall'xlsx
    python3 scripts/xlsx_to_csv.py --verifica   # non scrive: segnala se sono disallineati
"""
import argparse
import csv
import datetime as dt
import io
import sys
from pathlib import Path

import openpyxl

RADICE = Path(__file__).resolve().parent.parent
SORGENTE = RADICE / "data" / "LOG_editoriale_AI.xlsx"
DESTINAZIONE = RADICE / "data" / "csv"


def valore(cella):
    """Rende una cella in testo, in modo stabile fra un'esecuzione e l'altra."""
    if cella is None:
        return ""
    if isinstance(cella, dt.datetime):
        # le date senza orario si scrivono come date, non come "… 00:00:00"
        if cella.time() == dt.time(0, 0):
            return cella.date().isoformat()
        return cella.isoformat(sep=" ")
    if isinstance(cella, dt.date):
        return cella.isoformat()
    if isinstance(cella, float) and cella.is_integer():
        return str(int(cella))
    return str(cella)


def righe_utili(foglio):
    """Le righe non vuote del foglio, senza le colonne vuote in coda."""
    righe = [r for r in foglio.iter_rows(values_only=True)
             if any(c is not None and str(c).strip() for c in r)]
    if not righe:
        return []
    larghezza = max(
        len(r) - next((i for i, c in enumerate(reversed(r)) if c is not None), len(r))
        for r in righe
    )
    return [[valore(c) for c in r[:larghezza]] for r in righe]


def rendi_csv(righe):
    buffer = io.StringIO(newline="")
    csv.writer(buffer, quoting=csv.QUOTE_MINIMAL, lineterminator="\n").writerows(righe)
    return buffer.getvalue()


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verifica", action="store_true",
                    help="non scrive nulla: esce con errore se i CSV sono disallineati")
    args = ap.parse_args()

    if not SORGENTE.exists():
        sys.exit(f"manca il file sorgente: {SORGENTE.relative_to(RADICE)}")

    libro = openpyxl.load_workbook(SORGENTE, data_only=True)
    if not args.verifica:
        DESTINAZIONE.mkdir(parents=True, exist_ok=True)

    attesi, disallineati = set(), []
    for foglio in libro.worksheets:
        righe = righe_utili(foglio)
        if not righe:
            continue
        percorso = DESTINAZIONE / f"{foglio.title}.csv"
        attesi.add(percorso.name)
        nuovo = rendi_csv(righe)
        vecchio = percorso.read_text(encoding="utf-8-sig") if percorso.exists() else None
        if nuovo == vecchio:
            print(f"  allineato       data/csv/{percorso.name}")
            continue
        disallineati.append(percorso.name)
        if args.verifica:
            motivo = "manca" if vecchio is None else "non corrisponde al log"
            print(f"  DA RIALLINEARE  data/csv/{percorso.name}  ({motivo})")
        else:
            percorso.write_text(nuovo, encoding="utf-8-sig")
            print(f"  scritto         data/csv/{percorso.name}  "
                  f"({len(righe)} righe × {len(righe[0])} colonne)")

    # un foglio rinominato o rimosso lascerebbe un csv orfano
    if DESTINAZIONE.exists():
        for orfano in sorted(DESTINAZIONE.glob("*.csv")):
            if orfano.name not in attesi:
                disallineati.append(orfano.name)
                if args.verifica:
                    print(f"  DA RIMUOVERE    data/csv/{orfano.name} "
                          f"(non corrisponde ad alcun foglio del log)")
                else:
                    orfano.unlink()
                    print(f"  rimosso         data/csv/{orfano.name}")

    if not disallineati:
        print("\nI CSV corrispondono al log.")
        return

    if args.verifica:
        print(f"\n{len(disallineati)} file non corrispondono più al log editoriale.")
        print("\nPer riallinearli, due strade:")
        print("  · da GitHub, senza installare nulla: scheda Actions -> «CSV dal log»")
        print("    -> «Run workflow»; i CSV rigenerati si scaricano dagli allegati")
        print("    dell'esecuzione e si caricano in data/csv/;")
        print("  · da un computer con Python: python3 scripts/xlsx_to_csv.py")
        sys.exit(1)

    print(f"\n{len(disallineati)} file aggiornati.")


if __name__ == "__main__":
    main()
