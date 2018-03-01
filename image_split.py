import glob
import matplotlib.image as mpimg
from scipy import misc
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to load images')
ap.add_argument('-sv', '--save', required=True, help='path to save images')
ap.add_argument('-sz', '--size', type=int, default=256, help='needed size of images')
ap.add_argument('-st', '--stride', type=int, default=100, help='stride of window')
args = vars(ap.parse_args())


def split_image(load_path, save_path, size, stride):
    images = []
    t = 0
    #size = args['size']
    #stride = args['stride']

    for img_path in glob.glob(load_path+'/*.jpg'):
        images.append(mpimg.imread(img_path))

    for i, im in enumerate(images):
        print('Spliting the %d image' % (1+i))
        length = im.shape[0]
        width = im.shape[1]

        j = 1
        for a in range(0, length - size - stride, stride):
            for b in range(0, width - size - stride, stride):
                misc.imsave(save_path+'/%d-%d.jpg'%((1+i),j), im[a : a + size, b : b + size, :])
                j += 1
        print('Get %d images.'%j)
        t += j

    print('You get %d images!'%t)
split_image(args['image'], args['save'], args['size'], args['stride'])