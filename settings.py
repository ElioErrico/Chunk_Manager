from pydantic import BaseModel
from cat.mad_hatter.decorators import plugin


class MySettings(BaseModel):
    Chunk_Size: int = 1024
    Chunk_Overlap: int = 128


@plugin
def settings_schema():
    return MySettings.schema()
