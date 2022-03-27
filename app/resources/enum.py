from enum import Enum, unique


@unique
class MediaType(Enum):
    MOVIE = 1
    TV_SERIES = 2
    SHOT_SERIES = 3

    def __int__(self):
        return self.value
