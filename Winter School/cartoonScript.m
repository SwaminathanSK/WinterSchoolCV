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
img1Sobel = edge(img1Blur, "sobel");


threshold = [.1, .25];
img1Canny = edge(img1Blur, 'canny', threshold, 2);

se = strel('disk', 2);
thickenedEdges = imdilate(img1Canny, se);

img1BorderCanny = uint8(~img1Canny) .* img1;
img1BorderSobel = uint8(~img1Sobel) .* img1;
img1BorderCannyThickBlur = uint8(~thickenedEdges) .* img1BlurReduced;
img1BorderSobelBlur = uint8(~img1Sobel) .* img1Blur;

tiledlayout(3,2)

nexttile
imshow(img1Sobel)
title('Sobel')

nexttile
imshow(img1Canny)
title('Canny Filter')

nexttile
imshow(img1BorderSobel)
title('Border Sobel')

nexttile
imshow(thickenedEdges)
title('BorderCanny')

nexttile
imshow(img1BorderSobelBlur)
title('SobelBlur')

nexttile
imshow(img1BorderCannyThickBlur)
title('CannyBlur')



