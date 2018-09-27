from textwrap import wrap
from builtins import print
from typing import List, Any

from LoremIpsum import *


# from MengClasses import *


class TextBlob:
    # blob_wrap: List[Any]

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
        return self.blob_wrap[index].ljust(self.width)


test_blob = TextBlob(paragraph_ipsum)
test_blob.width = 40
test_blob.update()

for m in range(0, test_blob.blob_wrap.__len__()):
    print(test_blob.render(m) + " |")
