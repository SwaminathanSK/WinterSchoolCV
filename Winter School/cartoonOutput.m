img1 = imread('bb1.jpg');
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

img2 = imread('alex.jpg');
img2 = rgb2gray(img2);
hsize = 11;
sigma = 2;
h = fspecial('gaussian', hsize, sigma);

hsize1 = 11;
sigma1 = 1.5;
h1 = fspecial('gaussian', hsize1, sigma1);

img2Blur = imfilter(img2, h);
img2BlurReduced = imfilter(img2, h1);

threshold = [.1, .25];
img2Canny = edge(img2Blur, 'canny', threshold, 2);

se = strel('disk', 2);
thickenedEdges2 = imdilate(img2Canny, se);

img2BorderCannyThickBlur = uint8(~thickenedEdges2) .* img2BlurReduced;

tiledlayout(1,2)

nexttile
imshow(img1)
title('Image')

nexttile
imshow(img1BorderCannyThickBlur)
title('Cartoon')







