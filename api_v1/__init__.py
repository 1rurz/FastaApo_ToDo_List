from fastapi import APIRouter

from .records.views import router as record_router

router = APIRouter()
router.include_router(router=record_router, prefix="/records")
