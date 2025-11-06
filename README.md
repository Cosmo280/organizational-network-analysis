# Semiconductor Supply-Chain Network: API Collector & Graph Gallery

**End-to-end, API-driven pipeline** that builds a buyer–supplier network for semiconductor firms and produces publication-quality visuals for downstream social network analysis (ERGM, QAP, etc.).

- **What this shows:** How **network structure** helps sustain outsourcing ties even after shocks (e.g., the 2020–2023 chip shortage).
- **Who this helps:** Researchers, data engineers, and hiring teams evaluating full-lifecycle data work (collection → cleaning → modeling → visualization).

---

## Highlights

- **Collector + Graphs:** Python pipeline (Refinitiv) to fetch firm attributes and supplier–buyer edges, reconcile names/IDs, export CSVs, and render graphs.
- **Scalable new collector:** Parallelized lookups and cleaner expand-search logic; designed to scale to **thousands of firms** (subject to API limits and your data access).
- **Example outputs:** Curated figures in `Graphs/` demonstrate structural patterns by **market cap**, **R&D**, **firm role**, and **HQ geography**.

---

## Repository Layout
.
├── API Collector finalized.py
├── API collector fnialized.ipynb
├── Graphs/
│ ├── Market Cap All.png
│ ├── RnD Groups.png
│ ├── Role 80 Graph.png
│ ├── HQ 80 Graph.png
│ └── HQ no USA 80 Graph.png
└── README.md


- **API Collector finalized.py** — script entry point for the current collector.
- **API collector fnialized.ipynb** — notebook version mirroring the same logic.
- **Graphs/** — **example** figures generated from an **older** dataset (details below).

---

## Example Graphs (from `Graphs/`)

> These images were generated using **an older version** of the collector and are shown **as examples** of results.

- **`Market Cap All.png`**  
  Network of semiconductor firms and inter-firm ties. **Node color/size = market capitalization**.

- **`RnD Groups.png`**  
  Same network with **node color/size = R&D expenses**.

- **`Role 80 Graph.png`**  
  Firms colored by **role** (chip users vs. manufacturers). **Clear clustering** by role.

- **`HQ 80 Graph.png`**  
  Firms colored by **HQ country**. Distinct cluster for **U.S.-headquartered** firms.

- **`HQ no USA 80 Graph.png`**  
  U.S.-HQ firms removed; clusters for **Taiwan**, **Korea**, and **Japan** become clearer.

You can open these directly in the `Graphs/` folder on GitHub to view them inline.

---

## How the Collector Works (Overview)

1. **Resolve firms → identifiers (RICs)**  
   Batched discovery to map input firm names to RICs.
2. **Fetch firm attributes (nodes)**  
   HQ country, market cap (USD), revenue proxies, etc.
3. **Fetch supplier–buyer relationships (edges)**  
   Relationship endpoints + confidence scores; filtered for reliability.
4. **Reconcile names/IDs**  
   Human-readable names for analysis and visualization.
5. **Export & visualize**  
   CSVs for modeling; PNG graphs for quick structural inspection.

**Entry points**
- Script: `API Collector finalized.py`  
- Notebook: `API collector fnialized.ipynb`

---

## Data Provenance & Access

- The **original data collection** and early visuals were associated with a prior project setup.  
  The process was documented in a Jupyter notebook (titled **“Network Analysis”**) and the raw outputs were extracted to an Excel file called **`raw_data`** purely to **aid replication** of that older workflow:
  > *“The original data collection process is listed in this Jupyter notebook **Network Analysis**. It wasn’t tightly organized, so I extracted the raw data and stored them in an Excel file **raw_data** for the convenience of replicating my results.”*

- **Important:** The underlying dataset **cannot be distributed** here because it draws on **proprietary business data** (Refinitiv). This repository includes **code** and **example images** only.

- The **new collector** in this repository is **more efficient** and designed for **larger-scale** collection, but rebuilding the dataset requires your **own licensed access** and **credentials**.

---

## Quick Start (minimal)

1. Ensure you have Python and valid access credentials for your data provider (e.g., Refinitiv).
2. In `API Collector finalized.py` (or the notebook), specify your **seed firm list**.
3. Run the collector to:
   - Resolve identifiers
   - Pull firm attributes and supplier–buyer ties
   - Export tables (CSV) and generate visuals (PNG)

> Note: This README intentionally skips pinned versions; rely on the imports at the top of the script/notebook to set up your environment.

---

## Research Context

This pipeline supports the argument that **network structure**—beyond firm capacity or national policy—**constrains and sustains** outsourcing decisions in semiconductor supply chains.

- **Thesis (index link):**  
  *When Structure Takes Over: The Autonomy of Global Supply Chain Networks Beyond Firm Capacity  and Institutional Constraints* — see **Google Scholar**:  
    [Thesis Link](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C14&q=When+Structure+Takes+Over%3A+The+Autonomy+of+Global+Supply+Chain+Networks+Beyond+Firm+Capacity+and+Institutional+Constraints&btnG=)

---

## Notes & Contact

- Figures in `Graphs/` are **illustrative** from an **older** data snapshot.
- Rebuilding requires your **licensed** data access and is subject to provider **terms**.
- Happy to discuss API limits, confidence thresholds for ties, layout choices, or model specs (ERGM/QAP).

---

*© 2025. Code provided for research and evaluation; data access and reuse remain subject to the original provider’s license.*
