#require File.join(File.dirname(__FILE__),'individual')

class Population
  attr_accessor :generation, :individuals
  def self.generate
    population = Population.new
    population.generation = 1
    individuals = []
    begin
      individual = Individual.new(:x => rand(19),
                                  :y => rand(9),
                                  :z => rand(4))
      individuals << individual if individual.is_possible?
    end until(individuals.size == 100)
    population.individuals = individuals
    population
  end

  def show(stdout = false)
    result = File.open("generation#{@generation}.dat",'w')
    
    @individuals.each_with_index do |individual,i|
      if stdout
        values = []
        individual.v.each{|k,v| values << "#{k} -> #{v}"}
        puts "#{i+1}: #{values.join(', ')} = #{individual.f}"
      end
      result.puts "#{i+1} #{individual.f}"
    end
    
    result.close
  end
end
