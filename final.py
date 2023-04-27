import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

data_path = Path('Data/')
df_meteo = pd.read_pickle(Path(data_path, 'ec_meteo/lic_meteo'))
df_meters = pd.read_pickle(Path(data_path, 'ec_meters/lic_meters'))
df_nwp = pd.read_pickle(Path(data_path, 'ec_nwp/lic_nwp'))


# Plot the e_pos measure in the df_meters dataset
e_pos_cols = [col for col in df_meters.columns if 'e_pos' in col]
# Plot the e_neg measure in the df_meters dataset
e_neg_cols = [col for col in df_meters.columns if 'e_neg' in col]


df_meteo.plot(figsize=(15, 6), alpha=0.8)


# Plot the e_pos columns against the DataFrame's index
df_meters[e_pos_cols].plot(figsize=(15, 6), alpha=0.8)
plt.xlabel('Time')
plt.ylabel('e_pos')
plt.legend(loc='upper right', ncol=2, fontsize=8)
plt.show()




# Plot the e_neg columns against the DataFrame's index
df_meters[e_neg_cols].plot(figsize=(15, 6), alpha=0.8)
plt.xlabel('Time')
plt.ylabel('e_neg')
plt.legend(loc='upper right', ncol=2, fontsize=8)
plt.show()

df = df_meters.copy()
df[e_neg_cols] = -df[e_neg_cols]
# Plot the e_neg columns against the DataFrame's index
df["PCC"].plot(figsize=(15, 6), alpha=0.8)
plt.xlabel('Time')
plt.ylabel('e_neg')
plt.legend(loc='upper right', ncol=2, fontsize=8)
plt.show()