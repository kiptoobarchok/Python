#!/usr/bin/python3
import uuid
import json
from datetime import datetime

"class BaseModel that defines all common attributes/methods for other classes"

class BaseModel:
    def __init__(self):
        "public instance attributes"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        "return a string representation for visualization"
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        dict_cp = self.__dict__.copy()
        dict_cp["__class__"] = self.__class__.__name__
        dict_cp["created_at"] = self.created_at.isoformat()
        dict_cp["updated_at"] = self.updated_at.isoformat()
        return dict_cp
    