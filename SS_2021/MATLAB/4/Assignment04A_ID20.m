preamble

harm = @(t, A, w, phi) A* sin(w*t - phi);

Asum = @(A1, A2, phi1, phi2) sqrt(A1^2 + A2^2 + 2*A1*A2*cos(phi2 - phi1));

phisum = @ (A1, A2, phi1, phi2) atan( (A1*sin(phi1) + A2*sin(phi2))/(A1*cos(phi1) + A2*cos(phi2)) );

A1 = 1;
A2 = 2;
phi1 = pi/3;
phi2 = -pi/2;
w = 1.5;

As = Asum(A1, A2, phi1, phi2)
phis = phisum(A1, A2, phi1, phi2)

t = linspace(0,15,1000);

y1 = harm(t, A1, w, phi1);
y2 = harm(t, A2, w, phi2);
ys = harm(t, As, w, phis);

figure(1)
clf
py1 = plot(t, y1);
hold on
py2 = plot(t, y2);
hold on
pys = plot(t, ys, 'g');
hold on
pysum = plot(t, y1+y2, 'm--');

hleg=legend([py1, py2, pys, pysum],'$y_1(t)=A_1 \sin(\omega t - \phi_1)$','$y_2(t)=A_2 \sin(\omega t - \phi_2)$', '$y_s(t)=A_s \sin(\omega t - \phi_s)$', '$y_{sum}(t)=y_1(t) + y_2(t)$', 'location','southwest');
xlabel('$t$') % label x a xis
ylabel('$y$') % label y axis
htit=title('$y(t) = A \sin(\omega t - \phi)$ for different values of $A$ and $\phi$');