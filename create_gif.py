import imageio as iio
filenames = ['3.png', '4.png']
images = []
for filename in filenames:
    images.append(iio.imread(filename))

iio.mimsave('cats.gif', images, duration=600, loop=0)