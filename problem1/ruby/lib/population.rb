#require File.join(File.dirname(__FILE__),'individual')

class Population
  def self.generate
    @generation = 1
    @individuals = []
    begin
      individual = Individual.new(:x => rand(19),
                                  :y => rand(9),
                                  :z => rand(4))
      @individuals << individual if individual.is_possible?
    end until(@individuals.size == 100)
    self
  end

  def show
    result = File.open("generation#{@generation}.dat",'w')
    
    @individuals.each_with_index do |individual,i|
      values = []
      individual.v.each{|k,v| values << "#{k} -> #{v}"}
      puts "#{i+1}: #{values.join(', ')} = #{individual.f}"
      result.puts "#{i+1} #{individual.f}"
    end
    
    result.close
  end
end
