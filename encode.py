import png

# helper function for converting the 8 bit color space to 2
def bitcrush_color(value: int):
    # there is almost definitely a better way to do this
    # *technically* performance isn't a main concern
    # this works at an acceptable speed

    # effectively "rounds off" the 8 bit colors to 2 bit
    # (maps 256 values to 4 values)
    return value//64

def encode_twobit(filename):
    """
    converts an image to a 2-bit color space (64 possible colors)
    filename (str): name of the file to encode
    """
    # this first function is just modified example code from the pypng documentation
    # this loads in the image as an array of pixels
    width, height, pixels, metadata = png.Reader(filename).read()
    list_pixels = list(pixels)
    # create a new array for the image with the same dimensions
    # each pixel has 3 color components
    # so, every 3 elements of the inner array is 1 pixel
    # (not how I would've done it but sure why not)
    output_grid = [[0]*(width*3) for i in range(height)]

    # iterate through all pixels
    # (inner loop counts up by 3. see above)
    for i in range(0, len(list_pixels)):
        for j in range(0, len(list_pixels[i]), 3):
            pixel_red, pixel_green, pixel_blue = list_pixels[i][j], list_pixels[i][j+1], list_pixels[i][j+2]
            lsd_pixel_red, lsd_pixel_green, lsd_pixel_blue = bitcrush_color(pixel_red), bitcrush_color(pixel_green), bitcrush_color(pixel_blue)

            # normalize image
            # 255*(color_component)//4
            # (2 slashes does integer division)
            # this will be moved later
            # need to generate two images: a 2bit preview, and the final hidden image
            output_grid[i][j] = 255*(lsd_pixel_red)//4
            output_grid[i][j+1] = 255*(lsd_pixel_green)//4
            output_grid[i][j+2] = 255*(lsd_pixel_blue)//4
    return output_grid

decodedImageGrid = encode_twobit("steg.png")
png.from_array(decodedImageGrid, 'RGB').save("images/2bit_encode.png")




    

        


        

