import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
g = 0

data = pd.read_csv("new.csv")
data.head()

x = data[["LotArea"]]
y = data["New"]

model = LinearRegression()
model.fit(x, y)



prediction = model.predict([[50000]])
print("The predicted price of a house with 200" + "square feet is $" + str(prediction[0]))



