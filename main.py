from builtins import print

print("Hello World")


class Panel:

    def __init__(self, parent, content, width=1, height=1):
        """

        :type width: int
        :type height: int
        """
        self.parent = parent
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


class Layout(panel):

    def __init__(self, parent, style, content, width, height):
        """
        Styles: simpleGrid, columns, rows, box, columnSplit
        :type style: str
        """
        super(Layout, self).__init__(parent, content, width, height)
        self.style = style
