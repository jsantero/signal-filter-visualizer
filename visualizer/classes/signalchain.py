

class ChainElement(object):
    def __init__(self, data=(0,0), name=None):
        self.input_ = data
        self.output = None
        self.function = None
        self.enabled = True
        self.name = name

    def function(self):
        raise ValueError("ChainElement.function called when it was not set.")

    def update(self):
        if self.enabled and self.function:
            self.output = self.function(self.input_)
        else:
            self.output = self.input_

class ChainContainer(object):
    """Contains elements of a signal chain where one element's output is
       routed to the following element's input
    """
    def __init__(self):
        #super().__init__()
        self.chainList = []

    def update(self):
        for i in range(len(self.chainList)):
            if i is not 0:
                self.chainList[i].input_ = self.chainList[i-1].output
            else:
                self.chainList[i].input_ = (0,0)  # Reset input if first elem
            self.chainList[i].update()

    def add(self, element):
        self.chainList.append(element)
        self.update()

    def remove(self, index):
        if len(self.chainList) > 0:
            self.chainList.pop(index)
            self.update()

    def rename(self, index, name):
        if len(self.chainList) > 0:
            self.chainList[index].name = name
