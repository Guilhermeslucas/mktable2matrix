# mktable2matrix

Python package to convert markdown tables to matrix.

## Download

To download and use it via pip, do:

``` sh
pip install -i https://test.pypi.org/simple/ mktable2matrix
```

Note: For now, the package is on the test.pypi org. It will be on general pypi
as soon as it hits version 1.0.0.

## Usage Examples

The package is intended to be simple. To convert your table, follow
the steps:

``` python
from mktable2matrix import to_matrix

f = open('myTable.md', 'r')

matrix = to_matrix(f.read())

```
