pkg load control

function tfPlot = tfPlot()
    R = 0.06727;
    L = 0.001882;
    KtKe = Kt*Ke;
    s = tf('s');
    sys = Kt/((J * s^2 + b * s) * (R * s + L) + KtKe * s);
    graphics_toolkit('gnuplot')
    step(sys);
    title("Unit-Step Response");
    impulse(sys);
    title("Unit-Impulse Response");
