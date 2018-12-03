from visualize import df
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

first_criteria = df['year'].map(lambda x:x == 2017)
second_criteria = df['freq_desc'].map(lambda x: x != 'ANNUAL')
third_criteria = df['reference_period_desc'].map(lambda x: x!= 'DEC' and x!= 'NOV')
fit_df = df[first_criteria][second_criteria][third_criteria]
X=[0,1,2,3,4,5,6,7,8,9]
X = np.array(X).reshape((len(X),1))
y=fit_df['Value'].values
model = LinearRegression()
model.fit(X,y)

#Part 3a
def fitJantoOct():
    fit_df.plot(x = 'reference_period_desc',y = 'Value',title = 'JAN to OCT 2D plot',style = 'o')
    plt.plot(X,model.predict(X),color='k')
    plt.show()

#Part 3b
def predictNovember():
    global predictedValue
    predictedValue = model.predict([[10]])
    print "Prediction for the month of November is: ", predictedValue

#Part 3c
def calculateAbsError():
    absolute_error = abs(predictedValue-2332000)
    print "The absolute error is: ",absolute_error

#Part 3d
def calculateRSq():
    print "R squared score is: ", model.score(X,y)

#Part 3e
def fitAll():
    forth_criteria = df["year"].map(lambda x:x == 2017)
    fifth_criteria = df["freq_desc"].map(lambda x:x != 'ANNUAL')
    df_2017 = df[forth_criteria][fifth_criteria]
    X=[0,1,2,3,4,5,6,7,8,9,10,11]
    X = np.array(X).reshape((len(X),1))
    y = df_2017['Value'].values
    df_2017.plot(x = 'reference_period_desc',y = 'Value',title = '2D plot for 2017',style = 'o')
    model = LinearRegression()
    model.fit(X,y)
    plt.plot(X,model.predict(X),color='k')
    plt.show()

if __name__ == '__main__':
    fitJantoOct()
    predictNovember()
    calculateAbsError()
    calculateRSq()
    fitAll()
