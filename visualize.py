import pandas as pd

df = pd.read_csv('data.csv')
first_criteria = df['year'].map(lambda x: x > 2002)
second_criteria = df['year'].map(lambda x:x>=1989 and x<=2002)

old_df = df[first_criteria]
new_df = df[second_criteria]
