function [x, y] = polar2cartesian(r,phi)
%POLAR2CARTESIAN converts polar into cartesian coordinates

  if r < 0
    disp('Error in ''polar2cartesian''! Negative values for ''r'' are not allowed!');
  end

  x = r*cos(phi);
  y = r*sin(phi);
end
