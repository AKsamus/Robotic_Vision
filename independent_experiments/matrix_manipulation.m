num = 6   %code works for 4, 5, 6
num2 = 111
num3 = round(num*0.6)
rz = zeros(num);
ro = num2*ones(num);
a = [repmat(rz, 1, num);
     repmat([rz repmat(ro,1,num3) rz], num3,1);
     repmat(rz, 1, num);]
%a=[0,0,0,0,0;
 %   0,1,1,1,0;
  %  0,1,1,1,0;
   % 0,1,1,1,0;
    %0,0,0,0,0]
angle = 45
new_a = imrotate(a, angle, 'nearest', 'crop')
disp(nnz(a==num2))
disp(nnz(new_a==num2))