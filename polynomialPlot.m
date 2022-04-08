function polynomialPlot(a, b, c)
  graphics_toolkit('gnuplot')
  t = linspace (-10,10);
  plot(t, polyval([a b c], t));
endfunction
