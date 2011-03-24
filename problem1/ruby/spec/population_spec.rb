require File.dirname(__FILE__) + '/spec_helper'
require 'population'

describe Population do
  it 'should generate a rand population' do
    population = Population.new(100)
    population.size.should == 100

    values = []
    population.each do |individual|
      individual.should be_possible
      values << individual.f if individual.f > 0
    end
    
    values.size.should >  0
    
  end
end
