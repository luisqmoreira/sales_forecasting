import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle

new_mg = pd.read_csv('/Users/luismoreira/Downloads/clean_sales.csv')

model = linear_model.LinearRegression()

x = new_mg.drop(['size',"Product","Variant", "Unnamed: 0"], axis = 1)# independent variable(s)

y = new_mg['size']

model.fit(x,y)

model.score(x,y)

pkl_filename = 'sales_model.pkl'

with open(pkl_filename, 'wb') as file:
    pickle.dump(model, file)