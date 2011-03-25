# Será um cromossomo com 3 genes
#  x    y   z
# 000|0000|00

class Individual
  attr_reader :chromosome
  def initialize(chromosome)
    @chromosome = chromosome
  end

  def f
    50*x + 70*y + 100*z if possible?
  end

  def possible?
    ((x + y + z)<=10) && 
      (x <= 4) && (y <= 8) && (z <= 3) &&
      ((x + 2*y + 3*z) <= 18)
  end

  def x
    @chromosome[0..2].to_i(2)
  end

  def y
    @chromosome[3..6].to_i(2)
  end

  def z
    @chromosome[7..8].to_i(2)
  end

  def crossover(father)
    son1 = ''
    son2 = ''
    9.times do |i| 
      if([true,false][rand(2)])
        son1 += @chromosome[i,1]
        son2 += father.chromosome[i,1]
      else
        son2 += @chromosome[i,1]
        son1 += father.chromosome[i,1]
      end
    end
    Individual.new(son1)
  end
end


