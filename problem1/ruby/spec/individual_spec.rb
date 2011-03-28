require File.dirname(__FILE__) + '/spec_helper'
require 'individual'

describe Individual do
  it 'should get values from gene' do
    individual = Individual.new('010011001')
    individual.x.should == 2
    individual.y.should == 6
    individual.z.should == 1
  end

  it 'should get a result of objective function' do
    individual = Individual.new('000000000')
    individual.f.should == 0
    individual = Individual.new('100001110')
    individual.x.should == 4
    individual.y.should == 3
    individual.z.should == 2
    individual.f.should == 610
  end

  it 'should generate a son' do
    f1 = Individual.new('000000000')
    f2 = Individual.new('000000010')

    son = f1.crossover(f2)
    [0,2].include?(son.z).should be_true
  end

  it 'should dont generate a individual impossible' do
    individual = Individual.new('011011101')
    individual.should be_possible

    individual = Individual.new('111111111')
    individual.should be_possible
  end

  it 'should carry a mutation' do
    individual = Individual.new('001011101')
    individual.x.should == 1
    individual.y.should == 7
    individual.z.should == 1
    
    individual.mutation
    individual.should be_possible
    individual.chromosome.should_not == '001011101'
  end

end
