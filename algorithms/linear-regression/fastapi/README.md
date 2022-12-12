# Algorithms: Linear Regression

Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables.

In this example, a `FastAPI` object is created and a `LinearRegression` model is fit to the training data. A route is defined using the `@app.get` decorator, which specifies the URL path that the route will handle. When a GET request is made to the specified path, the `predict` function is called, which uses the linear regression model to make predictions on the input data `x` and returns the predictions.

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

### Get user data
```bash
curl -X GET "http://localhost:8000/predict/4"
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
