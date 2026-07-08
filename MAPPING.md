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
| bk01ch01 | What is coding? How programming works, survey of languages | none — **confirmed**: prose/conceptual chapter only. Read the full chapter (not just the opener bullets); it contains no "Listing" captions, no "available with this book's example files" note, and no runnable code — only tiny inline illustrations (a machine-code/assembly snippet, a `printf("Hello, World!")` fragment, and an HTML `<script>` tag example). Nothing to move or create. | **resolved — no companion code** |
| bk01ch02 | Variables, data types, objects, expressions, functions (language-agnostic) | none — **confirmed**: same situation as ch01. Read the full chapter; all code shown is short, generic syntax illustration (variable declarations, arithmetic/comparison/logical operator tables, `if`/`if...else`/`while`/function syntax templates, dot-notation examples, comment syntax). No listing numbers, no filenames, no "example files" reference anywhere. Nothing to move or create. | **resolved — no companion code** |
| bk01ch03 | First looks at Python & JS, peek at other languages (incl. assembly, PHP) | none previously; **new companion files created** in `bk01/ch03/` — the chapter explicitly states "All the code in this chapter is available with this book's example files," and shows a "Hello, World!" example in 13 languages/variants (assembly, Python, JavaScript, C, C++, C#, Go, Java, Kotlin, PHP, Rust, Swift, TypeScript) plus a JS/TS data-type-mixing illustration. Created `bk01ch03_helloworld.{asm,py,js,c,cpp,cs,go,kt,php,rs,swift,ts}`, `HelloWorld.java` (filename forced by Java's public-class-name rule), `bk01ch03_typemixing.js`, and `bk01ch03_typemixing_bug.ts`. Python/JS/C/C++/TypeScript verified by actually running/compiling (all matched claimed output); Java could not be compiled in this sandbox (JRE only, no `javac`) and Go/Kotlin/PHP/Rust/C#/Swift/assembly toolchains were unavailable, so those were verified by manual syntax review only (same limitation noted in Batch1-Errors.md's own review). | **resolved — new listings added** |
| bk01ch04 | Automating tasks, syntax help, testing, AI-assisted learning (Mongoose/MongoDB + phone-validator example per proof errata) | `Book1/` (validatePhoneNumber.js, mongoose/mongodb listings, bk01ch04fg* assets) — moved to `bk01/ch04/` | **resolved — fixed and moved**: <br>• `bk01ch04fg001.html` (Listing 4-1 / Figure 4-1): fixed `<!doctype html>`→`<!DOCTYPE html>`, non-self-closing `<meta>` tags, and **`nav` background-color `#f0f0f0`→`#444`** to match the proof exactly (confirmed via `pdftotext` text-layer extraction of the actual Listing 4-1 code block, not just the rendered page image). Removed stray duplicate `lbk01ch04fg001.html`. <br>• `listing0401.js` renamed to **`listing0402.js`** (the filename the book text itself instructs readers to use — "node listing0402.js") and fixed to include the `mongoose.connect(...)` options object (`useNewUrlParser`/`useUnifiedTopology`) that Listing 4-2 shows but the old repo file was missing entirely. <br>• `package.json`/`package-lock.json` regenerated, pinning `mongoose` to exact version **7.1.0** per the Batch1-Errors.md erratum (page 78) — verified by testing both versions directly: `mongoose@9.7.4` (unpinned "latest") throws `MongoParseError: options usenewurlparser, useunifiedtopology are not supported` on connect and has `findByIdAndRemove === undefined`, while `mongoose@7.1.0` does neither (connects without a parse error and `findByIdAndRemove` is a real function), exactly matching the erratum's findings. Also removed the unused explicit `mongodb` driver dependency (nothing in the code `require`s it directly; only `mongoose` is used, matching the book's own `npm install mongoose` instruction). <br>• Removed the redundant top-level `validatePhoneNumber.js` (byte-for-byte duplicate of `bk01ch04fg005.js`). <br>• `bk01ch04fg007.js` was a non-functional stub (`return;`); replaced with the completed `itemsInCart.reduce(...)` function shown in Figure 4-7, tested and confirmed to compute the correct cart total. <br>• `bk01ch04fg005.js` and `bk01ch04fg006.js` confirmed to already match the proof; moved as-is. <br>• Could not spin up a live MongoDB in this sandbox to run listing0402.js end-to-end (no arm64 `mongod` binary available via `mongodb-memory-server`, no Docker/sudo) — verified the specific documented Mongoose version behavior directly instead (see above) and confirmed the file's syntax and module loading are sound (`node --check`, `require()`). |

