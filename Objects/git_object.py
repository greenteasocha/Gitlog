from dataclasses import dataclass
from pprint import *
from typing import List

OBJECT_TYPES: List[str] = [
    "undefined",
    "commit",
    "tree",
    "blob",
    "tag",
]


@dataclass()
class GitObject(object):
    obj_type: str = None
    obj_size: str = None
    data: str = None

    def get_object(self, decompressed: bytes):
        header: bytes
        contents: bytes
        header, data = decompressed.split(b"\x00")

        obj_type: str
        obj_size: str
        obj_type, obj_size = header.decode('utf-8').split(" ")

        if obj_type not in OBJECT_TYPES:
            raise Exception("Invalid object type: {}".format(obj_type))
        if len(data) != int(obj_size):
            raise Exception("Invalid object size. Expect: {}, Actual: {}".format(obj_size, len(data)))

        data = data.decode('utf-8')
        self.obj_type, self.obj_size, self.data = obj_type, obj_size, data

class MyObject(object):
    def __init__(self):
        self.x = 1
