from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from views import user_view


# Define a fake database
fake_db = {
    "foo": {"id":1, "username": "foo"},
    "bar": {"id":2, "username": "bar"},
}

# Define the FastAPI app
app = FastAPI()

# Define the templates
templates = Jinja2Templates(directory="templates")

# Define the view for handling user
user_view = user_view(app, templates, fake_db)
