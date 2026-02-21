from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["GET"])
@app.get("/api")
def get_students(class_name: list[str] = Query(None, alias="class")):
    df = pd.read_csv("students.csv")
    if class_name:
        df = df[df["class"].isin(class_name)]
    return {"students": df.to_dict(orient="records")}
