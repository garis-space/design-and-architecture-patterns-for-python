from django.db import models
import numpy as np
from sklearn.linear_model import LinearRegression


class LinearRegressionModel(models.Model):
    # Training data
    x = models.TextField()
    y = models.TextField()

    # Model
    model = models.TextField()

    # Training
    def train(self):
        # Convert x and y to numpy arrays
        x = np.array(self.x.split(',')).astype(np.float)
        y = np.array(self.y.split(',')).astype(np.float)

        # Train model
        model = LinearRegression()
        model.fit(x.reshape(-1, 1), y)

        # Save model
        self.model = model

    # Prediction
    def predict(self, x):
        # Convert x to numpy array
        x = np.array(x.split(',')).astype(np.float)

        # Predict
        y = self.model.predict(x.reshape(-1, 1))

        # Return prediction
        return y

    # String representation
    def __str__(self):
        return self.x + ' ' + self.y
