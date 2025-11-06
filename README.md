# Semiconductor Supply-Chain Network: API Collector & Graph Gallery

**End-to-end, API-driven pipeline** that builds a buyer–supplier network for semiconductor firms and produces publication-quality visuals for downstream social network analysis (ERGM, QAP, etc.).

- **What this shows:** How **network structure** of global supply chains could be collected, organized, and visualized.
- **Who this helps:** Researchers, data engineers, and anyone interested in supply network analysis.

---

## Table of Contents
- [Highlights](#highlights)
- [Repository Contents](#repository-contents)
- [Example Graphs](#example-graphs-rendered-inline)
- [How the Collector Works (Overview)](#how-the-collector-works-overview)
- [Data Useage & Access](#data-provenance--access)
- [Quick Start (Minimal)](#quick-start-minimal)
- [Research Context](#research-context)
- [Notes & Contact](#notes--contact)

---

## Highlights

- **Collector + Graphs:** Python pipeline (Refinitiv) to fetch firm attributes and supplier–buyer edges, reconcile names/IDs, export CSVs, and render graphs.
- **Scalable new collector:** Parallelized lookups and cleaner expand-search logic; designed to scale to **thousands of firms** (subject to API limits and your data access).
- **Example outputs:** Curated figures in `Graphs/` demonstrate structural patterns by **market cap**, **R&D**, **firm role**, and **HQ geography**.

---

## Repository Contents

- `API Collector finalized.py` — script entry point for the current collector  
- `API collector fnialized.ipynb` — notebook version mirroring the same logic  
- `Graphs/` — **example** figures generated from an **older** dataset (details below):  
  - `Market Cap All.png`  
  - `RnD Groups.png`  
  - `Role 80 Graph.png`  
  - `HQ 80 Graph.png`  
  - `HQ no USA 80 Graph.png`

---

## Example Graphs (Rendered Inline)

> These images were generated with an **older version** of the collector and are shown here **as examples** of results.  
> The new collector in this repo is **more efficient** and designed for **larger-scale** datasets.

### Market Cap – All Firms
Network of semiconductor firms and inter-firm ties. **Node color/size = market capitalization**.  
![Market Cap All](Graphs/Market%20Cap%20All.png)

### R&D Groups
Same network with **node color/size = R&D expenses**.  
![RnD Groups](Graphs/RnD%20Groups.png)

### Roles (Chip Users vs. Manufacturers)
Firms colored by **role**; **clear clustering** by role.  
![Role 80 Graph](Graphs/Role%2080%20Graph.png)

### Headquarters Countries (with U.S.)
Firms colored by **HQ country**; distinct **U.S. cluster**.  
![HQ 80 Graph](Graphs/HQ%2080%20Graph.png)

### Headquarters Countries (U.S. Removed)
U.S.-HQ firms removed; clusters for **Taiwan**, **Korea**, and **Japan** become clearer.  
![HQ no USA 80 Graph](Graphs/HQ%20no%20USA%2080%20Graph.png)

---

## How the Collector Works (Overview)

1. **Resolve firms → identifiers (RICs)**  
   Run the Refinitiv terminal to locate and map input firm names to RICs.
2. **Fetch firm attributes (nodes)**  
   HQ country, market cap (USD), revenue proxies, etc.
3. **Fetch supplier–buyer relationships (edges)**  
   Relationship endpoints + confidence scores; filtered for reliability.
4. **Reconcile names/IDs**  
   Human-readable names for analysis and visualization.
5. **Export & visualize**  
   CSVs for modeling; PNG graphs for quick structural inspection.

**Entry points:** `API Collector finalized.py` and `API collector fnialized.ipynb`

---

## Data Useage & Access

- The original figures above come from an older run of the pipeline. For transparency:

  > *The original data collection process is listed in a Jupyter notebook **Network Analysis**. It wasn’t tightly organized, so I extracted the raw data and stored them in an Excel file **raw_data** for the convenience of replicating my results.*

- **Important:** The underlying dataset **cannot be distributed** here because it draws on **proprietary business data** (Refinitiv). This repository provides **code** and **example images** only.

- The **new collector** here is **more efficient** and designed for **larger-scale** collection, but rebuilding the dataset requires your **own licensed access** and **credentials**.

---

## Quick Start (Minimal)

1. Ensure you have Python and valid access credentials for your data provider (e.g., Refinitiv).
2. In `API Collector finalized.py` (or the notebook), specify your **seed firm list**.
3. Run the collector to:
   - Resolve identifiers
   - Pull firm attributes and supplier–buyer ties
   - Export tables (CSV) and generate visuals (PNG)


---

## Research Context

This pipeline supports the argument that **network structure**—beyond firm capacity or national policy—**constrains and sustains** outsourcing decisions in semiconductor supply chains.

- **Thesis:** [Thesis Link](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C14&q=When+Structure+Takes+Over%3A+The+Autonomy+of+Global+Supply+Chain+Networks+Beyond+Firm+Capacity+and+Institutional+Constraints&btnG=)

---

## Notes & Contact

- Figures in `Graphs/` are **illustrative** from an **older** data snapshot.
- Rebuilding requires your **licensed** data access and is subject to provider **terms**.
- Happy to discuss API limits, confidence thresholds for ties, layout choices, or model specs (ERGM/QAP).

---

*© 2025. Code provided for research and evaluation; data access and reuse remain subject to the original provider’s license.*
