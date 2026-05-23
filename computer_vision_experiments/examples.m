p = [1;4;3;1]
% 60 degree in x, trans t=[1;2;3]
t = [1;2;3]
phi = pi*(60/180)
rot_x = [1 0 0 1; 0 cos(phi) -sin(phi) 2; 0 sin(phi) cos(phi) 3; 0 0 0 1]
% inv(T) = trans(R) -trans(r); O-1x3 1) 
final_pos = inv(rot_x)*p
