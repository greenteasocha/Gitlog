import dataclasses
import zlib
import os
import sys
from pprint import pprint
from datetime import datetime

from Util.Util import *

filename = ""
with open(filename, "rb") as f:
    data = f.read()
    #
    print(data)
    pprint(zlib.decompress(data))
