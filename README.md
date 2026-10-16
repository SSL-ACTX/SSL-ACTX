<!-- @readme:header:start -->
```text
┌──  S E U R I I N  ·  v0.0.1-alpha.1  ────────────────────────
│    Compiler Architect & Systems Researcher · Formal Methods · Runtimes
└──────────────────────────────────────────────────────
```
<!-- @readme:header:end -->

<!-- @readme:meta:start -->
`LICENSE` **MIT**  ·  `MSRV` **1.80+**  ·  `EDITION` **2024**
<!-- @readme:meta:end -->

<div align="center">
  <img src="https://wsrv.nl/?url=https://cdn.jsdelivr.net/gh/SSL-ACTX/SSL-ACTX@main/images/seuriin_frz_circ.gif&output=webp&maxage=1y&n=-1&q=20&w=450" width="140" height="140" alt="Seuriin">
  <br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=SSL-ACTX.SSL-ACTX&color=06b6d4" alt="Visitors">
</div>

---

### § 01 · PROFILE

Systems researcher and compiler engineer focused on formal verification, mathematical memory safety, low-level execution models, and runtime security. Designs self-contained language toolchains, virtual machines, and high-assurance systems from first principles.

**Stack:** Rust · C/C99 · Zig · F\* w/ Pulse · ARM64 NEON · WebAssembly · Seccomp-BPF · SMT (oxiz, Z3) · Cranelift

---

### § 02 · PROJECTS

<!-- @readme:pipeline:start -->
```text
⟨DRIVER⟩ Valerie  ──►  ⟨CRYPTO⟩ Shuangning  ──►  ⟨LANG⟩ Causm  ──►  ⟨JIT⟩ Lirien  ──►  ⟨WEB⟩ Ruoxi
```
<!-- @readme:pipeline:end -->

