<div align="center">
  <img src="https://wsrv.nl/?url=https://cdn.jsdelivr.net/gh/SSL-ACTX/SSL-ACTX@main/images/seuriin_frz_circ.gif&output=webp&maxage=1y&n=-1&q=20&w=450" width="180" height="180" alt="Seuriin's Profile Picture">
  
  <h1>Seuriin</h1>
  <p><i>Systems Researcher | Compilers & Distributed Runtimes</i></p>
  
  <p align="center">
    <img src="https://img.shields.io/badge/Degree-BSIT%20@%20CDM-06b6d4?style=flat-square" alt="Education">
    <img src="https://visitor-badge.laobi.icu/badge?page_id=SSL-ACTX.SSL-ACTX&color=06b6d4" alt="Visitors">
  </p>

  <p align="center">
    <i>"The more you know, the more you know you don't know."</i>
  </p>
</div>

> [!NOTE]
> This is a **personal profile README** — a running log of things I’ve built, broken, and learned.  
> Not a professional portfolio. Not here to impress anyone.

---

### 🌙 Technical Profile
  
**Graduating June 2026** (BSIT) — **Colegio de Montalban**  
*Formal Methods • Runtime Security • Systems Architecture*

I enjoy building systems from scratch to understand how they work under the hood. This profile is just a collection of my projects and experiments—ranging from custom runtimes to security research.

 * 🎓 **Current Status:** Graduating June 23, 2026 "TODAY!" (BSIT) | Colegio de Montalban.
 * 🦀 **Focus:** Formal Methods, Runtime Security, Systems Architecture.
 * 🧪 **Primary Stack:** **Rust** (Performance Primitives), **Zig** (Native Interception), **Python & JavaScript** (Orchestration).
 * 🌐 **Web Development:** Engineering modern, performant web applications utilizing **Next.js** and **FastAPI**.
 * 🫢 **Notice:** I prefer building something from scratch over reading about it. Currently diving deeper into formal methods and runtime internals.

---

### 🔭 Systems Research & Technical Explorations

A collection of theoretical and practical explorations into systems-level engineering.

<br>

| Repository | Project Specification | Technologies |
| :--- | :--- | :--- |
| **[Lirien](https://github.com/SSL-ACTX/Lirien)** | A verifying JIT compiler for a safe subset of Python. By leveraging Z3 SMT verification and Cranelift code generation, Lirien statically proves refinement-type invariants, memory safety, and bounds correctness at compile-time—then emits native machine code with GIL-free execution, SIMD intrinsics, monomorphization, and AOT IR caching. | <img src="https://skillicons.dev/icons?i=rust,python&theme=dark&perline=1" /> |
| **[Astraea](https://github.com/SSL-ACTX/astraea)** | A zero-trust security middleware for Node.js implementing an Object-Capability (O-Cap) enforcement layer. It utilizes dynamic linker hijacking via a Zig interceptor and a Rust engine to perform context-aware attribution and Seccomp-BPF kernel hardening against supply-chain attacks. | <img src="https://skillicons.dev/icons?i=rust,zig,nodejs&theme=dark&perline=2" /> |
| **[Iris](https://github.com/SSL-ACTX/iris)** | A high-performance distributed actor runtime in Rust with first-class Python bindings. It features a **reduction-based cooperative scheduler** (Vortex) and a location-transparent messaging fabric, enabling zero-downtime hot-swapping of actor logic and resilient, cross-language service orchestration. | <img src="https://skillicons.dev/icons?i=rust,python,js,nodejs&theme=dark&perline=2" /> |
| **[Causm](https://github.com/SSL-ACTX/Causm)** | A domain-specific research language targeting non-determinism in concurrent systems. It implements an **Entropic Memory Model** (state decay) and **Isochronous Scheduling**, using a Z3-governed correctness kernel to mathematically prove temporal invariants and race-freedom at compile-time. | <img src="https://skillicons.dev/icons?i=rust,ts&theme=dark&perline=2" /> |
| **[Ocular](https://github.com/SSL-ACTX/ocular)** | A high-performance, zero-allocation instruction tracer for Python 3.12+ (PEP 669). It leverages hardware TSC cycle counting for nanosecond-precision profiling and implements **dynamic de-instrumentation**, automatically unhooking from hot loops to allow CPython's native quickening while generating Chrome Perfetto timelines. | <img src="https://skillicons.dev/icons?i=rust,python&theme=dark&perline=1" /> |
| **[MirageFS](https://github.com/SSL-ACTX/mirage-fs)** | A steganographic virtual block device enabling encrypted storage within multimedia containers. By camouflaging data as **Adobe DNG metadata** or **H.264 NAL-unit filler**, it creates a FUSE-mounted filesystem that is mathematically indistinguishable from standard media noise to defeat forensic analysis. | <img src="https://skillicons.dev/icons?i=rust&theme=dark&perline=1" /> |
| **[Argus](https://github.com/SSL-ACTX/argus)** | An entropy-based secret scanner utilizing Aho-Corasick pattern matching and Shannon entropy context to distinguish true cryptographic risks from noise in large codebases. | <img src="https://skillicons.dev/icons?i=rust,python,wasm&theme=dark&perline=2" /> |
| **[Isla](https://github.com/SSL-ACTX/isla)** | A userspace TCP/IP stack implementation in Rust designed to bypass kernel overhead, prioritizing raw throughput for specialized, high-performance networking research. | <img src="https://skillicons.dev/icons?i=rust&theme=dark&perline=1" /> |

<br>

---

### 🛠 Engineering & Toolset

I'm a big believer in learning by building. To really understand a complex concept, I try to implement it from scratch. 

- **Systems & Runtimes:** **Rust** is my go-to for memory safety and performance. I use it to build core infrastructure like distributed actor runtimes and custom schedulers, pairing it with **Python** and **JavaScript** for high-level orchestration.
- **Compilers & Formal Methods:** I spend a lot of time exploring language design and compiler architecture. I'm especially interested in integrating **SMT solvers (Z3)** to mathematically prove memory safety, type constraints, and temporal invariants.
- **Security & Low-Level Internals:** I like digging into the OS boundary. This involves native C-ABI interception (often using **Zig**), kernel-level sandboxing (Seccomp-BPF), and researching steganography and anti-forensics.
- **Web Architectures:** When building standard applications or APIs, I stick to reliable stacks like **Next.js** and **FastAPI**, focusing on type safety and fast development cycles.
- **Workflow:** Mostly terminal-based. I use **KDE Kate** for most of my editing, but switch to **VSCode** when I'm working on language support or larger projects.

<div align="center">
  <img src="https://skillicons.dev/icons?i=rust,zig,python,js,ts,nodejs,wasm,nextjs,fastapi,mongodb,mysql,redis,docker,bash,git,github,vscode&theme=dark&perline=9" />
</div>

---

### 📊 Activity & Analytics

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

### ☕ Connection

I'm always down to chat about systems, performance (like why Python is slow), or nerdy/weeb stuff. If you're building something weird or unconventional, feel free to reach out.

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
