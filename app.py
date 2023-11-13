from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="./templates")


class RegistrationForm(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/success", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("success.html", {"request": request})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
