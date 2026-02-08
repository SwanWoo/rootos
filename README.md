# RootOS — Personal Digital Infrastructure Architecture

RootOS is an architect-level personal digital infrastructure system that unifies knowledge, engineering assets, projects, data, and life management into a single scalable directory architecture.

It is inspired by:
- Linux Filesystem Hierarchy Standard (FHS)
- DevOps & MLOps lifecycle design
- Knowledge Management Systems (PKM, Zettelkasten)
- Enterprise Architecture frameworks
- Personal Digital Infrastructure (PDI) concepts

RootOS is not just a folder structure — it is an operating system for your digital life.

---

## 1. Core Concepts

RootOS is designed around five architectural layers:

| Layer | Name        | Purpose |
|-------|------------|--------|
| L0    | Inbox      | Chaos & temporary files |
| L1    | Action     | Active projects and tasks |
| L2    | Knowledge  | Structured knowledge system |
| L3    | Engineering| Code, data, models, infrastructure |
| L4    | Asset      | Documents, finance, identity |
| L5    | Archive    | Historical data |
| L6    | System     | Rules, automation, security |

---

## 2. Architecture Overview

```

ROOTOS/
├── 00_Inbox
├── 10_Action
├── 20_Knowledge
├── 30_Engineering
├── 40_Asset
├── 50_Business
├── 90_Archive
└── 99_System

````

RootOS is designed to scale from personal use to enterprise-level knowledge and asset management.

---

## 3. Features

- YAML-driven directory architecture
- Cross-platform support (macOS / Linux)
- CLI-based initialization
- Modular presets (Architect / AI Engineer / Minimal)
- GitHub Actions CI integration
- Extensible to DevOps, MLOps, PKM, and AI workflows

---

## 4. Quick Start

### Install dependencies

```bash
pip install pyyaml
````

### Initialize RootOS

```bash
python src/rootos.py --path ~/Workspace
```

---

## 5. Presets

RootOS supports multiple architectural presets:

* architect.yaml — Architect-level digital infrastructure
* ai_engineer.yaml — AI/LLM/MLOps oriented
* minimal.yaml — Lightweight structure

Example:

```bash
python src/rootos.py --config config/presets/architect.yaml
```

---

## 6. Design Philosophy

RootOS follows three core principles:

1. Architecture-first
2. Asset-centric design
3. Long-term scalability

It treats personal knowledge, code, data, and identity as first-class assets.

---

## 7. Roadmap

* [ ] RootOS CLI tool (`rootos init`)
* [ ] Plugin system
* [ ] AI-based file classification
* [ ] Obsidian / NAS / Cloud integration
* [ ] Visualization of knowledge graph
* [ ] Enterprise mode

---

## 8. Vision

RootOS aims to become a personal digital operating system — a unified architecture for thinking, building, and managing digital assets.

> Your mind is the CPU. RootOS is the filesystem.

---

## License

MIT License
