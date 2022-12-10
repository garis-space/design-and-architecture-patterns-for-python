# Design Pattern: Model-View-Template (MVT)

Model-View-Template (MVT) is a common design pattern for web applications, where the model represents the data being stored and manipulated, the view represents the user interface, and the template represents the layout and structure of the user interface. This pattern is commonly used in Django. Here is an example of how MVT can be implemented.

In this example, we have defined a model for the user, with a field for the username. We also defined a view to handle user accounts, which retrieves the user from the database and renders a template with the user's information.

Finally, we defined a template for displaying the user, which uses the user object provided by the view to display the user's name. This is an example of how MVT can be used to separate the data model, user interface and application logic in a web application.

#
### Create and activate a virtual environment
```bash
# virtualenv, pyenv, or conda
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run example
```bash
uvicorn main:app --reload
```

### Get user data
```bash
curl http://localhost:8000/user?username=foo
```

### Run tests
```bash
pytest tests.py
```
