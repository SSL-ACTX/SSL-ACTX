<div align="center">
  <img src="https://wsrv.nl/?url=https://cdn.jsdelivr.net/gh/SSL-ACTX/SSL-ACTX@main/images/seuriin_frz_circ.gif&output=webp&maxage=1y&n=-1&q=20&w=450" width="180" height="180" alt="Seuriin's Profile Picture">
  
  <h1>Seuriin</h1>
  <p><i>Systems Researcher | Compilers & Distributed Runtimes</i></p>
  
  <p align="center">
    <img src="https://img.shields.io/badge/Graduated-BSIT%20%40%20CDM-gold?style=flat-square" alt="Graduated">
    <img src="https://img.shields.io/badge/Active%20Focus-Causm%20Compiler-06b6d4?style=flat-square&logo=rust&logoColor=white" alt="Active Focus">
    <img src="https://visitor-badge.laobi.icu/badge?page_id=SSL-ACTX.SSL-ACTX&color=06b6d4" alt="Visitors">
  </p>

  <p align="center">
    <i>"The more you know, the more you know you don't know."</i>
  </p>
</div>

---

### Technical Profile

BSIT Graduate (June 2026, Colegio de Montalban) focused on formal verification, runtime security, and low-level systems architecture. I build compilers, virtual machines, and distributed execution engines from first principles.

* **Core Focus:** Formal Methods, Temporal Systems, Runtime Security, Compiler Architectures.
* **Primary Languages:** Rust for core compiler infrastructure & VMs, Zig for native stuff, Python and JavaScript/TypeScript for orchestration and tooling.
* **Web & Systems Stack:** Next.js, FastAPI, Linux Seccomp/eBPF, POSIX C-ABI, and SMT Solvers (Z3).

---

### Active Research: The Causm Language

Currently designing and developing **[Causm](https://github.com/SSL-ACTX/Causm)** — a real-time, formally verified systems programming language with temporal semantics, entropic memory decay, and empirical contract synthesis.

```text
[ Source (.csm) ] ──> [ Pest AST / Lowering ] ──> [ SSA IR & DCE / Phi Opts ] ──> [ Z3 SMT Prover ] ──> [ Temporal Virtual Machine (TVM) ]
```

* **Temporal Quad-Clock Architecture:** Decouples execution across static WCET bounds, TVM deterministic logical clocks, capability I/O latency, and hardware cycle counters (`cntvct_el0` / TSC).
* **Entropic Memory Model (EGC):** Physics-inspired affine linear types with time-decay lifetimes (`decay_after`, `lease`), declarative C-handle reclamation (`auto_drop`), and zero runtime GC pauses.
* **Profile-Guided Time Contract Tuning (`causm tune`):** Automated AST-rewriting engine that empirically derives P99.9 execution bounds under chaotic conditions and generates verified `taking Nms` contracts in-place.
* **Self-Hosted POSIX Standard Library:** Native standard library authored in pure `.csm` using dynamic capability-sandboxed C-ABI FFI (`std/fs`, `std/path`, `std/time`, `std/net`, `std/process`).

---

### Projects & Systems Research

A selection of open-source projects covering language verification, runtime security, distributed engines, and steganographic systems.

<br>

| Repository | Project Specification | Technologies |
| :--- | :--- | :--- |
| **[Causm](https://github.com/SSL-ACTX/Causm)** | A formally verified, hard real-time systems language with temporal pacing, SSA IR optimizations, SMT correctness proofs (Z3), and profile-guided contract synthesis (`causm tune`). | <img src="https://skillicons.dev/icons?i=rust,ts&theme=dark&perline=2" /> |
| **[Lirien](https://github.com/SSL-ACTX/Lirien)** | A verifying JIT compiler for a safe subset of Python. Uses Z3 SMT verification to statically prove refinement types, memory bounds, and safety invariants before lowering to native code with Cranelift. | <img src="https://skillicons.dev/icons?i=rust,python&theme=dark&perline=1" /> |
| **[Astraea](https://github.com/SSL-ACTX/astraea)** | A security middleware for Node.js implementing Object-Capability enforcement at the native boundary via dynamic C-ABI syscall hijacking (Zig) and kernel Seccomp-BPF filters. | <img src="https://skillicons.dev/icons?i=rust,zig,nodejs&theme=dark&perline=2" /> |
| **[Iris](https://github.com/SSL-ACTX/iris)** | A distributed actor runtime in Rust with Python bindings, featuring a reduction-based cooperative scheduler, location-transparent messaging, and live actor code updates. | <img src="https://skillicons.dev/icons?i=rust,python,js,nodejs&theme=dark&perline=2" /> |
| **[Ocular](https://github.com/SSL-ACTX/ocular)** | An instruction-level tracer and telemetry runtime for Python 3.12+ (PEP 669). Uses hardware TSC cycle counting and adaptive de-instrumentation to minimize profiling overhead. | <img src="https://skillicons.dev/icons?i=rust,python&theme=dark&perline=1" /> |
| **[MirageFS](https://github.com/SSL-ACTX/mirage-fs)** | A steganographic virtual block device (FUSE / WebDAV) that mounts encrypted filesystems inside media containers (PNG, MP4, MP3) with custom format-specific injectors. | <img src="https://skillicons.dev/icons?i=rust&theme=dark&perline=1" /> |
| **[Argus](https://github.com/SSL-ACTX/argus)** | An entropy-based security scanner combining Aho-Corasick pattern matching with Shannon entropy analysis to detect secrets and credentials in source repositories. | <img src="https://skillicons.dev/icons?i=rust,python,wasm&theme=dark&perline=2" /> |

<br>

---

### Engineering & Toolset

* **Systems & Runtimes:** Building core infrastructure, register-based VMs, and low-level runtimes in Rust, paired with Python or Node.js for high-level APIs.
* **Compilers & Formal Methods:** Designing SSA-form IR pipelines, dead-code elimination, and DSLs backed by SMT solvers (Z3) to guarantee real-time WCET safety.
* **Security & Systems Internals:** C-ABI dynamic interception using Zig, Linux Seccomp-BPF sandboxing, and binary obfuscation/steganography research.
* **Web Engineering:** Building web applications and backend services with Next.js and FastAPI.

<div align="center">
  <img src="https://skillicons.dev/icons?i=rust,zig,python,js,ts,nodejs,wasm,nextjs,fastapi,mongodb,mysql,redis,docker,bash,git,github,vscode&theme=dark&perline=9" />
</div>

---

### Activity & Analytics

<div align="center">
  <table border="0" cellpadding="10" cellspacing="0">
    <tr>
      <td width="50%" valign="top">
        <img src="https://raw.githubusercontent.com/SSL-ACTX/SSL-ACTX/main/generated/overview.svg" alt="Profile Overview" />
      </td>
      <td width="50%" valign="top">
        <img src="https://raw.githubusercontent.com/SSL-ACTX/SSL-ACTX/main/generated/languages.svg" alt="Language Stats" />
      </td>
    </tr>
  </table>
</div>

---

<p align="center">
  <a href="mailto:seuriin@gmail.com">
    <img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>
  <a href="https://discord.com/users/seuriin" target="_blank">
    <img src="https://img.shields.io/badge/Discord-Seuriin-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord">
  </a>
  <a href="https://m.me/seuriin" target="_blank">
    <img src="https://img.shields.io/badge/Messenger-Seuriin-0084FF?style=for-the-badge&logo=facebook-messenger&logoColor=white" alt="Messenger">
  </a>
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=06b6d4&height=60&section=footer" width="100%"/>
</p>
