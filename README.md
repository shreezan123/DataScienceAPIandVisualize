# Group Project  - *Getting Data from API, Analyzing and Visualizing Data*


## Part 1: Making an API GET Request and saving to a csv file

**Requests** library was used to make a GET request to the API and the result was stored in a csv using **csv** library. A data dictionary of following key value pairs was created at first:
```
param_dict = {'key':'2ECEF0FA-03C3-33EA-8410-658A77DA3BA6','commodity_desc':'TURKEYS','year__GE':'1989','state_alpha':'VA','short_desc':'TURKEYS, YOUNG, SLAUGHTER, FI - SLAUGHTERED, MEASURED IN HEAD','format':'csv'}
```
and passed API request as:
```
r = requests.get("https://quickstats.nass.usda.gov/api/api_GET/?",params = param_dict)

```
Then each line of the response ```r``` was iterated through and stored in a csv file using **csv** library as below:
```
with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    reader = csv.reader(r.text.splitlines())
    for row in reader:
        writer.writerow(row)
```
## Part 2: Creating dataframe and  Visualizing data

**pandas** library was used to create dataframe and to visualize data. The csv file contained 292 rows and 39 columns. Because the dataframe did not contain data from 2002-2009, it was separated into 2 parts the one containing data from 1989-2002 and 2009-2018. This was done using lambda function to create two criteria as:
```
df = pd.read_csv('data.csv')
first_criteria = df['year'].map(lambda x: x > 2002)
second_criteria = df['year'].map(lambda x:x>=1989 and x<=2002)
```
Then two data frames for these old and new data were created as:
```
old_df = df[first_criteria]
new_df = df[second_criteria]
```
### Visuazling two different types of data

Line plot was used to visualize these data. A challenge was to change datatype of **Value** column to float type which initially was in **Object** type with commas in between. So the commas were replaced by empty spaces. Then ```astype``` function was used to convert string datatype to float
```
df['Value'] = df['Value'].str.replace(',','').astype(float)

```
Line plot was made by following code:
```
new_df.plot.line(x = 'reference_period_desc',y = 'Value')
old_df.plot.line(x = 'reference_period_desc',y = 'Value')
plt.show()
```
### Following plots were observed:
<img src = 'https://i.imgur.com/2Bf0N8R.png' width = "500" height = "500">

This is a plot observed for 2009 and beyond. The line chart suggests that the pattern is consistently repeating for this period. Upon looking at the data, the peak portion in the plot is for the annual value. So the annual value for each period is almost the same for these years.    

<img src = 'https://i.imgur.com/LMXT5HN.png' width = "500" height = "500">

This is a plot observed for 1989 to 2009. The plot shows that the value for each month is "fairly" consistent but it is slightly decreasing towards the end i.e. 1989. 
The value of 1,721,000 is the lowest for February 1989, which can also be seen in the dip of the line chart. 

### Using aggregation function with groupby

Mean and median were two aggregation functions that were used. First the columns were grouped by 'Year' and their mean and median were found by following lines of code
```
print df.groupby('year')['Value'].mean()
print df.groupby('year')['Value'].median()
```
The results came out to be:<br>
**Mean**<br>
1989    2.202583e+06<br>
1990    2.551500e+06<br>
1991    2.561833e+06<br>
1992    2.835500e+06<br>
1993    3.040000e+06<br>
1994    3.148583e+06<br>
1995    3.086417e+06<br>
1996    3.203833e+06<br>
1997    2.997417e+06<br>
1998    2.915400e+06<br>
1999    3.094417e+06<br>
2000    3.025700e+06<br>
2001    5.703231e+06<br>
2002    5.975900e+06<br>
2003    3.524800e+07<br>
2008    2.902500e+07<br>
2009    4.293692e+06<br>
2010    4.282000e+06<br>
2011    4.240615e+06<br>
2012    4.194154e+06<br>
2013    4.034923e+06<br>
2014    4.072308e+06<br>
2015    4.108462e+06<br>
2016    4.181846e+06<br>
2017    4.112154e+06<br>
2018    2.248200e+06<br>

