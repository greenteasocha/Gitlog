import pytest

from Objects.git_object import GitObject


def test_get_commit():
    hash_value = "d97c56d835a41b5fcd169c858516bfd2d8ca3ae8"
    decompressed = b'commit 19\x00' \
             b'dummy data\n' \
             b'newline\n'

    o = GitObject()
    o.get_object(decompressed, hash_value)

    assert o.obj_type == "commit"
    assert o.obj_size == 19
    assert o.data == "dummy data\nnewline\n"
    assert o.hash_value == hash_value


def test_get_commit_invalid_hash_fail():
    hash_value = "abcdefg835a41b5fcd169c858516bfd2d8ca3ae8"
    decompressed = b'commit 19\x00' \
                   b'dummy data\n' \
                   b'newline\n'

    with pytest.raises(Exception):
        o = GitObject()
        o.get_object(decompressed, hash_value)




def test_get_commit_invalid_size_fail():
    hash_value = "64ccff6ed120f92f1e48b325fe7d7eaefcdfc9b9"
    decompressed = b'commit 30\x00' \
                   b'dummy data\n' \
                   b'newline\n'

    with pytest.raises(Exception):
        o = GitObject()
        o.get_object(decompressed, hash_value)


def test_get_commit_invalid_type():
    hash_value = "19628db2b8b2328cd8490baf122c6962e3d17732"
    decompressed = b'invalid 19\x00' \
                   b'dummy data\n' \
                   b'newline\n'

    with pytest.raises(Exception):
        o = GitObject()
        o.get_object(decompressed, hash_value)



