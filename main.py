from fastapi import FastAPI
import random
from mangum import Mangum

app = FastAPI()

app = FastAPI()
handler = Mangum(app)


@app.get("/random")
def get_random_number():
    random_number = random.randint(1, 100)  # Generates a random number between 1 and 100
    return {"random_number": random_number}