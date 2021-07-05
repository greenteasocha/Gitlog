import dataclasses
import zlib
import os
import sys
from pprint import pprint
from datetime import datetime

from Reader.reader import Reader

filename = "./.git/objects/9e/fc8cae1418d66e96fcef940e986093ea69a606"
r = Reader()
r.get_object("d4fbabb18e6ea798e2cbbbe3f70bb975ba37c603")


# with open(filename, "rb") as f:

    # print(len("tree 2f1c5e0a9d1907f30203c1fea1f51fcf599077de\nauthor abe <kouheiatts@gmail.com> 1625493180 +0900\ncommitter abe <kouheiatts@gmail.com> 1625493180 +0900\n\ninit\n"))