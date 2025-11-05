# Semiconductor Supply-Chain: Data Collector & Network Visualizations

API-driven pipeline that assembles a **buyer–supplier network** for publicly listed semiconductor firms , then produces **model-ready data** for **exploratory visuals** and regression (ERGM, QAP) in network analysis.

> Goal: expose how **network structure** sustains outsourcing relationships—even after the 2020–2023 chip-shortage shock.

---

## Repository Structure








### This is the original dataset and network mapping of my research project proposal: A network analysis to the semiconductor supply chain governance structure
- The original data collection process is listed in this jupyter notebook [Network Analysis](https://github.com/Cosmo280/organizational-network-analysis/blob/main/Network%20Analysis/Network%20Analysis.ipynb). It's not well organized so I extracted the raw data and store them in this excel file [raw_data](https://github.com/Cosmo280/organizational-network-analysis/blob/main/Network%20Analysis/raw_data.xlsx) for the convinence of replicate my results. In the excel file, the column "core actors" are the names of all the core organizations; the column "peripheral actors" are the names of all the peripheral organizations; the columns "Ties_Org1" and "Ties_Org2" are the two organizations that formed a tie, make all rows in columns "Ties_Org1" and "Ties_Org2" into ("Ties_Org1", "Ties_Org2") tuples to create a list of all the network ties. Because the ties are non-directional, there is no need to create a list of ("Ties_Org2", "Ties_Org1") tuples. 
&nbsp;
- The Latex version of the final paper is [here](https://github.com/Cosmo280/organizational-network-analysis/blob/main/Thesis%20proposal%20components/LitReview.tex); the pdf version is [here](); the citations are [here](https://github.com/Cosmo280/organizational-network-analysis/blob/main/Thesis%20proposal%20components/LitReview.tex).
* ### Link to presentation slides: https://docs.google.com/presentation/d/1bnDo80cQu7bRS-YaNlS6LAqo-4ZAsahPlmnQUqEHorw/edit#slide=id.g2d28a14a21f_0_1226
&nbsp;
- My project argues that transaction cost theory offers no middle ground between internalizing and outsourcing when analyzing firm boundaries. Thus embeddedness should be operationalize with structural cohesion and the depiction of the inter-firm organizational governance structure would require network analysis with organizations as unit of analysis and interlocking dirocrates are strong ties.
&nbsp; 
- [Requirements with versions](https://github.com/Cosmo280/30200/blob/main/requirements.txt): 
* Python -- 3.11.5
* Numpy -- 1.24.3
* Pandas -- 1.5.3
* Matplotlib -- 3.7.1
* Networkx -- 3.1
&nbsp;
- Citation: Wang, C.(2024), organizational network analysis (Version 1.0.0). GitHub. https://github.com/Cosmo280/30200.git
