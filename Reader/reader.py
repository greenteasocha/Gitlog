import zlib

from typing import Type

from Objects.git_object import GitObject, MyObject
from Util.Util import *

class Reader(object):
    def __init__(self, hash_string: str):
        self.hash_string = hash_string
        self.object = self.get_object(hash_string)

    def get_object(self, hash_string: str) -> GitObject:
        root_dir: str = find_git_root(".")
        object_file_path: str = r"{0}/.git/objects/{1}/{2}".format(
            root_dir,
            hash_string[:2],
            hash_string[2:]
        )

        try:
            with open(object_file_path, "rb") as f:
                data: bytes = f.read()

                print(zlib.decompress(data))

        except Exception:
            # e.g. character encoding and decoding
            print("Fail at reading binary object files.")
            raise Exception

        return GitObject(hash_string)