**Median**<br>
1989     2251500.0<br>
1990     2518500.0<br>
1991     2562500.0<br>
1992     2808500.0<br>
1993     3060000.0<br>
1994     3130000.0<br>
1995     3162500.0<br>
1996     3178500.0<br>
1997     3021000.0<br>
1998     3030000.0<br>
1999     3087000.0<br>
2000     2990000.0<br>
2001     3076000.0<br>
2002     2966000.0<br>
2003    35248000.0<br>
2008    29025000.0<br>
2009     2315000.0<br>
2010     2388000.0<br>
2011     2306000.0<br>
2012     2218000.0<br>
2013     2234000.0<br>
2014     2214000.0<br>
2015     2269000.0<br>
2016     2267000.0<br>
2017     2303000.0<br>
2018     2281000.0<br>

## Part 3: Fitting Data

### Fitting Data for January to October 2017

Different criteria were created to create a dataframe for the months of January-October.
```
first_criteria = df['year'].map(lambda x:x == 2017)
second_criteria = df['freq_desc'].map(lambda x: x != 'ANNUAL')
third_criteria = df['reference_period_desc'].map(lambda x: x!= 'DEC' and x!= 'NOV')
```
Then the dataframe was created
```
fit_df = df[first_criteria][second_criteria][third_criteria]
```
As this is a linear regressor, there should be independent and dependent variable. Here Value is a dependent variable which depends on independent variable Month (reference_period_desc).  ```sklearn.linear_model``` library is used to fit the data and create a best line that aims to capture most of the data. The X and Y axes for fitting the data is created as: 
```
X=[0,1,2,3,4,5,6,7,8,9]
X = np.array(X).reshape((len(X),1))
y=fit_df['Value'].values
```
Then ```LinearRegression``` library is used to fit the data as:
```
model = LinearRegression()
model.fit(X,y)
```
Then data is plotted in the following way to create a linear regression model:
```
fit_df.plot(x = 'reference_period_desc',y = 'Value',title = 'JAN to OCT 2D plot',style = 'o')
plt.plot(X,model.predict(X),color='k')
plt.show()
```
The plot came as follows. The image is zoomed in so it might not look like the regression line captures most of the data but in reality this is the best fitting model.
<img src = 'https://images2.imgbox.com/d2/a6/bvSbWvQw_o.png' width = "500" height = "500">

### Predicting value for November

The ```predict``` function was used to predict value for November. The value for november came out to be: ***2373133.33333333***
The code is as follows:
```
global predictedValue
predictedValue = model.predict([[10]])
print "Prediction for the month of November is: ", predictedValue
```

### Computing absolute error

The absolute error was simply calculated using native ```abs``` function in Python. It came out to be: ***41133.33333333***  
```
absolute_error = abs(predictedValue-2332000)
print "The absolute error is: ",absolute_error
```

### Computing coefficient of determination/ R^2

R^2 was calculated using score function as follows: The value came out to be: 0.16351145981204795
```
print "R squared score is: ", model.score(X,y)

```

### Fitting Data for January to December 2017

The approach for this is similar to the one mentioned above. Several criteria were created and dataframe was created by the following lines of code:
```
forth_criteria = df["year"].map(lambda x:x == 2017)
fifth_criteria = df["freq_desc"].map(lambda x:x != 'ANNUAL')
df_2017 = df[forth_criteria][fifth_criteria]
```
Then X and Y variables for the regressor were created as: 
```
X=[0,1,2,3,4,5,6,7,8,9,10,11]
X = np.array(X).reshape((len(X),1))
y = df_2017['Value'].values
```
The data was fitted using ```LinearRegression``` function as:
```
df_2017.plot(x = 'reference_period_desc',y = 'Value',title = '2D plot for 2017',style = 'o')
model = LinearRegression()
model.fit(X,y)
plt.plot(X,model.predict(X),color='k')
plt.show()
```
The plot came as follows. The image is zoomed in so it might not look like the regression line captures most of the data but in reality this is the best fitting model.
<img src = "https://images2.imgbox.com/eb/a8/29sGWTdA_o.png">

## Challenges

* Learning how requests library works in python and how to pass parameters as key-valued pairs
* Learning how to index dataframe by creating a lambda function and temporary boolean column (which I have named as **first_criteria** and **second_criteria**)
* Using logical criteria in dataframe using *map* in Python to create different dataframe based on **Year** field. 
* Learning to use aggregation function (mean and median) with group by in Python as I only knew how to do this in mySQL.
