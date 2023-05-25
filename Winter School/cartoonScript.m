img1 = imread('christian.jpg');
img1 = rgb2gray(img1);
hsize = 11;
sigma = 2;
h = fspecial('gaussian', hsize, sigma);

img1Blur = imfilter(img1, h);
img1Sobel = edge(img1Blur, "sobel");


threshold = [.1, .2];
img1Canny = edge(img1Blur, 'canny', threshold, 2);

img1BorderCanny = uint8(~img1Canny) .* img1;
img1BorderSobel = uint8(~img1Sobel) .* img1;
img1BorderCannyBlur = uint8(~img1Canny) .* img1Blur;
img1BorderSobelBlur = uint8(~img1Sobel) .* img1Blur;

tiledlayout(3,2)

nexttile
imshow(img1Sobel)
title('Sobel Filter')

nexttile
imshow(img1Canny)
title('Canny Filter')

nexttile
imshow(img1BorderSobel)
title('Border Sobel')

nexttile
imshow(img1BorderCanny)
title('BorderCanny')

nexttile
imshow(img1BorderSobelBlur)
title('SobelBlur')

nexttile
imshow(img1BorderCannyBlur)
title('CannyBlur')


display(uint8(img1Canny))

