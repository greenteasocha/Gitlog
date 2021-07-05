from pprint import *
from typing import List

OBJECT_TYPES: List[str] = [
    "undefined",
    "commit",
    "tree",
    "blob",
    "tag",
]

class GitObject(object):
    def __init__(self, decompressed: bytes):
        header: bytes
        contents: bytes
        header, contents = decompressed.split(b"\x00")

        obj_type: str
        obj_size: str
        obj_type, obj_size = header.decode('utf-8').split(" ")

        if obj_type not in OBJECT_TYPES:
            raise Exception("Invalid object type: {}".format(obj_type))
        if len(contents) != int(obj_size):
            raise Exception("Invalid object size. Expect: {}, Actual: {}".format(obj_size, len(contents)))

        pprint(contents.split(b"\n"))


class MyObject(object):
    def __init__(self):
        self.x = 1