import uvicorn
from fastapi import FastAPI
from models import get_predict


# Define the FastAPI app
app = FastAPI()

@app.get("/predict/{x}", response_model=list)
async def predict(x: int):
    # Make predictions
    return get_predict(x)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
