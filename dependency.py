from fastapi import Depends, Request, security, Security, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db_session
from cache import get_redis_connection
from exception import TokenExpiredException, TokenNotCorrectException
from repository import TaskRepository, TaskCache, UserRepository
from service import TaskService, UserService, AuthService
from settings import Settings


async def get_task_repository(db_session: AsyncSession = Depends(get_db_session)) -> TaskRepository:
    return TaskRepository(db_session)


async def get_task_repository_cache() -> TaskCache:
    redis_connection = get_redis_connection()
    return TaskCache(redis_connection)


async def get_task_service(
        task_repository: TaskRepository = Depends(get_task_repository),
        task_cache: TaskCache = Depends(get_task_repository_cache)
) -> TaskService:
    return TaskService(
        task_repository=task_repository,
        task_cache=task_cache
    )


async def get_user_repository(db_session: AsyncSession = Depends(get_db_session)) -> UserRepository:
    return UserRepository(db_session=db_session)


async def get_auth_service(user_repository: UserRepository = Depends(get_user_repository)) -> AuthService:
    return AuthService(user_repository=user_repository, settings=Settings())


async def get_user_service(
        user_repository: UserRepository = Depends(get_user_repository),
        auth_service: AuthService = Depends(get_auth_service)
) -> UserService:
    return UserService(user_repository=user_repository, auth_service=auth_service)

reusable_oauth2 = security.HTTPBearer()

async def get_request_user_id(
        auth_service: AuthService = Depends(get_auth_service),
        token: security.http.HTTPAuthorizationCredentials = Security(reusable_oauth2)
        ) -> int:

    try:
        user_id = auth_service.get_user_id_from_token(token.credentials)
    except TokenExpiredException as e:
        raise HTTPException(status_code=401, detail=e.detail)
    except TokenNotCorrectException as e:
        raise HTTPException(status_code=401, detail=e.detail)

    return user_id