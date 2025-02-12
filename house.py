import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
#1.1 Load the provided .CSV file into a Pandas Data Frame.
df = pd.read_csv(
    r'_YOUR_LOCATION_\house_data.csv')
#1.2 Preprocess the data, See rows with missing values
data[data.isnull().any(axis=1)]

columns = ['bedrooms', 'bathrooms', 'floors', 'yr_built','sq_leng','price']
df = df[columns]

#2.1 Split the dataset 
X = df.iloc[:, 0:5]
y = df.iloc[:, 5:]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

#2.2 Build a regression model
lr = LinearRegression()
lr.fit(X_train, y_train)

# Plotting the heatmap of correlation between features
# Create a heatmap using plotly
#fig = px.density_heatmap(df, x="bedrooms", y="bathrooms", z="price")

# Save the heatmap as an HTML file
#fig.write_html('templates/heatmap.html')

#3.1 Create a Flask web application
pickle.dump(lr, open('model.pkl', 'wb'))

#3.2 Use web development tools/scripting - html,css