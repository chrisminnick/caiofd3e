# Old Repo → 3rd Edition Chapter Mapping

Working notes for reconciling the old (2nd-edition-derived) `Book1`–`Book8` folders
against the new 3rd-edition structure (`bk01`–`bk07`, per the page proofs).

**Important:** Old Book/chapter numbers are NOT reliable indicators of where content
belongs in the new edition. Confirmed mismatch: `Book4/chapter01` (trivia-game +
"Prompt:"-commented script.js) actually belongs in **bk04ch03**, not bk04ch01.
Mapping below is based on matching actual code/content against the page proofs.

Proofs received so far (batches 1–3): bk01–bk04 only. bk05–bk07 (likely HTML/CSS,
JavaScript, React/Vue based on old Book5/6/7 content) are pending from the layout team.

## Part 1 — bk01: Getting Started with Coding

| New chapter | Topic (from proof) | Old source | Status |
|---|---|---|---|
| bk01ch01 | What is coding? How programming works, survey of languages | none identified yet — likely new/rewritten prose, minimal code | to confirm |
| bk01ch02 | Variables, data types, objects, expressions, functions (language-agnostic) | none identified yet | to confirm |
| bk01ch03 | First looks at Python & JS, peek at other languages (incl. assembly, PHP) | none identified yet | to confirm |
| bk01ch04 | Automating tasks, syntax help, testing, AI-assisted learning (Mongoose/MongoDB + phone-validator example per proof errata) | `Book1/` (validatePhoneNumber.js, mongoose/mongodb listings, bk01ch04fg* assets) | **confirmed**, already partially renamed correctly |

`Book2/chapter2/8ball.js` (vanilla JS magic-8-ball) does not fit any bk01–04 chapter
content seen so far — likely a 2nd-edition leftover (old Book2 may have been a JS book).
Flagged for removal or relocation once bk05–07 proofs arrive.

## Part 2 — bk02: Python from Scratch

| New chapter | Topic (from proof) | Old source | Status |
|---|---|---|---|
| bk02ch01 | Installing Python/VS Code/Copilot/Jupyter, interactive mode, writing/debugging/running | `Book2/chapter2/hello.py` | likely match |
| bk02ch02 | Python design principles, modules | `Book2/chapter3/chapter3.ipynb`? | to confirm |
| bk02ch03 | Built-in number tools, math module | unidentified | to confirm |
| bk02ch04 | Strings: joining, length, operators, methods | unidentified | to confirm |
| bk02ch05 | Dates and times | `Book2/chapter5/chapter5.ipynb`? | to confirm |
| bk02ch06 | Storing data, conditionals, loops | `Book2/chapter6/listing0601.py` | likely match (old ch6 → new ch6) |
| bk02ch07 | Functions, scope, installing/importing modules | `Book2/chapter7/listing07xx.py`, quotations.txt | likely match (old ch7 → new ch7) |

## Part 3 — bk03: Python for Data and AI (Data Science)

| New chapter | Topic (from proof) | Old source | Status |
|---|---|---|---|
| bk03ch01 | What is data science, data science/big data/AI | `Book3/chapter1` (currently empty) | to confirm — likely all-new prose |
| bk03ch02 | NumPy arrays, pandas DataFrames | `Book3/chapter2/chapter_02_working_with_data.ipynb` | **confirmed** (old ch2 → new ch2) |
| bk03ch03 | Scikit-learn built-in datasets, loading data formats, large datasets | `Book3/chapter3/chapter_03_getting_your_data.ipynb` | **confirmed** (old ch3 → new ch3) |
| bk03ch04 | Exploratory Data Analysis | `Book3/chapter4/chapter_04_exploring_and_visualizing.ipynb` | **confirmed** (old ch4 → new ch4) |
| bk03ch05 | Machine learning, Scikit-learn fit/predict/score | `Book3/chapter5/chapter_05_your_first_machine_learning_model.ipynb` | **confirmed** (old ch5 → new ch5) |

Book3 chapter numbering already lines up 1:1 with the new bk03 chapters — simplest
book to reconcile.

## Part 4 — bk04: Coding with AI

| New chapter | Topic (from proof) | Old source | Status |
|---|---|---|---|
| bk04ch01 | AI terms, NLP, transformers/tokens, limitations of AI | unidentified | to confirm — likely all-new prose |
| bk04ch02 | Prompt engineering, coding with chatbots | unidentified | to confirm |
| bk04ch03 | Chatbots → agents, project requirements, coding a prototype with prompts | `Book4/chapter01/` (trivia-game, script.js, listing040101.py todo app) | **confirmed** — script.js literally contains a "Prompt: ..." comment matching this chapter's theme |
| bk04ch04 | Finding/eliminating bugs, refactoring, AI-assisted testing | unidentified | to confirm |

## Deferred (no proofs yet)

- `Book5/` (HTML/CSS — index.html, grid-example, figures) → likely bk05 or bk06
- `Book6/` (JavaScript listings, ball-game, weather API) → likely bk06 or bk07
- `Book7/` (React `my-react-app`, Vue `vue-project`) → likely bk07
- `Book8/` — empty, unclear purpose

## Next steps
1. For each "to confirm" / "unidentified" row above, read the full chapter proof text
   (not just the chapter-opener bullets) to find listing captions/numbers and match
   them against old repo files or determine the content is new and needs a fresh listing.
2. Rename matched files/folders to `bk0Xch0Y...` convention (mirroring what's already
   done in Book1).
3. Fix code to match what's printed in the proofs; flag anything that can't be resolved.
4. Commit per chapter on the `3e-code-update` branch.
