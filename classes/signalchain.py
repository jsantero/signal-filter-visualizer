

class ChainElement(object):
    def __init__(self, data=None):
        self.input = data
        self.output = None
        self.function = None
        self.enabled = True
        #self.update()

    def update(self):
        if self.enabled and self.function:
            self.output = self.function(self.input)
        else:
            self.output = self.input

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
                self.chainList[i].input = self.chainList[i-1].output
            self.chainList[i].update()

    def add(self, data):
        element = ChainElement(data)
        self.chainList.append(element)
        self.update()
