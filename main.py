from textwrap import wrap
from builtins import print

from LoremIpsum import *


class TextBlob:

    def __init__(self, blob, width=10, height=10):
        self.blob = blob
        self.width = width
        self.height = height
        self.blob_wrap = []

    def update(self):
        in_list: list = self.blob.splitlines(keepends=True)
        for m in in_list:
            if m != "\n":
                if m.endswith("\n"):
                    self.blob_wrap.extend(wrap(m.strip("\n"), self.width))
                    self.blob_wrap.append("")
                else:
                    self.blob_wrap.extend(wrap(m, self.width))
            elif m == "\n":
                self.blob_wrap.append("")

    def render(self, index):
        print(self.blob_wrap[index].ljust(self.width))
        return self.blob_wrap[index].ljust(self.width)


class ColumnSplit:

    def __init__(self, child, column_count, width=10, height=10, sep=" | "):
        self.child = child
        self.column_count = column_count
        self.width = width
        self.height = height
        self.sep = sep
        self.cache = []
        self.column_width = width // column_count

    def update(self):
        self.child.width = (self.column_width - 1)
        self.child.update()

    def render(self, index):
        t_list = []
        for column in range(0, self.column_count):
            t_list.append(self.child.render(index * (column + 1)))
        print(t_list)
        return "-----------"

# Existing known problems:
# - The multiplication trick isn't working, need to map what actually
# happens and then come up with a better solution.
# - There's an index out of range issue, not quite sure where yet.

test_blob = TextBlob(paragraph_ipsum)
test_col_split = ColumnSplit(test_blob, 3, 90, 20)
test_col_split.update()
for i in range(0, test_col_split.height):
    print(test_col_split.render(i))
