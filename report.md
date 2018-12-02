# Group Project  - *Using API, Analyzing and Visualizing Data*


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
new_df['Value'] = new_df['Value'].str.replace(',', '').astype(float)
old_df['Value'] = old_df['Value'].str.replace(',', '').astype(float)
```
Line plot was made by following code:
```
new_df.plot.line(x = 'reference_period_desc',y = 'Value')
old_df.plot.line(x = 'reference_period_desc',y = 'Value')
plt.show()
```
Following plots were observed:
<img src = 'https://i.imgur.com/2Bf0N8R.png' width = "300" height = "300">

This is a plot observed for 2009 and beyond. The line chart suggests that the pattern is consistently repeating for this period. Upon looking at the data, the peak portion in the plot is for the annual value. So the annual value for each period is almost the same for these years.    

<img src = 'https://i.imgur.com/LMXT5HN.png' width = "300" height = "300">

This is a plot observed for 1989 to 2009. The plot shows that the value for each month is "fairly" consistent but it is slightly decreasing towards the end i.e. 1989. 
The value of 1,721,000 is the lowest for February 1989, which can also be seen in the dip of the line chart. 


## Challenges

* Learning how requests library works in python and how to pass parameters as key-valued pairs
* Learning how to index dataframe by creating a lambda function and temporary boolean column (which I have named as **first_criteria** and **second_criteria**)
