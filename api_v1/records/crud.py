from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine import Result
from sqlalchemy import select

from core.models import Record
from .schemas import RecordCreate, RecordUpdate, RecordUpdatePartial


async def get_records(session=AsyncSession) -> list[Record]:
    stmt = select(Record).order_by(Record.id)
    result: Result = await session.execute(stmt)
    records = result.scalars().all()
    return list(records)


async def get_record(session: AsyncSession, record_id: int) -> Record | None:
    return await session.get(Record, record_id)


async def create_record(session: AsyncSession, record_in: RecordCreate) -> Record:
    record = Record(**record_in.model_dump())
    session.add(record)
    await session.commit()
    return record


async def update_record(
    session: AsyncSession,
    record: Record,
    record_update: RecordUpdate | RecordUpdatePartial,
    partial: bool = True,
) -> Record:
    for name, value in record_update.model_dump(exclude_unset=partial).items():
        setattr(record, name, value)
    await session.commit()


async def delete_record(session: AsyncSession, record: Record) -> None:
    await session.delete(record)
    await session.commit()
