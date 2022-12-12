# Algorithms: Linear Regression

Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables.

In this example, a `LinearRegressionModel` class is defined that extends `django.db.models.Model`. This class has two fields, `x` and `y`, that are used to store the training data for the model. The `fit` method is used to fit a `LinearRegression` model to the training data, and the `predict` method is used to make predictions on new data using the fitted model.

In the `views.py` file, a `predict` view is defined that retrieves a `LinearRegressionModel` instance from the database and uses its predict method to make predictions on some input data. The predictions are then passed to a template, which can be used to display them to the user.

The `predictions` variable is passed to the template from the view and `predictions` variable is a list of the predicted values, and the `for` loop is used to iterate over the list and display each value in a li element.

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
# Run migrations
python manage.py migrate

# Load data into database (SQLite) from fixtures
python manage.py loaddata example/fixtures/linear-regression.json

# Run server
python manage.py runserver
```

### Run tests
```bash
python manage.py test
```

### Clean up
```bash
conda deactivate

conda remove -n patterns-and-algorithms --all
```
