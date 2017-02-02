from skimage import io
from skimage.exposure import equalize_adapthist
from pyspark import SparkContext
import sys
import glob
import os

from skimage.feature import hog
from skimage import data, color, exposure


def perform_hog(image):
	path, fname = os.path.split(image)
	# to grey
	image = color.rgb2gray(io.imread(image))

	fd, hog_image = hog(image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualise=True)

    io.imsave(os.path.join(out_dir, fname), hog_image)

pics = glob.glob(in_dir + "*.jpeg")

sc = SparkContext()

in_dir = sys.argv[1]
out_dir = sys.argv[2]

sc.parallelize(pics).map(perform_hog).count()