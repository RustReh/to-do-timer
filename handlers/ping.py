from fastapi import APIRouter
from settings import Settings

router = APIRouter(prefix='/ping', tags=['ping-app, ping-db'])

@router.get('/db')
async def ping_db():
    settings = Settings()
    return settings.GOOGLE_TOKEN_ID


@router.get('/app')
async def ping_app():
    return {'text': 'app is working'}