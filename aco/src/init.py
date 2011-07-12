#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: init.py

from space import Space

space = Space()
print "Lendo Entrada"
space.read_input('entrada')

print "Validando Entrada"
if(not space.valid()):
    print 'invalid input'
    quit()	


for i in range(100):
    print "Inicializando Formigas"
    space.put_ants()

    print "Gerando Soluções"
    space.generate_solution()
    solution = space.best_solution()
    
    print "Melhor solução"
    print "Valor %f"%(solution.distance)
    print [t.name for t in solution.route]
    
    print "Atualização dos Feromonios"
    space.update_pheromones()

