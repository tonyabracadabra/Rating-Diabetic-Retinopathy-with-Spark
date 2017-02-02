###Running The Files###

#resize_spark_mapper.py#

spark-submit resize_spark_mapper.py {Test/Train} {Image size} {Image directory}

#clahe.py#

spark-submit clahe.py {Image input directory} {New Image output directory}

#hog.py#

spark-submit hog.py {Image input directory} {New Image output directory}


#toCSV.py#

spark-submit toCSV.py {Label File's path} {Image input directory}

#svm.py#

spark-submit svm.py {Directory of the csv file}

#lr.py#

spark-submit lr.py {Directory of the csv file}# Rating-Diabetic-Retinopathy-with-Spark
