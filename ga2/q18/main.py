from fastapi import FastAPI, File, UploadFile, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import io

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["POST"])

TOKEN = "ztxngbrpcnlivtla"

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    x_upload_token_5088: str = Header(None)
):
    if x_upload_token_5088 != TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    content = await file.read()
    if len(content) > 87 * 1024:
        raise HTTPException(status_code=413, detail="Payload Too Large")
    
    if not any(file.filename.endswith(ext) for ext in [".csv", ".json", ".txt"]):
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    if file.filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(content))
        return {
            "email": "24f2001614@ds.study.iitm.ac.in",
            "filename": file.filename,
            "rows": len(df),
            "columns": list(df.columns),
            "totalValue": float(df["value"].sum()) if "value" in df else 0,
            "categoryCounts": df["category"].value_counts().to_dict() if "category" in df else {}
        }
    return {"status": "ok", "email": "24f2001614@ds.study.iitm.ac.in"}
