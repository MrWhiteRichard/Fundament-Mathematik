preamble

%%
m = load('pardata.mat');

options=optimset('display','off','maxiter',1000,'tolfun',1e-8,'tolx',1e-8);

for k = 1:2
figure(k)
clf
hold on 

xs = m.X(:, 1);
ys = m.X(:, 2);

points=scatter(xs, ys, 20, 'b', 'filled');

ncase=3;
for i=1:ncase
    switch i
        case 1
            fhan = @(coeffs) 0;
            for j = 1:length(m.X)
                fhan = @(coeffs) fhan(coeffs) + (m.X(j, 2) - (coeffs(1)*(m.X(j, 1))^2 + coeffs(2)*m.X(j, 1) + coeffs(3)) )^2;
            end
     
            coeffsstart=[1; 1; 1]; 
            sgn=1; % minimum
            
        case 2
            fhan = @(coeffs) 0;
            for j = 1:length(m.X)
                fhan = @(coeffs) fhan(coeffs) + abs(m.X(j, 2) - (coeffs(1)*(m.X(j, 1))^2 + coeffs(2)*m.X(j, 1) + coeffs(3)) );
            end
     
            coeffsstart=coeffsfinal; 
            sgn=1; % minimum
        case 3
            fhan = @(coeffs) [];
            for j = 1:length(m.X)
                fhan = @(coeffs) [fhan(coeffs) (m.X(j, 2) - (coeffs(1)*(m.X(j, 1))^2 + coeffs(2)*m.X(j, 1) + coeffs(3)) )^2];
            end
            fhan = @(coeffs) median(fhan(coeffs));
     
            coeffsstart=coeffsfinal; 
            sgn=1; % minimum
    end

    
    coeffsfinal=coeffsstart;
    
    if k == 1
        [coeffsfinal,fval,exitflag,output]=fminsearch(@(x) sgn*fhan(x),coeffsfinal,options);
    else
        [coeffsfinal,fval,exitflag,output]=fminunc(@(x) sgn*fhan(x),coeffsfinal,options);
    end
    display(coeffsfinal)
    display(fval)

    y = @(x) coeffsfinal(1).*x.^2 + coeffsfinal(2).*x + coeffsfinal(3);
    x = min(xs):0.1:max(xs);
    fminsearchparabola(i) = plot(x, y(x));
end
legend([fminsearchparabola(1), fminsearchparabola(2), fminsearchparabola(3)], ["Squared distances", "Absolute distances", "Median squared distance"])
end
