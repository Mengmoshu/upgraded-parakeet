from textwrap import wrap
from builtins import print
from LoremIpsum import *


# from MengClasses import *


class TextBlob:
    def __init__(self, blob, width=10, height=10):
        self.blob = blob
        self.width = width
        self.height = height
        self.blob_wrap = []

    def update(self):
        in_blob: str = self.blob
        # Uses the textwrap module/lib
        self.blob_wrap = wrap(in_blob, self.width)


    def render(self, index):
        return self.blob_wrap[index].ljust(self.width)


test_blob = TextBlob(paragraph_ipsum)
test_blob.width = 40
test_blob.update()

for m in range(0, test_blob.blob_wrap.__len__()):
    print(test_blob.render(m) + " |")
