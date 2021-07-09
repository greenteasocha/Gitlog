import zlib

from typing import Type

from Objects.git_object import GitObject
from Util.Util import *

class Reader(object):
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
                decompressed: bytes = zlib.decompress(data)

        except Exception:
            # e.g. character encoding and decoding
            print("Fail at reading binary object files.")
            raise Exception

        g: GitObject = GitObject()
        g.get_object(decompressed)

        return g

