# Verification

The complete analytical arguments live in [science/](../science/README.md). The executable checks provide independent finite calculations, source navigation checks and a reproducible inspection of the rendered mathematics.

## Finite scientific checks

From the repository root, with Python 3.12:

```bash
python -m pip install -r requirements.txt
python code/verify.py
```

A successful run exits with status zero and prints `"status": "pass"`, the largest observed numerical discrepancies, fidelity status and the number of resolved relative file links. It writes [results/verification.json](../results/verification.json), including the observation time, runtime versions, seeds and input SHA256 hashes. To keep the saved report unchanged during an independent run, choose another output path:

```bash
python code/verify.py --output /tmp/noisy-local-verification.json
```

The [implementation guide](../code/README.md) describes the independent constructions, system sizes and tolerances. The checks cover exact Haar moment formulas, physical adaptive instruments, interleaved transcript hybrids, and the unbiased noise-inverted fidelity score. They include conditional zero branches and a product target with zero ideal verification gap. Numerical agreement does not establish the asymptotic theorems or the literature comparison.

## Rendered mathematics

The hosted collector reads a full commit SHA, inventories every tracked Markdown page, and visits the actual commit-pinned GitHub pages at widths 1440 and 760. Each source expression is compiled locally for comparison with the host's MathML. It checks expression counts, structure, visible relations, source hashes and display geometry; [the text contract](math-contract.json) also checks selected headline expressions.

The two scripts in [hosted/](hosted/) are an unchanged snapshot of the collector and its structural checker. Install the pinned browser dependencies in a temporary directory outside this checkout:

```bash
npm install --prefix /tmp/noisy-local-render-deps playwright@1.56.1 mathjax-full@3.2.1
/tmp/noisy-local-render-deps/node_modules/.bin/playwright install chromium
```

With `REVISION` set to the full commit SHA to inspect, run from the repository root:

```bash
NODE_PATH=/tmp/noisy-local-render-deps/node_modules node verification/hosted/capture_hosted_math.cjs \
  --root . \
  --repository GoGoKo699/Noisy-Local-Certification \
  --revision "$REVISION" \
  --output /tmp/noisy-local-hosted-review \
  --contract verification/math-contract.json
```

Use a new empty output directory for each attempt. Exit zero means the automatic source-to-host comparisons passed for the recorded revision and page scope. Preserve failed attempts when diagnosing a defect. A blocked network connection, certificate error or unavailable browser cannot produce a hosted pass. Keep ordinary TLS verification enabled.

The output contains `hosted-report.json`, source and capture inventories, structural results, HTML and wide/narrow screenshots. Review actual screenshots for legibility, tables, navigation and scientific meaning, including every flagged or repaired display. Automated MathML comparison cannot replace that review, and local TeX compilation alone is not evidence of GitHub rendering.

## Continuous verification

The [verification workflow](../.github/workflows/verify.yml) runs finite scientific checks and the same hosted collector against the exact source commit. It uses read-only repository permissions, a fresh browser and pinned action revisions. Its artifacts retain the actual reports and screenshots for 14 days. Download needed evidence before that retention window expires; artifacts are observations of a particular revision, not permanent verification of future revisions.

The scientific report, hosted result, visual review and inspected source must refer to the same content tree. A later edit to a claim or its display requires the affected checks to be repeated. Branch-protection settings and a workflow badge do not establish the scientific validity of a theorem.
