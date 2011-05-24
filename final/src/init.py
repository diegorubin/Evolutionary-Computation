from tower import Tower

points = 0
towers = []

def read_input(file):
    inputs = open(file)
    points = int(inputs.readline())
    for line in inputs.readlines():
    	informations = line.split(' ')
    	tower = Tower()
    	tower.name = informations[0]
    	tower.cost = float(informations[1])
        tower.points = informations[2:]

        towers.append(tower)