**[Valerie](https://github.com/SSL-ACTX/valerie)** — Compiler driver, build orchestrator & formal verification pipeline · Vale/F\*/Pulse · Z3 · KaRaMeL C extraction · constant-time audit · native/QEMU targets

<!-- @readme:stats:url=github.com/SSL-ACTX/valerie:start -->
```text
REPO METRICS · github.com/SSL-ACTX/valerie
Files: 134  ·  Total Lines: 25173  ·  Languages: 9
■■■■■■■■■■■■■■■■■■■■▣▣▣▣▣▣▣▣▣▣▣▣▣□□□
──────────────────────────────────────────────────────
■ F* (53.7%)  ▣ Rust (36.4%)  □ OCaml (7.0%)  ▫ TOML (0.8%)  ░ Assembly (0.8%)  ■ Other (0.6%)  ▣ Python (0.3%)  □ Markdown (0.2%)  ▫ C (0.1%)

┌──────────────────────┬───────┬───────┬─────────┬───────┬───────┐
│ LANGUAGE             │ FILES │ BLANK │ COMMENT │ CODE  │ TOTAL │
├──────────────────────┼───────┼───────┼─────────┼───────┼───────┤
│ F*                   │ 74    │ 1164  │ 428     │ 11548 │ 13140 │
│  └─ Vale (vaf)       │ 29    │ 521   │ 209     │ 3071  │ 3801  │
│  └─ Pulse            │ 2     │ 73    │ 57      │ 981   │ 1111  │
│ Rust                 │ 33    │ 867   │ 778     │ 7825  │ 9470  │
│ OCaml                │ 9     │ 149   │ 6       │ 1503  │ 1658  │
│  └─ menhir/ocamlyacc │ 1     │ 50    │ 4       │ 501   │ 555   │
│  └─ ocamllex         │ 1     │ 29    │ 0       │ 281   │ 310   │
│ TOML                 │ 7     │ 22    │ 1       │ 178   │ 201   │
│ Assembly             │ 5     │ 38    │ 33      │ 175   │ 246   │
│ Other                │ 3     │ 104   │ 26      │ 129   │ 259   │
│ Python               │ 1     │ 13    │ 1       │ 68    │ 82    │
│ Markdown             │ 1     │ 19    │ 7       │ 50    │ 76    │
│ C                    │ 1     │ 5     │ 12      │ 24    │ 41    │
│ TOTAL                │ 134   │ 2381  │ 1292    │ 21500 │ 25173 │
└──────────────────────┴───────┴───────┴─────────┴───────┴───────┘
```
<!-- @readme:stats:end -->

**[Shuangning](https://github.com/SSL-ACTX/shuangning)** — Experimental verified cryptographic core · F\* / Pulse proofs · C / Assembly targets

<!-- @readme:stats:url=github.com/SSL-ACTX/shuangning:start -->
```text
REPO METRICS · github.com/SSL-ACTX/shuangning
Files: 41  ·  Total Lines: 7083  ·  Languages: 8
■■■■■■■■■■■▣▣▣▣▣▣▣▣□□□□□□▫▫▫▫░░░░■■▣
──────────────────────────────────────────────────────
■ F* (30.5%)  ▣ C (22.3%)  □ Rust (17.3%)  ▫ Markdown (11.0%)  ░ Other (10.2%)  ■ Python (6.7%)  ▣ Assembly (1.2%)  □ TOML (0.7%)

┌────────────────┬───────┬───────┬─────────┬──────┬───────┐
│ LANGUAGE       │ FILES │ BLANK │ COMMENT │ CODE │ TOTAL │
├────────────────┼───────┼───────┼─────────┼──────┼───────┤
│ F*             │ 16    │ 258   │ 224     │ 1678 │ 2160  │
│  └─ Pulse      │ 2     │ 31    │ 17      │ 332  │ 380   │
│  └─ Vale (vaf) │ 2     │ 70    │ 12      │ 281  │ 363   │
│ C              │ 9     │ 251   │ 154     │ 1228 │ 1633  │
│ Rust           │ 5     │ 163   │ 94      │ 953  │ 1210  │
│ Markdown       │ 1     │ 121   │ 78      │ 605  │ 804   │
│ Other          │ 4     │ 129   │ 14      │ 563  │ 706   │
│ Python         │ 2     │ 68    │ 2       │ 369  │ 439   │
│ Assembly       │ 2     │ 4     │ 18      │ 66   │ 88    │
│ TOML           │ 2     │ 6     │ 0       │ 37   │ 43    │
│ TOTAL          │ 41    │ 1000  │ 584     │ 5499 │ 7083  │
└────────────────┴───────┴───────┴─────────┴──────┴───────┘
```
<!-- @readme:stats:end -->

**[Causm](https://github.com/SSL-ACTX/Causm)** — Real-time systems lang · EGC · SMT proofs · Cranelift JIT · WASIp2

<!-- @readme:stats:url=github.com/SSL-ACTX/Causm:start -->
```text
REPO METRICS · github.com/SSL-ACTX/Causm
Files: 387  ·  Total Lines: 77257  ·  Languages: 10
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■▣▣▣□□
──────────────────────────────────────────────────────
■ Rust (86.3%)  ▣ Markdown (6.5%)  □ Other (5.4%)  ▫ JSON (0.5%)  ░ TOML (0.4%)  ■ Python (0.2%)  ▣ Shell (0.2%)  □ TypeScript (0.2%)  ▫ JavaScript (0.2%)  ░ YAML (0.0%)

┌────────────┬───────┬───────┬─────────┬───────┬───────┐
│ LANGUAGE   │ FILES │ BLANK │ COMMENT │ CODE  │ TOTAL │
├────────────┼───────┼───────┼─────────┼───────┼───────┤
│ Rust       │ 209   │ 4628  │ 2002    │ 57641 │ 64271 │
│ Markdown   │ 54    │ 1821  │ 1309    │ 4321  │ 7451  │
│ Other      │ 90    │ 494   │ 55      │ 3625  │ 4174  │
│ JSON       │ 7     │ 0     │ 0       │ 360   │ 360   │
│ TOML       │ 22    │ 43    │ 4       │ 300   │ 347   │
│ Python     │ 1     │ 30    │ 7       │ 165   │ 202   │
│ Shell      │ 1     │ 22    │ 26      │ 137   │ 185   │
│ TypeScript │ 1     │ 19    │ 3       │ 106   │ 128   │
│ JavaScript │ 1     │ 0     │ 4       │ 102   │ 106   │
│ YAML       │ 1     │ 3     │ 0       │ 30    │ 33    │
│ TOTAL      │ 387   │ 7060  │ 3410    │ 66787 │ 77257 │
└────────────┴───────┴───────┴─────────┴───────┴───────┘
```
<!-- @readme:stats:end -->

**[Ruoxi](https://github.com/SSL-ACTX/Ruoxi)** — Web synthesis engine · 23µs/page · 43k pages/sec

<!-- @readme:stats:url=github.com/SSL-ACTX/Ruoxi:start -->
```text
REPO METRICS · github.com/SSL-ACTX/Ruoxi
Files: 50  ·  Total Lines: 17361  ·  Languages: 6
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■▣□▫
──────────────────────────────────────────────────────
■ Rust (91.2%)  ▣ CSS (3.5%)  □ Other (2.8%)  ▫ Python (1.8%)  ░ TOML (0.5%)  ■ Markdown (0.2%)

┌──────────┬───────┬───────┬─────────┬───────┬───────┐
│ LANGUAGE │ FILES │ BLANK │ COMMENT │ CODE  │ TOTAL │
├──────────┼───────┼───────┼─────────┼───────┼───────┤
│ Rust     │ 35    │ 1381  │ 846     │ 13451 │ 15678 │
│ CSS      │ 1     │ 79    │ 19      │ 515   │ 613   │
│ Other    │ 6     │ 80    │ 62      │ 411   │ 553   │
│ Python   │ 1     │ 58    │ 4       │ 265   │ 327   │
│ TOML     │ 6     │ 9     │ 0       │ 77    │ 86    │
│ Markdown │ 1     │ 24    │ 49      │ 31    │ 104   │
│ TOTAL    │ 50    │ 1631  │ 980     │ 14750 │ 17361 │
└──────────┴───────┴───────┴─────────┴───────┴───────┘
```
<!-- @readme:stats:end -->

**[Lirien](https://github.com/SSL-ACTX/Lirien)** — Verifying JIT for Python · SMT refinement types · Cranelift

<!-- @readme:stats:url=github.com/SSL-ACTX/Lirien:start -->
```text
REPO METRICS · github.com/SSL-ACTX/Lirien
Files: 210  ·  Total Lines: 40348  ·  Languages: 5
■■■■■■■■■■■■■■■■■■■■■■■▣▣▣▣▣▣▣▣▣▣▣□▫
──────────────────────────────────────────────────────
■ Rust (64.0%)  ▣ Python (30.6%)  □ Markdown (3.1%)  ▫ Other (1.7%)  ░ TOML (0.6%)

┌──────────┬───────┬───────┬─────────┬───────┬───────┐
│ LANGUAGE │ FILES │ BLANK │ COMMENT │ CODE  │ TOTAL │
├──────────┼───────┼───────┼─────────┼───────┼───────┤
│ Rust     │ 84    │ 1668  │ 1148    │ 21462 │ 24278 │
│ Python   │ 100   │ 2458  │ 387     │ 10262 │ 13107 │
│ Markdown │ 16    │ 574   │ 435     │ 1030  │ 2039  │
│ Other    │ 2     │ 117   │ 3       │ 566   │ 686   │
│ TOML     │ 8     │ 30    │ 9       │ 199   │ 238   │
│ TOTAL    │ 210   │ 4847  │ 1982    │ 33519 │ 40348 │
└──────────┴───────┴───────┴─────────┴───────┴───────┘
```
<!-- @readme:stats:end -->



---

### § 03 · ACTIVITY

<div align="center">
  <img src="https://raw.githubusercontent.com/SSL-ACTX/SSL-ACTX/main/generated/overview.svg" alt="Profile Overview" width="49%">
  <img src="https://raw.githubusercontent.com/SSL-ACTX/SSL-ACTX/main/generated/languages.svg" alt="Language Stats" width="49%">
</div>

---

<!-- @readme:seal:start -->
```text
┌────────────────────────────────────────────────────────┐
│ REPRODUCIBILITY DIGEST                                 │
├────────────────────────────────────────────────────────┤
│ GIT REVISION  │ b15e4e8 (● clean)                      │
│ MANIFEST HASH │ SHA256: 66e756962bdd…                  │
└────────────────────────────────────────────────────────┘
```
<!-- @readme:seal:end -->

`seuriin@gmail.com` · `discord: seuriin` · `messenger: seuriin`
