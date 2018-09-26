from builtins import print

print("Hello World")


class Panel:

    def __init__(self, parent, style, content, width=1, height=1):
        """
        Styles: simpleGrid, columns, rows, box, columnSplit
        :type style: str
        :type width: int
        :type height: int
        """
        self.parent = parent
        self.style = style
        self.content = content
        self.width = width
        self.height = height

    def update(self):
        # Refresh cached whatever
        pass


class DisplayTerminal:

    def __init__(self, width=10, height=10):
        """

        :type width: int
        :type height: int
        """
        self.width = width
        self.height = height
        self.owner = "dummyPlayer"  # TODO: Multiplayer
        self.contents = list()
