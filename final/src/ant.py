class Ant():
    def __init__(self):
        self.distance = .0
        self.route = []
        self.__coverage = []
        self.__actual_tower = None

    def set_coverage(self, points):
        self.__coverage = points

    def travel_completed(self):
        return len(self.__coverage) == 0

    def set_actual_tower(self,tower):
        self.__actual_tower = tower
        self.__coverage.append(tower)
        self.distance += tower.cost
        self.route.append(tower)
        self.__update_coverage()

    def __update_coverage(self):
        for point in self.__actual_tower.points:
            try:
        	    self.__coverage.remove(point)
            except:
                pass