**Update:** `Book2/chapter2/8ball.js` was investigated further during the bk02 pass
and, contrary to the note above, it DOES belong to bk02ch02 — it's the JS half of that
chapter's JS-vs-Python indentation comparison (p.118). Moved to `bk02/ch02/`; see the
bk02ch02 row below.

## Part 2 — bk02: Python from Scratch (RESOLVED — all 7 chapters reconciled)

| New chapter | Topic (from proof) | New location | Status |
|---|---|---|---|
| bk02ch01 | Installing Python/VS Code/Copilot/Jupyter, interactive mode, writing/debugging/running | `bk02/ch01/bk02ch01_hello.py`, `bk02/ch01/bk02ch01_notebook.ipynb` | **resolved** — confirmed match to old `Book2/chapter2/hello.py` + `.../Jupyter Notebooks/01 Notebook.ipynb`. Fixed both from `print("Hello, World!")` to `print("Hello World")` to match the exact code/output shown on pp.105-111. |
| bk02ch02 | Python design principles (why indentations count), modules, comments, variables | `bk02/ch02/bk02ch02_8ball.js`, `bk02ch02_8ball.py`, `bk02ch02_variables.py` | **resolved** — old `Book2/chapter2/8ball.js` (previously flagged as an unrelated 2nd-edition JS leftover) is actually THIS chapter's Magic-8-Ball JS-vs-Python indentation illustration (p.118-119); fixed `var`→`let` and removed an extra `else`/trailing `alert()` not in the proof. Added the Python translation and the closing "manipulating variables" example as new files. **Correction:** `Book2/chapter3/chapter3.ipynb` is NOT this chapter's source (see bk02ch03/04/05 below) — the original hint was wrong. |
| bk02ch03 | Built-in number tools, math module, formatting numbers | `bk02/ch03/bk02ch03_notebook.ipynb` | **resolved** — new notebook built from cells 1-29 of old `Book2/chapter3/chapter3.ipynb` (that notebook's content turned out to span bk02ch03/04/05, not bk02ch02). Fixed `sample_amount` (1234.56789→1234.56) and `user2`/`user3` names (Brandon/Cassandra→Babs/Carlos) to match the proof; used the proof's prose version (`username="Alan"`, no punctuation) for the p.138 example rather than Figure 3-5's inconsistent `"Quincy"`/punctuated version (proof has a real prose/figure mismatch here, logged in Batch2-Errors.md — judgment call, noted in the commit). All cells executed and verified; the `fr_FR` locale example is left as printed (Windows-only quirk, not a code bug). |
| bk02ch04 | Strings: concatenation, length, operators, methods | `bk02/ch04/bk02ch04_notebook.ipynb` | **resolved** — new notebook; string-operator and string-methods demos are identical to cells in the old `chapter3.ipynb`. Fixed p.151's curly-quote `print('£')` SyntaxError-as-typeset erratum to use a straight quote. All cells executed and verified. |
| bk02ch05 | Dates and times | `bk02/ch05/bk02ch05_notebook.ipynb` | **resolved** — new notebook covering datetime.date/time/datetime, timedelta, age calculation, naive-vs-aware UTC comparison, and the 5-timezone `gettz()` demo, all verified against the old `chapter3.ipynb`'s datetime cells (byte-identical) plus the proof's own bullet-point formatting examples. `Book2/chapter3/chapter3.ipynb` was deleted (`git rm`) once all of its content had been split across bk02ch03/04/05. Also found and deleted `Book2/chapter5/chapter5.ipynb`, a byte-for-byte duplicate of `chapter3.ipynb` with no unique content (the original "possible match" hint for bk02ch05) — nothing was lost since it was identical to the file already fully migrated. Table 5-1's `%y` "19" example and Table 5-2's "America/Los Angeles"/"America/Honolulu" typos (Batch2-Errors.md) are static reference tables that don't affect any runnable listing, so left as documentation-only issues. |
| bk02ch06 | Storing data (lists/tuples/dicts/sets), conditionals, loops | `bk02/ch06/bk02ch06_listing0601.py` | **resolved** (old ch6 → new ch6, confirmed) — moved the chapter's only numbered listing (Listing 6-1, "A Simple Survey Bot"); content already matched the proof exactly. The rest of the chapter is unnumbered inline REPL syntax illustration with no figures or filenames (same situation as bk01ch01/02) — no other companion files warranted. |
| bk02ch07 | Functions, scope, installing/importing modules, files | `bk02/ch07/bk02ch07_listing0701.py` .. `_listing0713.py`, `my_calculators.py`, `quotations.txt` | **resolved** (old ch7 → new ch7, confirmed) — renamed old `listing07xx.py` files to match the proof's actual Listing 7-N numbers (old numbering had gaps/wasn't 1:1 with the proof). Fixed a corrupted `√` symbol in Listing 7-5's comment and corrected Listing 7-9's limerick text (old file said "Buck" and was missing a line; proof says "Pete" + "His code was quite incomplete"). **Created two new files that didn't exist in the old repo**: `my_calculators.py` (the reusable module described just before Listing 7-6) and `bk02ch07_listing0706.py` (the script that imports it) — filenames for these two match exactly what the code's own `import my_calculators` statement and the proof require (unprefixed, like `HelloWorld.java` in bk01ch03). Verified the full quotation-archive program (Listing 7-13) end-to-end against the existing `quotations.txt` seed data, which turned out to be an exact match for Figure 7-1's terminal screenshot output (even the screenshot's window title, `listing0717.py`, matches the old repo's filename) — strong confirmation this file was already correct. The prose/code mismatch on p.204 (`calculate_price()` vs. the real `calculate_total()`) and the duplicate-phrase comment in `save_quotation()` (p.212) are prose/comment-only issues already in Batch2-Errors.md; no code fix needed since the actual function used throughout is consistently `calculate_total()`. |

