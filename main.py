import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('medical_examination.csv')

df['bmi'] = df['weight']/((df['height']/100)**2)
df['overweight'] = np.where(df['bmi'] > 25, 1, 0)
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

df_cat = pd.melt(df, id_vars=('cardio'), value_vars=('cholesterol', 'gluc', 'smoke','alco', 'active', 'overweight'))
df_cat['total'] = 0
df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio').figure
fig.savefig("cardio.png")