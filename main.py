import random
import string
from builtins import print
from copy import deepcopy
from typing import List, Any

from LoremIpsum import *
from PresentationClasses import TextBlob, ColumnSplit


class SimpleList:
    cache: List[Any]

    def __init__(self, content, width=10, height=10):
        self.content = content
        self.width = width
        self.height = height
        self.cache = []

    def update(self):
        # deepcopy content to cache
        self.cache = deepcopy(self.content)
        for i in range(0, self.cache.__len__()):
            if not str.__instancecheck__(self.cache[i]):
                self.cache[i] = str(self.cache[i])
            self.cache[i] = str(self.cache[i][:25])
            self.cache[i] = self.cache[i].ljust(self.width)

    def render(self, index):
        if index < self.cache.__len__():
            return self.cache[index]
        else:
            return " " * self.width


temporary_list = []
temporary_string = ''
for l in string.ascii_lowercase:
    temporary_string = ""
    temporary_string += str(l)
    for k in range(0, 40):
        temporary_string += str(k % 10)
    if random.randrange(0, 2, 1) >= 1:
        temporary_string = temporary_string[0: random.randrange(5, 40)]
    temporary_list.append(temporary_string)

temporary_simple_list = SimpleList(temporary_list, 25, 10)
temporary_simple_list.update()

for foo in range(0, 30):
    print(temporary_simple_list.render(foo))
