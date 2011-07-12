class Ant():
    def __init__(self):
        self.distance = .0
        self.route = []
        self.__coverage = []
        self.__actual_tower = None
        self.possible_towers = []
        self.position = -1

    def set_coverage(self, points):
        self.__coverage = points

    def travel_completed(self):
        return not any(self.__coverage)

    def set_actual_tower(self,tower):
        self.__actual_tower = tower
        self.distance += tower.cost
        self.route.append(tower)
        self.__update_coverage()
        self.__remove_possible_towers()

    def get_actual_tower(self):
        return self.__actual_tower

    def __update_coverage(self):
        for point in self.__actual_tower.points:
            try:
                self.__coverage.remove(point)
            except:
                pass
    
    def __remove_possible_towers(self):
        new_points = self.__actual_tower.points
        for tower in self.possible_towers:
            if new_points == tower.points:
            	self.possible_towers.remove(tower)
