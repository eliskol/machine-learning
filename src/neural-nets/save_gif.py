import imageio

images = []
filenames = [f"./temp/net{i}.png" for i in range(1, 1001)]
for filename in filenames:
    images.append(imageio.v2.imread(filename))

imageio.v2.mimsave("363-1-1000.gif", images)
