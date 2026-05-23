
% T = [1 0 0; 0 1 0; 0 0 1] and rotated about 30° (phi=0.5236) around C[3,2]

figure;
plotvol([-1 5 -2 4])     
T=[1 0 0;0 1 0;0 0 1]
trplot2(T,'frame','T');

C=[3;2]
plot_point(C, 'bo','MarkerFaceColor', 'g');
plot_point(C, 'printf', {'C',C},'g');
phi=0.5236;
TC=[1 0 3;0 1 2; 0 0 1]				                %translation about C

R=[cos(phi) -sin(phi) 0; sin(phi) cos(phi) 0;0 0 1]	%rotation matrix about phi
CT=[1 0 -3;0 1 -2;0 0 1]				            %translation about –C
RC=TC*R*CT*T
trplot2(RC,'frame','RC','C','color','r')