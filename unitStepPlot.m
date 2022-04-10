function unitStepPlot = unitStepPlot(J, b, Ke, Kt)
    R = 0.06727;
    L = 0.001882;
    pkg load control
    s = tf('s');
    disp(J)
    disp(b)
    disp(Ke)
    disp(Kt)
    sys = Kt / ((J*s^2 + b * s)*(L*s + R) + Kt*(Ke*s));
    setenv("GNUTERM","qt")
    graphics_toolkit('gnuplot')
    step(sys);
    title("Unit-Step Response");
endfunction
