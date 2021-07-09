import pytest

from Objects.commit_object import CommitObject
from Objects.git_object import GitObject

hash_value = "d4fbabb18e6ea798e2cbbbe3f70bb975ba37c603"


def test_get_commit():
    decompressed = b'commit 19\x00' \
             b'dummy data\n' \
             b'newline\n'

    o = GitObject()
    o.get_object(decompressed, hash_value)

    assert o.obj_type == "commit"
    assert o.obj_size == 19
    assert o.data == "dummy data\nnewline\n"
    assert o.hash_value == hash_value


def test_get_commit_invalid_size_fail():
    with pytest.raises(Exception):
        decompressed = b'commit 30\x00' \
                       b'dummy data\n' \
                       b'newline\n'

        o = GitObject()
        o.get_object(decompressed, hash_value)


def test_get_commit_invalid_type():
    with pytest.raises(Exception):
        decompressed = b'invalid 19\x00' \
                       b'dummy data\n' \
                       b'newline\n'

        o = GitObject()
        o.get_object(decompressed, hash_value)



