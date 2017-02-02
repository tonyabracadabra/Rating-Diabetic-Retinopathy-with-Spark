from pyspark.mllib.classification import LogisticRegressionWithLBFGS
from pyspark.mllib.regression import LabeledPoint
from numpy import array

DIR = "file://home/bigdataanalytics/fat/v1/train_256.csv"

sc = SparkContext()
labeledPoints = sc.textFile(DIR) \
                       .map(lambda row: row.split(',')) \
					   .map(lambda seq: LabeledPoint(seq[0], seq[1:]))

# Split data aproximately into training (60%) and test (40%)
training, test = labeledPoints.randomSplit([0.8, 0.2], seed=0)

model = LogisticRegressionWithLBFGS.train(training)

# Evaluating the model on training data
labelsAndPreds_training = training.map(lambda p: (p.label, model.predict(p.features)))
trainErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(training.count())


# Evaluating the model on testing data
labelsAndPreds_test = test.map(lambda p: (p.label, model.predict(p.features)))
testErr = labelsAndPreds.filter(lambda (v, p): v != p).count() / float(test.count())


print("Training Error = " + str(trainErr))
print("Test Error = " + str(testErr))