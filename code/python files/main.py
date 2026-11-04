import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel

from spam_prediction import predict
from fastapi.middleware.cors import CORSMiddleware


class pred(BaseModel):
    text: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/predict")
def pm(message: pred):
    return predict(message.text)


uvicorn.run(app, host="0.0.0.0", port=8000)