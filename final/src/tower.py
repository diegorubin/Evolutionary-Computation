class Tower():
    def __init__(self):
        self.name = ''
        self.cost = 0
        self.points = []
        self.__ants = []

    def append_ant(self,ant):
        ant.route.append(self.name)
        ant.distance += position.cost
        self.__ants.append(ant)
