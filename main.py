from builtins import print
from LoremIpsum import *

# from MengClasses import *

print("Hello World")

# Testing data
# top left
phat_string = "Insert some lorem ipsum here"
# top right
some_list = ["Andrew", "George", "Fred", "Alice"]  # Make it some names
# bottom right
an_inventory = []


class TextBlob:
    def __init__(self, blob):
        self.blob = blob
        self.width = 0
        self.blob_wrap = []

    def update(self):
        in_blob = self.blob
        # Go to width index, if not-space search left for space,
        # split there, pack left chunk in blob_wrap @ index, repeat until
        # in_blob is empty.

    def render(self, index):
        return self.blob_wrap[index].rjust(self.width)


test_blob = TextBlob(lorem_ipsum)
test_blob.width = 20
test_blob.update()
print(test_blob.render(0))
