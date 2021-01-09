from enum import IntEnum, Enum
from fastapi import  FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .upscaler import Upscaler
from .image import Image

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Scale(IntEnum):
    x2 = 2
    x3 = 3
    x4 = 4

class ImageForm(BaseModel):
    img: str
    upscale: Scale

@app.post("/upscale")
async def upscale(form: ImageForm):
    img = Image(form.img)
    upscaler = Upscaler(scale=form.upscale.value)
    img_upscaled = upscaler.upscale(img)
    return {
        'upscaled': f'{img.raw_header},{img_upscaled}'
    }
