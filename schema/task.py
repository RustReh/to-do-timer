from pydantic import BaseModel, Field, model_validator


class TaskSchema(BaseModel):
    id: int | None = None
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int | None = None
    asd: str | None = None
    user_id: int

    class Config:
        from_attributes = True

    @model_validator(mode='after')
    def name_pomodoro_count_validator(self):
        if self.name is None and self.pomodoro_count is None:
            raise ValueError('name and pomodoro_count are required fields')
        print (self)
        return self

class TaskCreateSchema(BaseModel):
    name: str | None = None
    pomodoro_count: int | None = None
    category_id: int | None = None
    asd: str | None = None