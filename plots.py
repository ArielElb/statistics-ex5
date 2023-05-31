import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read the CSV file
df = pd.read_csv('Journals.csv')

# Define the feature and target variables
X = df['pages'].values.reshape(-1, 1)
y = df['price']

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X, y)

# Get the coefficients
a = model.intercept_
b = model.coef_[0]

# Make predictions using the trained model
y_pred = model.predict(X)

# Create a scatter plot
plt.scatter(X, y, color='b', label='Actual')
plt.plot(X, y_pred, color='r', label='Regression Line')
plt.xlabel('Pages')
plt.ylabel('Price')
plt.title('Scatter Plot with Regression Line')
plt.legend()

# Print the coefficients
print("Coefficients:")
print("a =", a)
print("b =", b)

# Show the plot
plt.show()