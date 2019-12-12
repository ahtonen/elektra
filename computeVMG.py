#%%
import pandas as pd
import numpy as np

pd.set_option('precision', 3)

t = pd.read_csv("Guyader-gastronomieV1.pol", sep='\t')
t.set_index('TWA', inplace=True)
#%%
# VMGs
vmgs = pd.DataFrame(index=t.index, columns=t.columns)
#%%
# Compute VMGs for given TWA and TWS
for twa, speeds in t.iterrows():
    speeds_vmg = speeds.values*np.abs(np.cos(np.deg2rad(twa)))
    #print(twa, speeds_vmg)
    vmgs.loc[twa,:] = speeds_vmg
# %%
# Create 90% polars for ARC
#pol = t.applymap(lambda x: 0.9*x)

# Export VMGs and polars to html files (downwind only)
t.iloc[9:-1,:].to_html("ARC-Elektra-polars.html", justify='left')
vmgs.iloc[9:-1,:].to_html("ARC-Elektra-vmgs.html", justify='left')
print("Polars and VMGs exported to html files.")
# %%
