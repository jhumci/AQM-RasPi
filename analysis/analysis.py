# %%

import pandas as pd
import seaborn as sns

# %%

data = pd.read_csv("test_4A024.csv")
# %%

data.head()
# %%

data['date'] = pd.to_datetime(data['time'],unit='s')


#%%
fig1 = sns.scatterplot(data = data, x = "date", y = "CO2")
# %%
#%%
fig1 = sns.scatterplot(data = data, x = "date", y = "Pressure")

# %%
