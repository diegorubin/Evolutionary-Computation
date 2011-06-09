class Tower():
    def __init__(self):
        self.name = ''
        self.cost = 0
        self.points = []
        self.__ants = []

    def put_ant(self,ant):
        ant.route.append(self.name)
        ant.distance += self.cost
        self.__ants.append(ant)

    def get_ants(self):
        return self.__ants
