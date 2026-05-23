


% frame 1: translation of [1,2] + rotation of 30°==0.5236

phi=0.5236;
T1=[cos(phi) -sin(phi) 1; sin(phi) cos(phi) 2; 0 0 1]
plotvol([0 5 0 5]);
trplot2(T1,'frame','1','color','b');

% frame 2: translation of [2,1] + rotation of 0°==0
phi2=0;
T2=[cos(phi2) -sin(phi2) 2;sin(phi2) cos(phi2) 1; 0 0 1]
trplot2(T2,'frame','2','color','r');

% frame 3: compose of frame1 and frame2
T3=T1*T2
trplot2(T3,'frame','3','color','g');

% frame 4: compose of frame2 and frame1
T4=T2*T1
trplot2(T4,'frame','4','color','c');