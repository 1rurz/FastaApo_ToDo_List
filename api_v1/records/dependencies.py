from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Record
from . import crud


async def record_by_id(
    record_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Record:
    record = await crud.get_record(session=session, record_id=record_id)
    if record is not None:
        return record
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Record{record_id} not found!",
    )
