import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('medical_examination.csv')

df['bmi'] = df['weight']/((df['height']/100)**2)
df['overweight'] = np.where(df['bmi'] > 25, 1, 0)
df['cholesterol'] = np.where(df['cholesterol'] >= 1, 1, 0)
df['gluc'] = np.where(df['gluc'] >= 1, 1, 0)


