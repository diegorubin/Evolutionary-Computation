from space import Space

space = Space()
space.read_input('entrada')

print "Pontos a serem cobertos: %d"%(space.points)

if(space.valid()):
    print 'a valid input'
else:
	print 'invalid input'

space.put_ants()
space.generate_solution()
