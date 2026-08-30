from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.staticfiles import StaticFiles
import os
import shutil

app = FastAPI()

# Directory to store uploaded files
UPLOAD_DIRECTORY = "uploads"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# Mount the static files directory to serve uploaded files
#URL: http://localhost:8000/files/<filename>
app.mount("/files", StaticFiles(directory=UPLOAD_DIRECTORY), name="uploads")

# Upload file API endpoint
@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    filename = file.filename
    file_location = os.path.join(UPLOAD_DIRECTORY, filename)

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        "message": "File uploaded successfully",
        "filename": filename,
        "url": f"http://127.0.0.1:8000/files/{filename}"
    }

#Step 4: Get file API endpoint
@app.get("/files/{filename}")
def get_file(filename: str):
    file_path = os.path.join(UPLOAD_DIRECTORY, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return {
        "file_url": f"http://127.0.0.1:8000/files/{filename}"
    }