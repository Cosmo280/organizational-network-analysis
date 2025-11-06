# %%
import json
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import refinitiv.data as rd
from refinitiv.data.content import symbol_conversion, search

# %% [markdown]
# ## Step 0: Open Refinitiv API session

# %%
rd.open_session()

# %% [markdown]
# ## Step 1: Get RIC Codes for a batch of firms

# %%
def get_ric_codes(company_names):
    ric_dict = {}
    for company in company_names:
        try:
            company_df = rd.discovery.search(
                view=search.Views.ORGANISATIONS,
                filter=f"CommonName xeq '{company}'",
                select="PrimaryRIC"
            )
            if not company_df.empty:
                ric_dict[company] = company_df.iloc[0]['PrimaryRIC']
        except Exception as e:
            print(f"Error fetching RIC for {company}: {e}")
    return ric_dict

# %% [markdown]
# ## Step 2: Fetch Firm Data (Nodes)

# %%
def fetch_firm_data(ric_list):
    fields = ['TR.CommonName', 
              'TR.RIC', 
              'TR.HeadquartersCountry',
              'TR.CompanyMarketCapitalization(Curn=USD)',
              'TR.F.RevGoodsSrvc5YrAvg(Period=FY0,Curn=USD)'
             ]
    firm_data = rd.get_data(universe=ric_list, fields=fields)
    
    return firm_data

# %% [markdown]
# ## Step 3: Fetch Supplier-Buyer Relationships (Edges)

# %%
def fetch_supplier_buyer_relationships(ric_list):
    fields = ['TR.SCRelationship.ScorgIDOut',
              'TR.SCRelationship', 
              'TR.SCRelationship.instrument', 
              'TR.SCRelationshipConfidenceScore'
             ]
    ties_data = rd.get_data(universe=ric_list, fields=fields)
    ties_df = ties_data[ties_data['Value Chains Relationship Confidence Score'] >= 0.5]
    ties_df = ties_df.iloc[:, 1:]
    print(ties_df)
    return ties_df

# %% [markdown]
# ## Step 4: Match Supplier-Buyer Names

# %%
def match_supplier_buyer_names(df_relationships, df_firms):
    name_dict = df_firms.set_index('TR.RIC')['TR.CommonName'].to_dict()
    df_relationships['SupplierName'] = df_relationships['TR.SCRelationship.instrument'].map(name_dict)
    df_relationships['BuyerName'] = df_relationships['TR.SCRelationship.ScorgIDOut'].map(name_dict)
    
    return df_relationships

# %% [markdown]
# ## Step 5: Expand the search if new firms are found

# %%
def expand_search(ric_list, df_relationships):
    new_firms = set(df_relationships['TR.SCRelationship.ScorgIDOut']).union(set(df_relationships['TR.SCRelationship.instrument']))
    new_firms = list(new_firms.difference(ric_list))
    
    return new_firms

# %% [markdown]
# ## Step 6: Export Data to CSV

# %%
def save_data(df_firms, df_relationships):
    df_firms.to_csv('firm_data.csv', index=False)
    df_relationships.to_csv('relationship_data.csv', index=False)

# %% [markdown]
# ## Step 7: Visualize Network

# %%
def visualize_network(df_relationships):
    G = nx.Graph()
    for _, row in df_relationships.iterrows():
        G.add_edge(row['SupplierName'], row['BuyerName'])
    plt.figure(figsize=(10, 6))
    nx.draw(G, with_labels=True, node_size=50, font_size=8)
    plt.show()

# %% [markdown]
# ## Step 8: Convert for R

# %%
def convert_to_r_format(df_relationships):
    adj_matrix = nx.to_numpy_array(nx.from_pandas_edgelist(df_relationships, 'SupplierName', 'BuyerName'))
    pd.DataFrame(adj_matrix).to_csv('network_matrix.csv', index=False)

# %% [markdown]
# ## Debugging section

# %%
'''
company_names = ["Intel Corp"]
ric_dict = get_ric_codes(company_names)
'''

# %% [markdown]
# ## Main execution code body

# %%
#company_names = ["Intel Corp", 
#                 "Texas Instruments Inc", 
#                 "SK Hynix Inc", 
#                 "Taiwan Semiconductor Manufacturing Co Ltd"
#                ]

ric_dict = get_ric_codes(company_names)
ric_list = list(ric_dict.values())

df_firms = fetch_firm_data(ric_list)
df_relationships = fetch_supplier_buyer_relationships(ric_list)
df_relationships = match_supplier_buyer_names(df_relationships, df_firms)

new_firms = expand_search(ric_list, df_relationships)
while new_firms and len(ric_list) < 1000:  # Limit expansion to 1000 firms
    ric_new_dict = get_ric_codes(new_firms)
    new_ric_list = list(ric_new_dict.values())
    ric_list.extend(new_ric_list)
    
    df_new_firms = fetch_firm_data(new_ric_list)
    df_new_relationships = fetch_supplier_buyer_relationships(new_ric_list)
    df_new_relationships = match_supplier_buyer_names(df_new_relationships, df_new_firms)
    
    df_firms = pd.concat([df_firms, df_new_firms], ignore_index=True)
    df_relationships = pd.concat([df_relationships, df_new_relationships], ignore_index=True)
    
    new_firms = expand_search(ric_list, df_new_relationships)

save_data(df_firms, df_relationships)
visualize_network(df_relationships)
convert_to_r_format(df_relationships)

# %%



