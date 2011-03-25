require File.dirname(__FILE__) + '/spec_helper'
require 'individual'

describe Individual do
  it 'should get values from gene' do
    individual = Individual.new('010100001')
    individual.x.should == 2
    individual.y.should == 8
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

end
