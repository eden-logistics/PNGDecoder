# i = 244
# bini = bin(244)
# print(bini)
# print(bini[-2:])

# def extract_lsd(value: int):
#     bin_rep = bin(value)
#     lsd = bin_rep[:2]
#     return int(lsd, 2)

# print(extract_lsd(244))
# initializing an empty 2d array
# grid = [[(0, 0, 0)]*256]*256

# iterating through a tuple
# pixel = (67, 68, 69)
# for color in pixel:
#     print(color)

width = 200
height = 200

new_image_grid = [[0]*(width*3) for i in range(height)]
new_image_grid[5][1] = 67
print(new_image_grid)