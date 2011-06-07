from tower import Tower
from ant   import Ant

class Space():
    def __init__(self):
        self.__towers = []
        self.points = 0

    def append_tower(self, tower):
        self.__towers.append(tower);

    # check if input is valid
    def valid(self):
        points = range(1,self.points+1); 
        for tower in self.__towers:
            for point in tower.points:
                try:
            	    points.remove(point)
                except:
                    pass
            if(len(points) == 0):
            	break
        return (len(points) == 0)

    def read_input(self, input_file):
        inputs = open(input_file)
        self.points = int(inputs.readline())
        for line in inputs.readlines():
            informations = line.split(' ')
            tower = Tower()
            tower.name = informations.pop(0)
            tower.cost = float(informations.pop(0))
            tower.points = [int(point) for point in informations if point.isdigit()]

            self.append_tower(tower)
    
    def put_ants(self):
        for tower in self.__towers:
        	ant = Ant()
        	tower.append(ant)
