import os
import shutil
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to upload API"}


@app.post("/")
async def upload_file(file: UploadFile = File(...)):
    filepath = os.path.join("uploads", file.filename)
    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "content_type": file.content_type}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8060)
