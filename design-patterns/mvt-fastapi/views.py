from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import User


def user_view(app: FastAPI, templates: Jinja2Templates, fake_db: dict) -> FastAPI:

    # Define the user view
    @app.get("/user", response_class=HTMLResponse)
    async def user(request: Request, username: str):
        if username in fake_db:
            # Get the user from the database
            user = User(username=username)

            # Return the user template
            return templates.TemplateResponse("user.html", {"request": request, "user": user})
        raise HTTPException(status_code=404, detail="User not found")
