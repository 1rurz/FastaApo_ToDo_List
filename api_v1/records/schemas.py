from pydantic import BaseModel, ConfigDict


class RecordBase(BaseModel):
    name: str
    text: str


class RecordCreate(RecordBase):
    pass


class RecordUpdate(RecordCreate):
    pass


class RecordUpdatePartial(RecordCreate):
    name: str | None = None
    text: str | None = None


class Record(RecordBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
