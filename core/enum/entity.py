from enum import Enum

class EntityEnum(Enum):
    ROLE = "role"
    PERSON = "person"
    PERMISSION = "permission"
    
    def get(self):
        return self.value

    