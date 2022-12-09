from pydantic import BaseModel


# Define the model for a user
class User(BaseModel):
    username: str
