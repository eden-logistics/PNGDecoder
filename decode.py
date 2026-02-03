import png
# helper function for extracting the 2 least significant bits
# and converting it back to an int
def extract_lsd(value: int):
    bin_rep = bin(value) # get the binary representation of the integer
    lsd = bin_rep[-2:] # chop off all but the last 2 bits
    return int(lsd, 2) # return those last 2 bits as an int

def decode_normalize(filename):
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
            lsd_pixel_red, lsd_pixel_green, lsd_pixel_blue = extract_lsd(pixel_red), extract_lsd(pixel_green), extract_lsd(pixel_blue)

            # normalize image
            # 255*(color_component)//4
            # (2 slashes does integer division)
            output_grid[i][j] = 255*(lsd_pixel_red)//4
            output_grid[i][j+1] = 255*(lsd_pixel_green)//4
            output_grid[i][j+2] = 255*(lsd_pixel_blue)//4
    return output_grid

decodedImageGrid = decode_normalize("steg.png")
png.from_array(decodedImageGrid, 'RGB').save("images/decode_output.png")




    

        


        

