from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from auth.database import get_async_session
from models.models import roles
from app_script import get_app_dict

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/get_process")
async def get_running_process(session: AsyncSession = Depends(get_async_session)):
    query = select(roles).where(roles.c.status == "running")
    result = await session.execute(query)
    return result.all()


@router.post("/add_process")
async def add_running_process(session: AsyncSession = Depends(get_async_session)):
    data = get_app_dict()
    for value in data.values():
        statement = insert(roles).values(id=value[3], name=value[0], status=value[1], create_time=value[2])
        await session.execute(statement)
        await session.commit()
    return {"status": "succes"}