## Part 3 — bk03: Python for Data and AI (Data Science) (RESOLVED — all 5 chapters reconciled)

| New chapter | Topic (from proof) | New location | Status |
|---|---|---|---|
| bk03ch01 | What is data science, data science/big data/AI, installing the DS libraries | `bk03/ch01/bk03ch01_notebook.ipynb` | **resolved — new notebook created**. Contrary to the original note in this table (which assumed a prose-only chapter like bk01ch01/02), the proof explicitly names and shows a real companion notebook (`chapter_01_what_is_data_science.ipynb`, "find and run the two code cells") and Figure 1-1 shows the exact source of the version-check cell. Old `Book3/chapter1` was just a 0-byte placeholder *file* (not a directory). Created `bk03/ch01/bk03ch01_notebook.ipynb` with a `%pip install numpy pandas scikit-learn matplotlib` cell (the proof only describes this cell's purpose, doesn't show its source) plus the exact sys/platform/package-version-check cell from Figure 1-1; ran it end-to-end, zero errors. Babbage-quote, Thucydides/Plataea, and Columbia/Journal-of-Data-Science prose errata (Batch2-Errors.md) are narrative-only, left as-is. |
| bk03ch02 | NumPy arrays, pandas DataFrames | `bk03/ch02/bk03ch02_notebook.ipynb` | **resolved** (old ch2 → new ch2, confirmed) — fixed a real duplicated-line bug (`print(df.shape)` was printed twice in a row in "Getting the lay of the land"; proof prints it once). Added two code cells present in the proof's "Aggregating Data" section (simple column stats + groupby aggregations) that were missing from the notebook entirely; verified `groupby('Sex')['Survived'].mean()` output (female 0.742038 / male 0.188908) matches the proof exactly. Removed a stale `make_notebook.py` draft-generator script with no bk01/bk02 equivalent. Ran the full notebook end-to-end (Titanic CSV substituted from a local git-clone mirror only for sandbox testing; notebook's own URL unchanged) — zero errors. |
| bk03ch03 | Scikit-learn built-in datasets, loading data formats, large datasets | `bk03/ch03/bk03ch03_notebook.ipynb` + `bk03/ch03/titanic.csv` | **resolved** (old ch3 → new ch3, confirmed) — reordered the Iris-dataset cells to match the proof's actual sequence (type()/feature_names snippet first, DataFrame-conversion snippet second, both under one heading) and removed a redundant duplicate "Converting to a dataframe" section that repeated the same code a second time. Added a missing `print(housing.DESCR)` cell. Fixed a real spacing bug baked into the notebook's own source (not just the proof's typesetting): `chunk[chunk['value'] >0]` → `chunk[chunk['value'] > 0]`. Added `titanic.csv` (891×12, matching the shape the proof claims) alongside the notebook since `pd.read_csv('titanic.csv')` had no companion data file at all in the old repo. Ran end-to-end (network-gated URLs/APIs substituted with local equivalents only for sandbox verification) — zero errors. The EQ production-query callout (p.245) is an internal note, left as-is. |
| bk03ch04 | Exploratory Data Analysis | `bk03/ch04/bk03ch04_notebook.ipynb` | **resolved** (old ch4 → new ch4, confirmed) — added a missing "Measuring variance and range" section (`penguins.std()` and `penguins.max()-penguins.min()`), verified against the real Palmer Penguins dataset to match the proof's printed values exactly (std: 5.468668/1.969235/14.015765/805.215802; range: 27.5/8.4/59.0/3600.0). Everything else (mean/median, all four chart types, correlation matrix/heatmap, full EDA workflow script) already matched the proof's code and output precisely. Judgment call, no code change: the Figure 4-3 bar-chart color list and Figure 4-6 scatterplot's explicit palette dict assign coral/mediumseagreen to Chinstrap/Gentoo oppositely (Batch3-Errors.md) — both snippets are correct and match their own printed figures, so fixing the "inconsistency" would make the notebook diverge from the book's own printed figures; left as printed. Ran end-to-end headless (penguins.csv substituted from a local git-clone mirror only for sandbox testing) — zero errors. |
| bk03ch05 | Machine learning, Scikit-learn fit/predict/score | `bk03/ch05/bk03ch05_notebook.ipynb` | **resolved** (old ch5 → new ch5, confirmed) — every cell already matched the proof's code exactly; no code changes needed. Specifically investigated the Batch3-Errors.md "duplicated Longitude line" erratum (proof pp.279-280 prints Longitude's coefficient twice, 9 lines for an 8-feature dataset): the actual code is `for feature, coef in zip(X.columns, coefficients): print(...)`, and both `X.columns` and `coefficients` are always exactly 8 elements (one per California Housing feature) — `zip()` over two equal-length 8-element sequences cannot structurally produce a 9th line. Ran the exact cell and got exactly 8 lines, no repeat — confirmed this is a proof/typesetting-only copy-paste error, not a code bug. Ran the full notebook end-to-end (fetch_california_housing() has no network access in this sandbox; substituted an offline dataset re-derived from the same underlying 1990 census source for verification only) and got results strikingly close to the proof's printed numbers: full-data R² 0.606 (exact match), train/test R² 0.610/0.587 vs proof's 0.613/0.576, test MAE 0.540 vs 0.533, CV mean R² 0.599 vs 0.600, and coefficients matching or nearly matching the proof's table (MedInc +0.830, HouseAge +0.119, Population -0.005, AveOccup -0.039 all exact). Zero cell-execution errors. |

