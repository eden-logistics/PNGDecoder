# this first bit is just example code from the pypng documentation
# this loads in the image as an array of pixels
import png

# Read a PNG file
reader = png.Reader(filename='steg.png')
width, height, pixels, metadata = reader.read()

# Access basic information
print(f"Image size: {width}x{height}")
print(f"Metadata: {metadata}")

# Convert pixels to list
pixel_list = list(pixels)

# --- END EXAMPLE CODE ---

# helper function for extracting the 2 least significant bits
# and converting it back to an int
def extract_lsd(value: int):
    bin_rep = bin(value) # get the binary representation of the integer
    lsd = bin_rep[-2:] # chop off all but the last 2 bits
    return int(lsd, 2) # return those last 2 bits as an int

# create a new array for the image with the same dimensions
# each pixel has 3 color components
# so, every 3 elements of the inner array is 1 pixel
# (not how I would've done it but sure why not)
new_image_grid = [[0]*(width*3) for i in range(height)]

# iterate through all pixels
# (inner loop counts up by 3. see above)
for i in range(0, len(pixel_list)):
    for j in range(0, len(pixel_list[i]), 3):
        pixel_red, pixel_green, pixel_blue = pixel_list[i][j], pixel_list[i][j+1], pixel_list[i][j+2]
        lsd_pixel_red, lsd_pixel_green, lsd_pixel_blue = extract_lsd(pixel_red), extract_lsd(pixel_green), extract_lsd(pixel_blue)

        # normalize image
        # 255*(color_component)//4
        # (2 slashes does integer division)
        new_image_grid[i][j] = 255*(lsd_pixel_red)//4
        new_image_grid[i][j+1] = 255*(lsd_pixel_green)//4
        new_image_grid[i][j+2] = 255*(lsd_pixel_blue)//4

png.from_array(new_image_grid, 'RGB').save("output.png")




    

        


        

