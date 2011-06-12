# -*- coding: utf-8 -*-
from tower import Tower
from ant   import Ant

class Space():
    def __init__(self):
        self.__towers = []
        self.__ants = []
        self.points = 0
        self.pheromones = []
        self.distances = []

        self.alfa = 0.5
        self.beta = 0.5

    def append_tower(self, tower):
        self.__towers.append(tower)

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
        position = 0
        for line in inputs.readlines():
            informations = line.split(' ')
            tower = Tower()
            tower.name = informations.pop(0)
            tower.cost = float(informations.pop(0))
            tower.points = sorted([int(point) for point in informations if point.isdigit()])
            tower.position = position
            position += 1

            self.append_tower(tower)
        self.__towers = sorted(self.__towers, key=lambda tower: tower.cost)
        self.__generate_distances()
        self.__generate_pheromones()
    
    def put_ants(self):
        points = range(1,self.points+1); 
        for tower in self.__towers:
        	ant = Ant()
        	ant.set_coverage(points)
        	ant.possible_towers = self.__towers
        	ant.set_actual_tower(tower)
        	self.__ants.append(ant)
    
    def generate_solution(self):
        self.__transition(self.__ants[0])
        while(not self.__all_ants_have_completed()):
            for ant in self.__ants:
            	pass
                #self.__transition(ant)

    def __all_ants_have_completed(self):
        for ant in self.__ants:
            if not ant.travel_completed():
                return False
        return True
    
    def __generate_pheromones(self):
        _len = len(self.__towers)
        self.pheromones = [[1]*_len]*_len
    
    def __generate_distances(self):
        _len = len(self.__towers)
        self.distances = [[0]*_len]*_len
        for i in range(_len):
            for j in range(_len):
                if i != j:
                    self.distances[i][j] = self.__find_distance(self.__towers[i],self.__towers[j])
    
    def __find_distance(self,origin, destiny):
        a = len(origin.points)
        b = len([point for point in origin.points if point in destiny.points])

        return int(destiny.cost**(a - b + 1))


    def __transition(self,ant):
        position = ant.get_actual_tower().position
        _sum = self.__sum(ant)
        soma_probabilidades = .0
        for tower in ant.possible_towers:
        	soma_probabilidades += (self.__partial(position,tower.position)/_sum)

    def __partial(self,i,j):
        p = self.pheromones[i][j]**self.alfa
        h = (1.0/self.distances[i][j])**self.beta
        return p*h

    def __sum(self,current):
        _sum = 0
        position = current.get_actual_tower().position
        for tower in current.possible_towers:
        	_sum += self.__partial(position,tower.position)
        return _sum

