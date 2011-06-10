from tower import Tower
from ant   import Ant

class Space():
    def __init__(self):
        self.__towers = []
        self.__ants = []
        self.points = 0
        self.__inf = []

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
        self.__init_inf()
    
    def put_ants(self):
        points = range(1,self.points+1); 
        for tower in self.__towers:
        	ant = Ant()
        	ant.set_coverage(points)
        	ant.set_actual_tower(tower)
        	self.__ants.append(ant)
    
    def generate_solution(self):
        while(not self.__all_ants_have_completed()):
            for tower in self.__towers:
                for ant in self.__ants:
                	self.__transition(ant)

    def __all_ants_have_completed(self):
        for ant in self.__ants:
            if not ant.travel_completed():
                return False
        return True
    
    def __init_inf(self):
        position = 0
        for tower in self.__towers:
            tower.set_position = position
            self.__inf.append([])
            
            for i in range(len(self.__towers)):
                self.__inf[position].append(0)
        
            position += 1

    def __transition(self,ant):
        # TODO: Next step
        return True
