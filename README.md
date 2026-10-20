# Word Hunt Solver

Finds every word on a 4x4 Word Hunt (GamePigeon) board, sorted from longest to shortest, with the score each one is worth.


| Board | Solver output |
| --- | --- |
| <img width="420" alt="Playing sheepishly in Word Hunt" src="https://github.com/user-attachments/assets/b5c65e5d-24fd-4608-8862-1a22e5118e9f" /> | <img width="239" alt="Solver output" src="https://github.com/user-attachments/assets/158eda6b-617f-4eea-b70f-7f530f2347ea" /> |

*Playing "sheepishly" (+3000), the longest word found by the solver*

## How it works

The word list is loaded into a **trie** (prefix tree). The solver then runs a **depth-first search** from every tile, moving to any of the 8 neighboring tiles without reusing one. As soon as the letters so far aren't the start of any real word, that path is dropped. This pruning is what makes it fast enough to search every path on the board instantly.

## Requirements

- Python 3.6+
- No packages to install

## Usage

```bash
git clone https://github.com/BaomoL/word-hunt-solver.git
cd word-hunt-solver
python3 solver.py
```

On Windows, use python solver.py.

Type the board one row at a time, four letters per row:

```
Row 1: ihyn
Row 2: vlsi
Row 3: rnpt
Row 4: shee
```

It prints the total possible score, then every word grouped by length.

## Word lists

By default the solver uses `wordlists/enable1.txt`, the public-domain ENABLE word list.

To use your own word list instead, save it as `wordlists/dictionary.txt`. It should be a plain text file with one word per line (upper or lower case both work). If that file exists, the solver uses it automatically. For results that match Word Hunt most closely, use a Scrabble tournament list such as Collins Scrabble Words, if you have a copy.

## Scoring

| Word length | Points |
| --- | --- |
| 3 | 100 |
| 4 | 400 |
| 5 | 800 |
| 6 | 1400 |
| 7 | 1800 |
| 8 | 2200 |
| 9+ | 2600, plus 400 for each extra letter |


