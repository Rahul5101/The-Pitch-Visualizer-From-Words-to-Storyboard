from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from apps.text_processing import segment_text, engineer_prompts
from apps.image_gen import generate_images

app = FastAPI()
templates = Jinja2Templates(directory="apps/templates")
app.mount("/static", StaticFiles(directory="apps/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("formating.html", {"request": request, "segments": None})

@app.post("/generate", response_class=HTMLResponse)
async def generate_storyboard(request: Request, input_text: str = Form(...), style: str = Form("digital art")):
    segmented_text = segment_text(input_text)
    prompts = engineer_prompts(segmented_text, style=style)
    images = generate_images(prompts)
    format = list(zip(segmented_text, images))
    return templates.TemplateResponse("foramting.html", {"request": request, "segments": format, "input_text": input_text, "style": style})
