import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data.csv')
first_criteria = df['year'].map(lambda x: x > 2002)
second_criteria = df['year'].map(lambda x:x>=1989 and x<=2002)
new_df = df[first_criteria]
old_df = df[second_criteria]

new_df['Value'] = new_df['Value'].str.replace(',', '').astype(float)
old_df['Value'] = old_df['Value'].str.replace(',', '').astype(float)

new_df.plot.line(x = 'reference_period_desc',y = 'Value')
old_df.plot.line(x = 'reference_period_desc',y = 'Value')
plt.show()
