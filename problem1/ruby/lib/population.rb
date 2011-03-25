require File.join(File.dirname(__FILE__),'individual')

class Population
  attr_accessor :generation, :individuals
  attr_reader :number_of_individuals, :number_of_populations
  def initialize(number_of_individuals = 100, number_of_populations = 100 )
    @generation = 1
    @crossover_percentage = 80
    @mutation_percentage = 20

    @sum_of_fitness = 0

    @number_of_populations = number_of_populations
    @number_of_individuals = number_of_individuals

    @individuals = []
    number_of_individuals.times do
      @individuals << Individual.new(generate_rand_chromosome)
    end
  end

  def show(stdout = false)
    result = File.open("generation#{@generation}.dat",'w')
    
    @individuals.each_with_index do |individual,i|
      if stdout
        values = []
        %w(x y z).each{|v| values << "#{v} -> #{individual.send(v)}" }
        puts "#{i+1}: #{values.join(', ')} = #{individual.f}"
      end
      result.puts "#{i+1} #{individual.f}"
    end
    
    result.close
  end

  def size
    @individuals.size
  end

  def each
    @individuals.each{|p| yield p}
  end

  def new_generation
    generate_roulette

    @generation += 1
    @individuals = []

    @number_of_individuals.times do 
      father1 = rand(1000).to_f/10

      @roulette.each{|k,v| father1 = v if k.include?(father1)}
      son = nil
      if((rand(100)+1) < @crossover_percentage)
        father2 = rand(1000).to_f/10
        @roulette.each{|k,v| father2 = v if k.include?(father2)}
        son = father1.crossover(father2)
      else
        son = father1.mutation
      end
      @individuals << son
    end
  end

  private
  def generate_rand_chromosome
    (0..8).map{['0','1'][rand(2)]}.join
  end

  def sum_of_fitness
    @sum_of_fitness = 0
    each do |individual|
      @sum_of_fitness += individual.f
    end
  end

  def generate_roulette
    sum_of_fitness
    @roulette = {}
    _begin = 0
    each do |individual|
      _end = individual.evaluation=(individual.f.to_f/@sum_of_fitness.to_f)*100
      @roulette[Range.new(_begin,_begin+_end,true)] = individual
      _begin += _end
    end
  end
end
