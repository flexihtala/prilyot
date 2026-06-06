from pydantic import BaseModel


class Rectangle(BaseModel):
    x_first: int
    x_second: int
    y_first: int
    y_second: int
