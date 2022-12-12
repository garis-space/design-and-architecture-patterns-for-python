from fastapi import HTTPException
from pydantic import BaseModel


# Define the model for a user
class User(BaseModel):
    username: str

    # Get the user from the fake database
    def get_user(self, fake_db: dict):
        if self.username in fake_db:
            return User(username=self.username)
        raise HTTPException(status_code=404, detail="User not found")
