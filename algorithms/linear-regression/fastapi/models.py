import numpy as np
from sklearn.linear_model import LinearRegression


# Training data
def get_training_data():
    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape((-1, 1))
    y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
    return x, y

# Model
def get_predict(x: int):
    # Convert to numpy array
    x = np.array(x).reshape((-1, 1))

    # Train model
    model = LinearRegression()

    # Fit model
    model.fit(*get_training_data())

    # Predict
    predictions = model.predict(x)

    # Return predictions
    return predictions.tolist()
