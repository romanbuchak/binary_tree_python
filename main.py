class Device:
    def __init__(self, type, brand, measureLimit, year):
        self.type = type
        self.brand = brand
        self.measureLimit = measureLimit
        self.year = year

    def __gt__(self, other):
        if self.brand > other.brand:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.brand < other.brand:
            return True
        else:
            return False

    def __str__(self):
        return "Type: {} brand: {} measurement limit:{} year: {}".format(self.type, self.brand, self.measureLimit,
                                                                         self.year)


class BinaryTreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self, side):
        print(side, " - ", self.data, )
        if self.left:
            self.left.print_tree("left")
        if self.right:
            self.right.print_tree("right")

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = BinaryTreeNode(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def getNodeOverMeasure(self, measureLimit):
        if self.left:
            self.left.getNodeOverMeasure(measureLimit)
        if self.data.measureLimit >= measureLimit:
            print(self.data)
        if self.right:
            self.right.getNodeOverMeasure(measureLimit)

    def minValue(self):
        current = self
        pre_current = None
        while current and current.left:
            pre_current = current
            current = current.left

        return current, pre_current

    def deleteByYear(self, year):
        if self.left:
            self.left = self.left.deleteByYear(year)
        if self.right:
            self.right = self.right.deleteByYear(year)
        if self.data.year == year:

            if not self.left and not self.right:  # no child
                return None
            elif not self.left:  # only right child
                return self.right
            elif not self.right:  # only left child
                return self.left

            # has 2 child
            temp, recurrent = self.right.minValue()
            if recurrent:
                if temp.right:
                    recurrent.left = temp.right
                else:
                    recurrent.left = None
            else:
                self.right = temp.right
            self.data = temp.data

        return self


dev1 = Device('sa', 5, 12, 2001)
dev2 = Device('asa', 2, 2, 2002)
dev3 = Device('dsa', 1, 32, 2003)
dev4 = Device('bsa', 3, 10, 2004)
dev5 = Device('bsa', 4, 8, 2001)
root = BinaryTreeNode(dev1)
root.insert(dev2)
root.insert(dev3)
root.insert(dev4)
root.insert(dev5)
root.insert(Device('bsa', 9, 8, 2002))
root.insert(Device('bsa', 7, 8, 2001))
root.insert(Device('bsa', 8, 8, 2004))
root.insert(Device('bsa', 10, 8, 2002))
root.print_tree('main node')
print()
root.deleteByYear(2002)
root.print_tree("main node2")
print()
print("Over measure")
root.getNodeOverMeasure(9)
dev1 = Device('sa', 3, 12, 2002)
dev2 = Device('asa', 2, 2, 2001)
dev3 = Device('dsa', 1, 32, 2004)
dev4 = Device('bsa', 5, 10, 2004)
dev5 = Device('bsa', 4, 8, 2003)
