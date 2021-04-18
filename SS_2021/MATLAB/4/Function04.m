function z = Function04(x,y)
s=(x.^2+y.^2)/4000;
p=cos(x).*cos(y/sqrt(2));
z = s - p + 1;
z=z.*exp(-0.02*(x.^2+y.^2));
end
