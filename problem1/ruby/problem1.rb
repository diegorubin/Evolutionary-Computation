#!/usr/bin/env ruby
# Problema 1
# Capitão Caverna S.A.
#
# maxf(x) = 50x + 70y + 100z
# sendo:
# x a quantidade de jangadas. x <= 4
# y a quantidade de canoa. y <= 8
# z a quantidade de arcas. z <= 3
# 
# Cada embarcação precisa de um capitão.
# A jangada precisa de 1 tripulante, a canoa
# 2 e a arca 3.
#
# assim:
# x + y + z <= 10
# x + 2y + 3z <= 18
#
# Modelagem
#
# Serão necessarios 3 genes.
# Cada individuo deve obedecer as restrições.
require 'lib/individual'
require 'lib/population'

population = Population.new(1000,1000)
population.show

population.number_of_populations.times do
  population.new_generation
  population.show
end
