#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: init.py

from space import Space

space = Space()
space.read_input('entrada')

print "Pontos a serem cobertos: %d"%(space.points)

if(space.valid()):
    print 'a valid input'
else:
	print 'invalid input'

print "Inicializando Formigas"
space.put_ants()

print "Gerando Soluções"
space.generate_solution()
