import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_table('input.csv', sep=",", header=0, index_col=None)
corr = df.corr()
print(corr)

corrmat = df.corr()

# Create the heatmap with dendrograms
cg = sns.clustermap(corrmat, cmap ="RdBu_r", linewidths = 0.1,figsize=(20,20))

# Rotate the y-axis labels
plt.setp(cg.ax_heatmap.yaxis.get_majorticklabels(), rotation = 0)

# Save the trimmed dataframe as a CSV file
corrmat.to_csv('input_calculated.csv', sep="\t") 
