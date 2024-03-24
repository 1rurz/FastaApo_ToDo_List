from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from sqlalchemy.orm import Session
from .schemas import Record, RecordCreate, RecordUpdate
from core.models import db_helper
from .dependencies import record_by_id

router = APIRouter(tags=["/Records"])


@router.get("/", response_model=list[Record])
async def get_records(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_records(session=session)


@router.post(
    "/",
    response_model=Record,
    status_code=status.HTTP_201_CREATED,
)
async def create_record(
    record_in: RecordCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_record(session=session, record_in=record_in)


@router.get("/{record_id}/", response_model=Record)
async def get_record(
    record: Record = Depends(record_by_id),
):
    return record


@router.put("/{record_id}/")
async def update_record(
    record_update: RecordUpdate,
    record: Record = Depends(record_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_record(
        session=session,
        record=record,
        record_update=record_update,
    )


@router.delete(
    "/{record_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
async def delete_record(
    record: Record,
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> None:
    await crud.delete_record(session=session, record=record)
