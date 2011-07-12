1000.times do |i|
  `gnuplot -e "set terminal png; set output 'generation#{i+1}.png'; plot [1:1000] 'generation#{i+1}.dat'"`
end
