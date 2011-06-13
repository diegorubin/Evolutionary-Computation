# -*- coding: utf-8 -*-
from random import random
from tower  import Tower
from ant    import Ant
from copy   import copy

class Space():
    def __init__(self):
        self.__towers = []
        self.__ants = []
        self.points = 0
        self.pheromones = []
        self.distances = []

        self.alfa = 2.0
        self.beta = 2.0
        self.p = 0.3
        self.q = 1.0


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
        print points
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
        points = range(1,self.points+1) 
        position = 0
        for tower in self.__towers:
        	ant = Ant()
        	ant.position = position
        	ant.set_coverage(copy(points))
        	ant.possible_towers = copy(self.__towers)
        	ant.route = []
        	ant.set_actual_tower(tower)
        	self.__ants.append(ant)
        	position += 1
    
    def generate_solution(self):
        while(not self.__all_ants_have_completed()):
            for ant in self.__ants:
                self.__transition(ant)

    def best_solution(self):
        solutions = sorted(self.__ants, key=lambda ant: ant.distance)
        return solutions[0]

    def update_pheromones(self):
        total = len(self.pheromones)
        for i in range(total):
            for j in range(total):
            	self.pheromones[i][j] = (1-self.p)*self.pheromones[i][j]
        for ant in self.__ants:
            for i in range(len(ant.route)-1):
            	self.pheromones[ant.route[i].position][ant.route[i+1].position] += self.q/ant.distance


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
        if ant.travel_completed():
        	return 
        position = ant.get_actual_tower().position
        _sum = self.__sum(ant)
        probabilities_begin = .0
        probabilities_end = .0
        _range = random()
        for tower in ant.possible_towers:
            probabilities_begin = probabilities_end 
            probabilities_end += (self.__partial(position,tower.position)/_sum)
            if((probabilities_begin < _range) and (_range <= probabilities_end)):
                ant.set_actual_tower(tower)

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

