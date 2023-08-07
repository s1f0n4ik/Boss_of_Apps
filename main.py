from fastapi import FastAPI, Request, Form
from fastapi_users import FastAPIUsers
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import uvicorn

from app_script import close_window
from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from pages.router import router as router_pages
from operations_win.router import router as router_oper


origins = ["http://localhost:8000"]


app = FastAPI(title="Boss of Apps")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router_pages)
app.include_router(router_oper)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/do_something")
def do_something(data: str = Form(...)):
    close_window(data)
    return {"Программа": data, "Состояние": "closed"}


def server():
    uvicorn.run(app)


if __name__ == "__main__":
    server()
