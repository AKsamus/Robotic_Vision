im=imread('../assets/parks.jpg');	% read an image and use gamma correction
figure;
imshow(im);	
im=lin2rgb(im);         %Apply gamma correction to the image according to the sRGB standard, storing the values in double precision
figure;
imshow(im);		            	
im1=zeros(2448,3264,3);			        %for new image generate emty matrix
im=double(im);                          %convert uint to double
im1=double(im1);
im1(:,:,1)=im(:,:,1)./im(:,:,2);			%elementwise division   r=R/G
im1(:,:,2)=im(:,:,3)./im(:,:,2);			%			            b=B/G
figure;
imshow(im1)                              %idisp(im1);
s(:,:,1)=8.5*log(im1(:,:,1))+15.5*log(im1(:,:,2));	% adjust factor till shadow removed, values not in region 0 till 255!
figure;
imshow(s)                                %apply scaling of values!
