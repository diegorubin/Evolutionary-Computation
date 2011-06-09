class Ant():
    def __init__(self):
        self.distance = .0
        self.route = []
        self.__coverage = []

    def set_coverage(self, points):
        self.__coverage = points

    def travel_completed(self):
        return len(self.__coverage) == 0
