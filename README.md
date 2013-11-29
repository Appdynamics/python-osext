# `filesystem` module

```python
import filesystem as fs
```

## Testing if a path is a file (shortcut for `try`/`with open`):

```python
fs.isfile('something')
fs.isfile('something', mode='r')
```

## Shortcut for `rsync -a`

Uses [`sh` module](https://pypi.python.org/pypi/sh/).

```python
fs.sync('name@somehost:~/somedir/', 'local_path')
fs.sync('~/somedir', '.')
```

Returns exit code and does not catch any exceptions raised by `sh`.


# `pushd` usage with the `with` statement

```python
from osext.pushdcontext import pushd

with pushd('some_dir') as context:
    pass
```
