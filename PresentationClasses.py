from textwrap import wrap


class TextBlob:

    def __init__(self, blob, width=10, height=10):
        self.blob = blob  # TODO: Refactor name "blob" to "content"
        self.width = width
        self.height = height
        self.blob_wrap = []  # TODO: Refactor name "blob_wrap" to "content_wrap"

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
        if index <= self.blob_wrap.__len__():
            return self.blob_wrap[index].ljust(self.width)
        else:
            return " " * self.width


class ColumnSplit:

    def __init__(self, child, column_count, width=10, height=10, sep=" |"):
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
            t_list.append(self.child.render(index + (column * (self.height +
                                                               1))))
        # print(t_list)
        t_string = self.sep.join(t_list)
        return t_string