Book3 chapter numbering lined up 1:1 with the new bk03 chapters as expected, making
this the most straightforward book to reconcile — mostly small fixes (duplicated
lines, missing cells, cell ordering) rather than wholesale rewrites, plus one
brand-new notebook for bk03ch01 (which turned out to need real companion code after
all, contrary to the original assumption). Old `Book3/` (including the leftover
2nd-edition `Python_For_Data_Science_FD3E_companion_files/` companion download,
which covered a completely different, obsolete chapter breakdown) has been fully
removed from the repo.

## Part 4 — bk04: Coding with AI

| New chapter | Topic (from proof) | Old source | Status |
|---|---|---|---|
| bk04ch01 | AI terms, NLP, transformers/tokens, limitations of AI | none | **resolved — no companion code**: read the full 16-page proof (not just the "IN THIS CHAPTER" bullets). It's entirely conceptual prose — AI/ML/DL/GenAI definitions, neural-network layers, NLP history (ELIZA/ALICE), supervised vs. unsupervised learning, transformers/self-attention/tokens, responsible-AI practices, GPT/generative-model limitations. No "Listing" captions, no filenames, no "available with this book's example files" note, and no code blocks at all (only prose and figures/screenshots, e.g., the OpenAI Tokenizer screenshots in Figures 1-9/1-10). Same situation as bk01ch01/02. Nothing to move or create. (Batch3-Errors.md's GPT-3/GPT-3.5, "non-directional"/"non-directive", and SNN-acronym notes are prose/terminology errata only — no code affected.) |
| bk04ch02 | Prompt engineering, coding with chatbots | none | **resolved — no companion code**: read the full 6-page proof. Covers prompt anatomy (instruction/context/input/output-format), open- vs. closed-ended prompts, zero-shot/few-shot prompting, and custom-instruction blocks — all illustrated with short inline example text, not numbered listings or files. The few-shot example shown (`test_slugify_basic`) is a preview of the real, fully-worked `slugify(text)` example that's actually built out in bk04ch03 (see below); it isn't a distinct companion-file listing in this chapter. No filenames or "example files" references anywhere. Nothing to move or create. (Batch3-Errors.md's unformatted "bread and" example-prompt note is a typesetting issue only.) |
| bk04ch03 | Chatbots → agents, project requirements, coding a prototype with prompts | **correction of prior mapping** — see below | **resolved — new code created; prior "CONFIRMED" mapping to `Book4/chapter01` was WRONG** |
| bk04ch04 | Finding/eliminating bugs, refactoring, AI-assisted testing | none | **resolved — no companion code**: read the full 16-page proof. Covers bug taxonomy, static analysis/linting, AI-assisted debugging, dependency hygiene, code smells and refactoring, code formatters, test plans/AI-generated tests/TDD, code translation between languages, profiling/optimization, and the four types of maintenance (corrective/adaptive/perfective/preventative) plus technical debt. Every example (e.g., a buggy `sum_numbers(a, b)` returning `"a + b"` as a string) is a tiny inline illustration with no listing number, caption, or filename — same pattern as bk01ch01/02 and bk04ch01. Nothing to move or create. (Batch3-Errors.md's garbled "× 2" placeholder-name note on p.330 is a typesetting erratum only, doesn't affect any code.) |

### bk04ch03 correction — the trivia-game/todo-app mapping was wrong

The mapping notes carried into this pass asserted that `Book4/chapter01/` (the
`trivia-game/` folder — `index.html`/`style.css`/`data/trivia.js` — plus `script.js`
with a "Prompt: Write a JavaScript module for a multiple-choice trivia game..."
header comment, and `listing040101.py`, a sqlite3/dataclass todo-list module) was a
**confirmed** match for bk04ch03, based on the "Prompt:" comment style matching this
chapter's theme.

That confirmation does not hold up against the actual proof. bk04ch03's full
12-page text (read page-by-page as rendered images, not just `pdftotext`) never
mentions a trivia game, a quiz app, machine-learning trivia questions, or a
todo/task-list app anywhere — not in the body text, not in a figure, not in a
screenshot. A targeted search of all four bk04 proof texts for `triviaData`,
`TodoItem`, `sqlite3`, `getRandomQuestion`, `showQuestion`, `handleAnswer`,
`dataclass`, and "trivia"/"todo" turned up zero matches. The chapter's one and
only worked example, start to finish (spec -> test -> implementation), is a
**`slugify(text)` function**, which independently corroborates
`Batch3-Errors.md`'s own note: *"the slugify(text) code sample and its test on
page 316 were executed and exactly match the printed output and surrounding
prose"* — no mention of a trivia game or todo app there either, and that review
covered all 12 pages.

**Conclusion:** the trivia-game project and the sqlite3 todo-list module are not
bk04ch03 (or bk04ch01/02/04 — confirmed absent from those too, see rows above).
They've been left in place under `Book4/chapter01/` and moved to the Deferred
section below rather than force-migrated into `bk04/`, since they don't match any
currently-proofed chapter. `bk04/ch03/` was built fresh from the real proof content
instead:

| File | Content |
|---|---|
| `bk04/ch03/myproj/text.py` | The `slugify(text)` implementation from p.316 (`unicodedata.normalize` + `re.sub` pipeline), placed at the exact module path (`myproj.text`) the book's own test imports from. |
| `bk04/ch03/test_slugify.py` | The `test_slugify_basic()` pytest test from p.316 (`from myproj.text import slugify`). |

Verified with `python3 -m pytest`: 1 passed. Also manually sanity-checked the
function against the edge cases the chapter's own prompts call out (unicode
`"Café Münchën"` → `"cafe-munchen"`, empty string → `""`, punctuation-only
`"!!!???"` → `""`) — all behave sensibly, though only the basic test is actually
printed in the proof, so only that one was added to the repo (no fabricated tests
added beyond what's shown). The chapter's various "copy this into your chatbot/
agent" prompt examples (the agent-task prompt, the spec-generation prompt, the
generated spec itself, and the code-generation prompt) are illustrative prose
elements without listing captions or filenames, consistent with how bk04ch02's
prompt examples were treated — not captured as separate companion files.

