#!/usr/bin/python3

from datetime import datetime
import uuid

import models


class BaseModel:

    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        """..."""
        self.id: str = str(uuid.uuid4())
        self.created_at: datetime = datetime.now()
        self.updated_at: datetime = self.created_at

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    val = datetime.strptime(str(value), "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, val)
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self) -> None:
        
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:

        properties: dict = self.__dict__.copy()
        properties["__class__"] = self.__class__.__name__


        properties["created_at"] = self.created_at.isoformat()
        properties["updated_at"] = self.updated_at.isoformat()

        return properties

    def __str__(self) -> str:
        """..."""
        classname = self.__class__.__name__
        return f"[{classname}] ({self.id}) {self.__dict__}"
