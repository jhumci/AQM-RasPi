# %%

import pandas as pd
import seaborn as sns

# %%
#data = pd.read_csv("none.csv", index_col=False)

data = pd.read_csv("aggregatedcalibrationdata.csv", index_col=False)
# %%


data = data.dropna()
data = data.drop_duplicates()
data['date'] = pd.to_datetime(data['time'],unit='s')

data = data[data["date"]>'2023-02-08 09:49:44']

data = data


data.head()
data.to_csv("2023-02-08--clean-calibration-data.csv")
#%%

data[" Sensor ID"].unique()
# %%


#%%
#fig1 = sns.scatterplot(data = data, x = "date", y = "CO2")
#fig1.set(ylim=(1350, 1450))

# %%
#%%
#fig1 = sns.scatterplot(data = data, x = "date", y = "Pressure")

# %%

data.head()


# %%

import plotly.express as px
fig = px.scatter(data, x="date", y="CO2", color=" Sensor ID"
                 )
fig.show()

# %%