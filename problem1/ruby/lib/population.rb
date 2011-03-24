require File.join(File.dirname(__FILE__),'individual')

class Population
  attr_accessor :generation, :individuals
  def initialize(times = 100)
    @generation = 1
    @individuals = []
    begin
      individual = Individual.new(generate_rand_chromosome)
      individuals << individual if individual.possible?
    end until(individuals.size == times)
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

  private
  def generate_rand_chromosome
    (0..8).map{['0','1'][rand(2)]}.join
  end
end
