from typing import Annotated
from fastapi import APIRouter, status, Depends, HTTPException

from dependency import get_task_repository, get_task_service, get_request_user_id

from database import get_db_session
from exception import TaskNotFoundException
from schema import TaskSchema, TaskCreateSchema
from repository import TaskRepository
from service import TaskService

router = APIRouter(prefix='/tasks', tags=['task'])


@router.get(
    '/all',
    response_model=list[TaskSchema]
)
async def get_tasks(
        task_service: Annotated[TaskService, Depends(get_task_service)]
):
    return await task_service.get_tasks()


@router.get(
    '/',
    response_model=TaskSchema
)
async def get_task(task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    task = await  task_repository.get_task()
    return task


@router.post('/',
             response_model=TaskSchema
             )
async def create_task(
        body: TaskCreateSchema,
        task_service: Annotated[TaskService, Depends(get_task_service)],
        user_id: int = Depends(get_request_user_id)
):
    task = await task_service.create_task(body, user_id)
    return task


@router.patch(
        '/{task_id}',
        response_model=TaskSchema
)
async def patch_task(
        task_id: int,
        name: str,
        task_service: Annotated[TaskService, Depends(get_task_service)],
        user_id: int = Depends(get_request_user_id)
):
    try:
        return await task_service.update_task_name(task_id=task_id,name=name,user_id=user_id)
    except TaskNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)


@router.delete('/{task_id}',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
        task_id: int,
        task_service: Annotated[TaskService, Depends(get_task_service)],
        user_id: int = Depends(get_request_user_id)
):
    try:
        await task_service.delete_task(task_id=task_id, user_id=user_id)
    except TaskNotFoundException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e.detail)

