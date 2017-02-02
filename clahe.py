from skimage import io
from skimage.exposure import equalize_adapthist
from pyspark import SparkContext
import sys
import glob
import os

in_dir = ""
out_dir = ""

sc = SparkContext()

in_dir = sys.argv[1]
out_dir = sys.argv[2]

def perform_clage(image):
    path, fname = os.path.split(image)
    img = io.imread(image)
    img = equalize_adapthist(img)
    io.imsave(os.path.join(out_dir, fname), img)

pics = glob.glob(in_dir + "*.jpeg")

sc.parallelize(pics).map(perform_clage).count()