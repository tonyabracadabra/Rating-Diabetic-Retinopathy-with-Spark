#!/usr/bin/env python

"""
	This code is used for transforming image to one dimensional array
"""

import sys
from pyspark import SparkContext
from PIL import Image
import glob
import csv

sc = SparkContext()

labelFileName = sys.argv[1]
inputImagesPath = sys.argv[2]

d = {}
#Make image mapping
reader = csv.reader(open(labelFileName, 'r'))
#Make dictionary from each row in the CSV (skip first row)
for k,v in reader:
    if k != "image":
        d[k] = int(v)

def make_img_list(im_path):
    return np.array(Image.open(im_path)).ravel().tolist()

def add_to_csv(f, im_path):
	img = make_img_list(im_path)
	img_label = [d[os.path.basename(path)[:-5]]]
	arr = [img_label] + img

    for i, j in enumerate(arr):
        if i == (len(arr) - 1):
            f.write(str(j) + "\n")
        else:
            f.write(str(j) + ",")


images = glob.glob(inputImagesPath + "/*")

pfile = "/home/bigdataanalytics/fat/v1/train_256_clahe.csv"
f = open(pfile, 'wb')
sc.parallelize(images).map(lambda x:add_to_csv(f, x)).count()



