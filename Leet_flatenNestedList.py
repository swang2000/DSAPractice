class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.idx = -1
        self.elements = []
        self.unNest(nestedList)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            self.idx += 1
            return self.elements[self.idx]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx < len(self.elements) - 1

    def unNest(self, i):
        if isinstance(i, int):
            self.elements.append(i)
        elif isinstance(i, list):
            for c in i:
                self.unNest(c)


a = NestedIterator([1,[4,[6]]])
a.next()
