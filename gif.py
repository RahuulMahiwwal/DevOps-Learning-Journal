import imageio.v3 as iio

filenames = ["team-pic1.png", "team-pic2.png"]

images = []

for filename in filenames :
    images.append(iio.imread(filename))

iio.imwrite("team.gif", images, duration = 500, loop = 0)

# Opening the GIF automatically

import os

gif_path = os.path.abspath("team.gif")

os.startfile(gif_path)