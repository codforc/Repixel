## What is Repixel ? 
Repixel filters each pixel in the image as you choose. Its approach to image filtering handles pixel harmony of the same color in the image very well.

It is quite possible that there are pixels of the same color and pixels of close colors in a picture. If we select r, g, b values to be increased, decreased, divided or multiplied, all pixels will go through the same process and there will be either the same or different results between these pixels. This also gives birth to beauty !


## Usage
```
main.py -p IMAGE_PATH -r +R -G /B (supported operators : * / - +)
example : main.py -p test_img.jpg -r +50 *1 -100
```

## Repixel Results (Before & After)

###### Before
<img src="/images/before.jpg" width="220">

###### After
<p float="left">
    <img src="/images/after_1.jpg" width="220">
    <img src="/images/after_2.jpg" width="220">
    <img src="/images/after_3.jpg" width="220">
</p>


