import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('medical_examination.csv')

df['bmi'] = df['weight']/((df['height']/100)**2)
df['overweight'] = np.where(df['bmi'] > 25, 1, 0)
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)
df = df[df['ap_lo'] < df['ap_hi']]

df_cat = pd.melt(df, id_vars=('cardio'), value_vars=('cholesterol', 'gluc', 'smoke','alco', 'active', 'overweight'))
df_cat['total'] = 0
df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
fig = sns.catplot(data=df_cat, x='variable', y='total', hue='value', kind='bar', col='cardio').figure
fig.savefig("cardio.png")

df_heat = df[(df['height'] >= df['height'].quantile(0.025)) &
                (df['height'] <= df['height'].quantile(0.975)) &
                (df['weight'] >= df['weight'].quantile(0.025)) &
                (df['weight'] <= df['weight'].quantile(0.975))]
corr = df_heat.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", cmap="icefire", cbar_kws={"shrink": 0.5}, linewidths=0.5)
fig.savefig('heatmap.png')