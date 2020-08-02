import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
import math

scale = StandardScaler()

df = pandas.read_csv("cars.csv")

X = df[['Weight', 'Volume']]
Y = df['CO2']


train_length_x = math.floor(.8*len(X))
train_length_y = math.floor(.8*len(Y))

train_x = X[:train_length_x]
train_y = Y[:train_length_y]

test_x = X[train_length_x:]
test_y = Y[train_length_y:]

rg = linear_model.LinearRegression()
rg.fit(train_x, train_y)

r2 = r2_score(test_y, rg.predict(test_x))

print(r2)



