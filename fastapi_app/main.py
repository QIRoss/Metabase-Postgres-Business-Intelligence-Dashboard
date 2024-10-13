from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "postgresql://your_user:your_password@postgres:5432/your_db_name"
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI in a Docker container"}

@app.get("/data")
def get_data():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM your_table"))
        return [dict(row._mapping) for row in result]
