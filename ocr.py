from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

import io
import cv2
import base64
import pytesseract
import numpy as np

class Image(BaseModel):
    data: str

app = FastAPI()

def recognize(base64_data):
    # convert base64_data to the processable image first
    nparr = np.fromstring(base64.b64decode(base64_data), np.uint8)
    img = cv2.cvtColor(cv2.imdecode(nparr, cv2.IMREAD_ANYCOLOR), cv2.COLOR_BGR2RGB)
    _, img_binary = cv2.threshold(img,100, 255, cv2.THRESH_BINARY)

    # process on the image and return recognized text
    return pytesseract.image_to_string(img_binary)

@app.post("/ocr/")
async def ocr_item(img: Image):
    return recognize(img.data)