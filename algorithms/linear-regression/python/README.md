# Algorithms: Linear Regression

Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables.

In this example, the independent variable `x` is an array of four values, and the dependent variable `y` is an array of the corresponding values. The `LinearRegression` class from the `sklearn` library is used to fit a linear regression model to the training data by calling its `fit` method. Then, the model is used to make predictions on new data by calling its `predict` method.

#
### Create and activate a virtual environment (conda for macOS)
```bash
conda create -n patterns-and-algorithms python=3.10

conda activate patterns-and-algorithms
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run example
```bash
python main.py
```

### Run tests
```bash
pytest tests.py
```

### Clean up
```bash
conda deactivate

conda remove -n patterns-and-algorithms --all
```
