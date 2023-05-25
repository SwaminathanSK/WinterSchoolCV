


img1 = imread('alex.jpg');
img1 = rgb2gray(img1);
hsize = 11;
sigma = 2;
h = fspecial('gaussian', hsize, sigma);

hsize1 = 11;
sigma1 = 1.5;
h1 = fspecial('gaussian', hsize1, sigma1);

img1Blur = imfilter(img1, h);
img1BlurReduced = imfilter(img1, h1);

threshold = [.1, .25];
img1Canny = edge(img1Blur, 'canny', threshold, 2);

se = strel('disk', 2);
thickenedEdges1 = imdilate(img1Canny, se);

img1BorderCannyThickBlur = uint8(~thickenedEdges1) .* img1BlurReduced;

tiledlayout(2,2)

nexttile
imshow(img1)
title('Image')

nexttile
imshow(img1BorderCannyThickBlur)
title('Cartoon')

nexttile
imshow(thickenedEdges1)
title('Thick Edges')

nexttile
imshow(img1Canny)
title('Canny Edge')








