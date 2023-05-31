import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split

# Read the CSV file
df = pd.read_csv('Journals.csv')

# Define the feature and target variables
features = ['pages', 'citations', 'subs']
best_feature = None
best_r2 = 0
best_mse = float('inf')

# Iterate through each feature
for feature in features:
    X = df[[feature]]
    y = df['price']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions using the trained model
    y_pred = model.predict(X_test)

    # Calculate R-squared and MSE scores
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    # Check if current feature is better than the previous best
    if r2 > best_r2:
        best_r2 = r2
        best_mse = mse
        best_feature = feature
    elif r2 == best_r2 and mse < best_mse:
        best_mse = mse
        best_feature = feature

# Print the best feature and its corresponding R-squared and MSE scores
print(f"Best Feature: {best_feature}")
print(f"R-squared: {best_r2:.2f}")
print(f"MSE: {best_mse:.2f}")
