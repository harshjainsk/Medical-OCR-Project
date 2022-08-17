from fastapi import FastAPI, Form, UploadFile, File
import uvicorn
from extractor import extract
import uuid


app = FastAPI()


@app.post("/extract_from_doc")
def extract_from_doc(
        file_format: str = Form(...),
        file: UploadFile = File(...)
):
    content = file.file.read()

    file_path = "../uploads/" + str(uuid.uuid4()) + ".pdf"

    with open(file_path, "wb") as f:
        f.write(content)

    data = extract(file_path, file_format)

    return data


if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
