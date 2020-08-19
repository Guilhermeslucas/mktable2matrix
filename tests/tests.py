import sys
from mktable2matrix import to_matrix

f = open('wordsTable.md', 'r')

matrix = to_matrix(f.read())

for line in matrix:
    print(line)