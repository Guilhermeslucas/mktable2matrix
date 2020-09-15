# mktable2matrix ![Run all tests](https://github.com/Guilhermeslucas/mktable2matrix/workflows/Run%20all%20tests/badge.svg?branch=main)

Python package to convert markdown tables to matrix.

## Download

To download and use it via pip, do:

``` sh
pip install -i https://test.pypi.org/simple/ mktable2matrix
```

Note: For now, the package is on the test.pypi org. It will be on general pypi
as soon as it hits version 1.0.0.

## Usage Examples

The package is intended to be simple. To convert your table to a array of arrays, follow
the steps:

``` python
from mktable2matrix import to_matrix

f = open('myTable.md', 'r')

matrix = to_matrix(f.read())

```

Now, to convert do a dictionary, that uses the header as the key, do:

``` python
from mktable2matrix import to_dict

f = open('myTable.md', 'r')

content_dict = to_dict(f.read())

```

You can see more examples on how to use the lib on the ```tests/tests.py``` file.
