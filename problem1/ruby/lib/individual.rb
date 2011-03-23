class Individual
  attr_reader :v
  def initialize(args={})
    @v = args
  end

  def f
    50*@v[:x] + 70*@v[:y] + 100*@v[:z]
  end

  def is_possible?
    ((@v[:x] + @v[:y] + @v[:z])<=10) && ((@v[:x] + 2*@v[:y] + 3*@v[:z]) <= 18)
  end
end


