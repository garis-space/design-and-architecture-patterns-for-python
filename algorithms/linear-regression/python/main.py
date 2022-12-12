import numpy as np
from sklearn.linear_model import LinearRegression


# Training data
x = np.array([[1], [2], [3], [4]])
y = np.array([1, 2, 3, 4])

# Fit the model
model = LinearRegression().fit(x, y)

# Make predictions
predictions = model.predict([[5], [6], [7], [8]])

# Print the predictions
print(predictions)

# Output
# [5. 6. 7. 8.]
