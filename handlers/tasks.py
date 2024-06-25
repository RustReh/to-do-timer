from typing import Annotated
from fastapi import APIRouter, status, Depends

from dependency import get_task_repository, get_task_service

from database import get_db_session
from schema.task import TaskSchema
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
    return task_service.get_tasks()


@router.get(
    '/',
    response_model=TaskSchema
)
async def get_task(task_repository: Annotated[TaskRepository, Depends(get_task_repository)]):
    task = task_repository.get_task()
    return task


@router.post('/',
             response_model=TaskSchema
             )
async def create_task(
        task: TaskSchema,
        task_repository: Annotated[TaskRepository, Depends(get_task_repository)]
):
    task_id = task_repository.create_task(task)
    task.id = task_id
    return task


@router.patch(
        '/{task_id}',
        response_model=TaskSchema
)
async def patch_task(
        task_id: int,
        name: str,
        task_repository: Annotated[TaskRepository, Depends(get_task_repository)]
):
    return task_repository.update_task_name(task_id, name)


@router.delete('/{task_id}',
               status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
        task_id: int,
        task_repository: Annotated[TaskRepository, Depends(get_task_repository)]
):
    task_repository.delete_task(task_id)
    return {'text': 'task deleted'}
