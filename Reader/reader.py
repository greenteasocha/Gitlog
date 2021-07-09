from __future__ import annotations

import zlib
from collections import defaultdict
from typing import Type
from queue import Queue

from Objects.git_object import GitObject
from Objects.commit_object import CommitObject
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
        g.get_object(decompressed, hash_string)

        return g

    def walk_history(self, target_hash):
        target_obj = self.get_object(target_hash)
        parents: Queue[GitObject] = Queue()
        parents.put(target_obj)

        hash_seen = defaultdict(int)  # used for cycle detection
        # hash_seen[target_hash] = 1

        # loop until reaching initial commit or raising errors
        while not parents.empty():
            current_obj = parents.get()

            if current_obj.obj_type != "commit":  # TODO: I'm not be sure that all objects must be commit
                raise Exception(
                    "target object is not a commit: {}".format(current_obj.hash_value)
                )

            if current_obj.hash_value in hash_seen:
                raise Exception(
                    "Cycle detected at walking history."
                )
            else:
                hash_seen[current_obj.hash_value] = 1

            commit = CommitObject()
            commit.get_commit(current_obj)
            print(commit)

            if commit.parents:
                for parent in commit.parents:
                    parent_obj = self.get_object(parent)
                    parents.put(parent_obj)

        print("finish")
        return

