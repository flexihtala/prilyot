import pydantic
from pygame import Surface


class Task(pydantic.BaseModel):
    image: Surface
    correct_answer: str

    model_config = pydantic.ConfigDict(arbitrary_types_allowed=True)
