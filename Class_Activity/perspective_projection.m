%Task 1: Perspective projection without K and T --> C=C0*P0

P=[0.3;0.4;3;1] % or P=[0.3,0.4,3.0,1]’	column vector (spaltenvektor) in homogeneous form
f=0.015		                    % focal length
C0=[f 0 0;0 f 0;0 0 1]          % origin camera matrix
P0=[1 0 0 0; 0 1 0 0;0 0 1 0]   %Projection matrix
C=C0*P0                         % Camera matrix
p=C*P                           % point on image plane

p1=[p(1)/p(3);p(2)/p(3)]        % convert to nonhomogeneous image plane

% % Task 2: Calculate position from Point P’ (0.0015/0.002/0.015) (Example before) 
% % in Pixel P’(u,v) for camera sensor with pixel size 10um and resolution of 
% % 1920x1080. (Perspective projection with K but without T--> C=C0*P0*K)
% 
P=[0.3;0.4;3;1] % or P=[0.3,0.4,3.0,1]’	column vector (spaltenvektor) in homogeneous form
f=0.015		                    % focal length
C0=[f 0 0;0 f 0;0 0 1]          % origin camera matrix
P0=[1 0 0 0; 0 1 0 0;0 0 1 0]   % Projection matrix
K=[100000 0 960;0 100000 540;0 0 1] % camera parameter matrix
C=K*C0*P0	                    % Camera matrix
p=C*P                           % point on image plane

p1=[p(1)/p(3);p(2)/p(3)]        % convert to nonhomogeneous image plane

% % Task 3: What happens with P and P’ when Camera shifted left about 0.5m?
% %(Perspective projection with K and  T --> C=C0*P0*K*T)
% 
% P=[0.3;0.4;3;1] % or P=[0.3,0.4,3.0,1]’	column vector (spaltenvektor) in homogeneous form
% f=0.015		                    % focal length
% C0=[f 0 0;0 f 0;0 0 1]          % origin camera matrix
% P0=[1 0 0 0; 0 1 0 0;0 0 1 0]   % Projection matrix
% K=[100000 0 960;0 100000 540;0 0 1] % camera parameter matrix
% T=[1 0 0 -0.5;0 1 0 0;0 0 1 0;0 0 0 1]  %T ransformation matrix
% C=K*C0*P0*inv(T)	                    % Camera matrix, attention to order C0*P0*K not possible
% p=C*P                           % point on image plane
% 
% p1=[p(1)/p(3);p(2)/p(3)]        % convert to nonhomogeneous image plane
