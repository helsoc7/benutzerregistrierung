from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, FlashResponse
from pydantic import BaseModel

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class RegistrationForm(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str


@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.post("/register", response_class=HTMLResponse)
async def register(request: Request, form: RegistrationForm = Form(...)):
    # Add form validation logic here (e.g., email validation)
    # For simplicity, the validation is not implemented in this example.
    flash_message = "Registration successful! Welcome, {}!".format(form.firstname)
    return FlashResponse(templates.TemplateResponse("register.html", {"request": request}), flash=flash_message)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
