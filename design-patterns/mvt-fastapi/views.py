from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import User


def user_view(app: FastAPI, templates: Jinja2Templates, fake_db: dict) -> FastAPI:

    # Define the user view
    @app.get("/user", response_class=HTMLResponse)
    async def user(request: Request, username: str):
        # Get the user from the database
        user = User(username=username).get_user(fake_db)

        # Return the user template
        return templates.TemplateResponse("user.html", {"request": request, "user": user})
