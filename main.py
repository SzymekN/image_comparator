import numpy as np
from PIL import Image
from numpy import asarray
       

# load images
image1 = Image.open("image2a.png")
image1_array = asarray(image1)

image2 = Image.open("image2b.png")
image2_array = asarray(image2)


# get sizes of images
image1_width = image1.size[0] 
image1_height = image1.size[1]
image2_width = image2.size[0] 
image2_height = image2.size[1] 

result_array = np.copy(image1_array)

# define bounds if images are not equal size
min_width = min(image1_width, image2_width)
min_height = min(image1_height, image2_height)

for y in range(min_height):
    for x in range(min_width):
        
        # calculate difference in pictures based on rgb values
        diff = image1_array[y][x] - image2_array[y][x]
        diff_sum = sum(diff)

        # if difference is noticable set pixel as red
        if(diff_sum) > 100:

            # if pixel is not white copy it from second array
            if(image2_array[y][x][0] != 255):
                result_array[y][x] = image2_array[y][x]

            # make pixel red
            result_array[y][x][0] = 255
        


# translate array to image and show it
result_image = Image.fromarray(result_array)
result_image.show()