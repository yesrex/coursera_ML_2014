n=1000;
del=0.05;
mH=@(n) n^50; 
Devequ=@(epi) epi-sqrt((1/(2*n)*(4*epi*(1+epi))+log(4*mH(n^2)/del)));

