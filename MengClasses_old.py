class Panel:

    def __init__(self, parent, style, children, width="auto", height="auto"):
        """
        Styles:
            simpleGrid: evenly divides (based on what?)
            column: Vertically arranged, sub-sized by list of dims, supports
            auto.
            row: Horizontally arranged, sub-sized by list of dims, supports
            auto.
            box: Single item, no sub-size.
            columnSplit: 'pages' contents across columns, sub-sized by
            column count, and maybe other stuff.
        :type style: str
        """
        self.parent = parent
        self.style = style
        self.children = children
        self.width = width
        self.height = height

    def update(self):
        # Set dimensions on all children, then call update() on them.
        # Refresh cached whatever.
        pass

    def present(self, width, index):
        # call present() on children in render order, for one line.
        print("I tried")


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


class ListRender:

    def __init__(self):
        pass