## Deferred (no proofs yet)

- `Book5/` (HTML/CSS — index.html, grid-example, figures) → likely bk05 or bk06
- `Book6/` (JavaScript listings, ball-game, weather API) → likely bk06 or bk07
- `Book7/` (React `my-react-app`, Vue `vue-project`) → likely bk07
- `Book8/` — empty, unclear purpose
- `Book4/chapter01/` (`trivia-game/` — `index.html`/`style.css`/`data/trivia.js` — plus
  `script.js` and `listing040101.py`, a sqlite3/dataclass todo-list module) — investigated
  thoroughly against all four bk04 proofs (see the bk04ch03 correction note above) and
  confirmed to match none of them. Left in place, untouched. May belong to a later,
  not-yet-proofed minibook (a JS-focused chapter in bk05/06/07) or may be obsolete
  2nd-edition-era scaffolding; revisit once those proofs arrive.
- `Book2/figures/fg020102.png`, `Book2/figures/fg020103.png` — two leftover 2nd-edition
  figure images under the old `Book2/` root (not `chapter2/`); no corresponding code to
  reconcile, left in place. `Book2/chapter2/`, `chapter5/`, `chapter6/`, and `chapter7/`
  are now empty of files (everything moved into `bk02/`) but the directories themselves
  may still exist as empty shells — harmless, git doesn't track them.

## Status: bk01–bk04 fully reconciled — this minibook is done

With bk04ch01–ch04 resolved above, **all four proofed minibooks (bk01, bk02, bk03,
bk04 — 20 chapters total) are now fully reconciled** against their 3rd-edition page
proofs and committed on `3e-code-update`. `Book1`–`Book3` (the old 2nd-edition-derived
folders for those minibooks) have been fully migrated and removed; `Book4` retains
only the still-unmatched `chapter01/` content noted in the Deferred section above,
left in place on purpose pending future proofs.

`bk05`–`bk07` (and whatever `Book8` turns out to be) remain **pending** — no page
proofs have been received from the layout team for those minibooks yet. `Book5`,
`Book6`, and `Book7` are believed to map to HTML/CSS, JavaScript, and React/Vue
content respectively (see the Deferred section above for specifics), but nothing in
those folders should be touched until their proofs arrive: old chapter numbers have
already been shown to be unreliable indicators of new-edition placement (bk02ch02,
bk04ch03) and content has turned out to be misfiled or absent more than once in this
project, so each remaining minibook needs the same full read-the-proof-first
treatment applied here before anything gets renamed, fixed, or moved.
