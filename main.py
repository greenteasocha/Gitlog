import dataclasses
import zlib
import os
import sys
from pprint import pprint
from datetime import datetime

from Objects.commit_object import CommitObject
from Reader.reader import Reader


def main():
    hash_value = "d4fbabb18e6ea798e2cbbbe3f70bb975ba37c603"
    r = Reader()
    # o = r.get_object(hash_value)
    # c = CommitObject()
    # c.get_commit(o)
    #
    # pprint(o)

    r.walk_history(hash_value)


if __name__ == "__main__":
    main()
