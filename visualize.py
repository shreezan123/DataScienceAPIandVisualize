import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df['Value'] = df['Value'].str.replace(',','').astype(float)
first_criteria = df['year'].map(lambda x: x >= 2009)
second_criteria = df['year'].map(lambda x:x>=1989 and x<=2002)
new_df = df[first_criteria]
old_df = df[second_criteria]

def createPlots():
    new_df.plot.line(x = 'reference_period_desc',y = 'Value',title = '2009 and beyond')
    old_df.plot.line(x = 'reference_period_desc',y = 'Value',title = '1989 to 2002')
    plt.show()

def groupBy():
    print df.groupby('year')['Value'].mean()
    print df.groupby('year')['Value'].median()

if __name__ == '__main__':
    createPlots()
    groupBy()
