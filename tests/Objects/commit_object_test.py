import pytest

from Objects.commit_object import CommitObject
from Objects.git_object import GitObject


def test_get_commit():
    o = GitObject()
    o.obj_type = "commit"
    o.obj_size = "265"
    o.data = 'tree de7dfe27b9f4a4621c067b045cf2101a76440e35\n' \
             'parent af80478c1338269ce4b3ac0106da3d3a5ef6e6f9\n' \
             'parent b3ac0106da3d3a5ef6e6f9af80478c1338269ce4\n' \
             'author abe <kouheiatts@gmail.com> 1625495822 +0900\n' \
             'committer abe <kouheiatts@gmail.com> 1625495822 +0900\n' \
             '\n' \
             'removing pycache\n' \
             '\n'

    c = CommitObject()
    c.get_commit(o)

    assert c.tree == "de7dfe27b9f4a4621c067b045cf2101a76440e35"
    assert c.parents == [
        "af80478c1338269ce4b3ac0106da3d3a5ef6e6f9",
        "b3ac0106da3d3a5ef6e6f9af80478c1338269ce4"
    ]
    assert c.author == "abe <kouheiatts@gmail.com> 1625495822 +0900"
    assert c.committer == "abe <kouheiatts@gmail.com> 1625495822 +0900"
    assert c.message == "\nremoving pycache\n\n"


def test_get_commit_without_parent():
    o = GitObject()
    o.obj_type = "commit"
    o.obj_size = "217"
    o.data = 'tree de7dfe27b9f4a4621c067b045cf2101a76440e35\n' \
             'author abe <kouheiatts@gmail.com> 1625495822 +0900\n' \
             'committer abe <kouheiatts@gmail.com> 1625495822 +0900\n' \
             '\n' \
             'removing pycache\n' \
             '\n'

    c = CommitObject()
    c.get_commit(o)

    assert c.tree == "de7dfe27b9f4a4621c067b045cf2101a76440e35"
    assert c.author == "abe <kouheiatts@gmail.com> 1625495822 +0900"
    assert c.message == "removing pycache\n\n"


def test_get_commit_invalid_fail():
    o = GitObject()
    o.obj_type = "commit"
    o.obj_size = "148"
    o.data = 'invalid something value\n' \
             'author abe <kouheiatts@gmail.com> 1625495822 +0900\n' \
             'committer abe <kouheiatts@gmail.com> 1625495822 +0900\n' \
             '\n' \
             'removing pycache\n' \
             '\n'

    with pytest.raises(Exception):
        c = CommitObject()
        c.get_commit(o)
