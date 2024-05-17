from enum import  Enum

class LinkEnum(Enum):
    DEFAULT_HOME = "default.home",
    DEFAULT_LOGIN = "default.login"

    def get(self):
        return self.value