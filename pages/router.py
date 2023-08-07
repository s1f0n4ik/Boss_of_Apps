from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates

from app_script import get_app_dict, get_win_dict, close_all, close_window

router = APIRouter(
    prefix="/pages",
    tags=["Pages"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/base")
def get_base_router(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})


@router.get("/base/apps")
async def get_apps_router(request: Request, result=Depends(get_app_dict)):
    return templates.TemplateResponse("apps.html", {"request": request, "result": result})


@router.get("/base/windows")
async def get_wins_router(request: Request, result=Depends(get_win_dict)):
    return templates.TemplateResponse("win.html", {"request": request, "result": result})


@router.get("/base/windows/close_all_window")
def get_close_all(request: Request, result=Depends(close_all)):
    return templates.TemplateResponse("close_all.html", {"request": request, "result": result})


# @router.get("/do_something")
# def do_something(request: Request):
#     data = request.form()
#     close_window(data)
#     return templates.TemplateResponse("win.html", {"request": request})

#
# @router.get("/base/windows/close_")
# async def get_apps_router(request: Request, result=Depends(close_window)):
#     return templates.TemplateResponse("win.html", {"request": request, "result": result})


# @router.get("/base/windows/close_window/{name}")
# async def get_user_item(request: Request, result=Depends(close_window)):
#     return templates.TemplateResponse("win.html", {"request": request, "result": result})



