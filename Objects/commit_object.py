from dataclasses import dataclass
from pprint import *
from typing import List

from Objects.git_object import GitObject


@dataclass
class CommitObject(object):
    tree: str = None
    parent: str = None
    author: str = None
    committer: str = None
    message: str = None

    def get_commit(self, obj: GitObject):
        data = obj.data
        lines = data.split("\n")

        message_flag: bool = False
        messages: List[str] = []

        for line in lines:
            split_text = line.split(" ", 1)
            if len(split_text) < 2:
                message_flag = True

            if message_flag:
                messages.append(line)

            else:
                self.set_attributes(split_text)

    def set_attributes(self, split_text: List[str]):
        key, value = split_text
        if key in ['tree', 'parent', 'author', 'committer']:
            exec("self.{} = value".format(key), {}, {"self": self, "value": value})



class MyObject(object):
    def __init__(self):
        self.x = 1
