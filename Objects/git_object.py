import hashlib
from dataclasses import dataclass
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
    hash_value: str = None
    obj_type: str = None
    obj_size: int = None
    data: str = None

    def get_object(self, decompressed: bytes, hash_value: str):
        content_hash = hashlib.sha1(decompressed).hexdigest()
        if content_hash != hash_value:
            raise Exception(
                "Hash doesn't match: {}".format(hash_value)
            )

        header: bytes
        contents: bytes
        header, data = decompressed.split(b"\x00")

        obj_type: str
        obj_size: str
        obj_type, obj_size = header.decode('utf-8').split(" ")

        if obj_type not in OBJECT_TYPES:
            raise Exception("Invalid object type: {}".format(obj_type))
        if len(data) != int(obj_size):
            raise Exception(
                "Invalid object size. Expect: {}, Actual: {}".format(
                    obj_size, len(data)
                )
            )

        data = data.decode('utf-8')

        self.hash_value = hash_value
        self.obj_type = obj_type
        self.obj_size = int(obj_size)
        self.data = data


