from typing import ForwardRef

from pydantic import BaseModel, PydanticUserError

UndefinedType = ForwardRef('UndefinedType')


class AddToCart(BaseModel):
    Item=str
    Price=int
    Quantity=int