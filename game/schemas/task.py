import pydantic
from pygame import Surface


class Task(pydantic.BaseModel):
    image: Surface
    correct_answer: str
