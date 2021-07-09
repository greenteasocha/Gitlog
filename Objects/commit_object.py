from dataclasses import dataclass, field
from pprint import *
from typing import List

from Objects.git_object import GitObject


@dataclass
class CommitObject(object):
    # TODO: hash check
    tree: str = None
    parents: List[str] = field(default_factory=list)
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

        self.message = "\n".join(messages)

        return

    def set_attributes(self, split_text: List[str]):
        key, value = split_text
        if key in ['tree', 'author', 'committer']:
            exec("self.{} = value".format(key), {}, {"self": self, "value": value})
        elif key == "parent":
            self.parents.append(value)
        else:
            raise Exception(
                "Invalid commit format: {} {}\nHash: {}"
                .format(key, value, hash)
            )

        return
