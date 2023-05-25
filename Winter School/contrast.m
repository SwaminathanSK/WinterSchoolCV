img1 = imread('alex.jpg');
img1 = rgb2gray(img1);

contrastImg1 = imadjust(img1, [], [], 1);

contrastFilter = (double(img1)- 127)/127;
contrastIntensity = .6;

contrastedImg1 = (double(img1)/255 + contrastFilter )*contrastIntensity;

tiledlayout(1, 2)

nexttile
imshow(img1)
title('Image')

nexttile
imshow(contrastedImg1)
title('Image')