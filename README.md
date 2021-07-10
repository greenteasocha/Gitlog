# Gitlog
Simple implementation of `git log` by python.  
(For personal learning)

## usage
```
python main.py {full commit hash)
```

**example**
```
$ python main.py 17446647f5bf5ee46216aa0be1d51fcfcabb8788
tree: 9c48013acbec3716a09f885cc4aa9b45e1485972
parent: d4fbabb18e6ea798e2cbbbe3f70bb975ba37c603
author: abe <kouheiatts@gmail.com> 1625509550 +0900
committer: abe <kouheiatts@gmail.com> 1625509550 +0900

implement GItObject

tree: de7dfe27b9f4a4621c067b045cf2101a76440e35
parent: af80478c1338269ce4b3ac0106da3d3a5ef6e6f9
author: abe <kouheiatts@gmail.com> 1625495822 +0900
committer: abe <kouheiatts@gmail.com> 1625495822 +0900

removing pycache

tree: 96465d4e6ebd4595bf549109c7c0354b24943987
parent: 9efc8cae1418d66e96fcef940e986093ea69a606
author: abe <kouheiatts@gmail.com> 1625495649 +0900
committer: abe <kouheiatts@gmail.com> 1625495649 +0900

implement reader and frame of GitObject Class

tree: 2f1c5e0a9d1907f30203c1fea1f51fcf599077de
author: abe <kouheiatts@gmail.com> 1625493180 +0900
committer: abe <kouheiatts@gmail.com> 1625493180 +0900

init

finish
```

## reference
**Hands-on**  
https://www.youtube.com/watch?v=-4rcs6SgT0o  
https://github.com/shumon84/git-log

**Git documents**  
https://git-scm.com/book/en/v2/Git-Internals-Git-Objects

## TODOs
:x: Handling multi-byte characters (doesn't seem to work properly)  
:x: Considering pack objects   
:x: automating test  
:x: writing reader test (need to create dummy direcroty and files(?))  

:heavy_check_mark: commit hash check  
:heavy_check_mark: writing object test  

