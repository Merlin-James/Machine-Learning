from sklearn import svm    			# To fit the svm classifier
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import read_csv
from sklearn.externals import joblib
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
data = read_csv("data.csv")
test_input = data[["Duration", "n_packets", "byte length"]]
y_true = data[["result"]]
clf = joblib.load("svm_model")
y_pred = clf.predict(test_input)
print y_pred
#op = pred
print "Support Vector Machine"
#accuracy = rf.score(test_input, op)
accuracy = accuracy_score(y_true, y_pred)
print "Accuracy = {}%".format(accuracy * 100)
#print '\n confussion matrix:\n',confusion_matrix(y_true, y_pred)
#results = confusion_matrix(y_true, y_pred)
#print "----Confusion Matrix-----"

#print results

#plt.matshow(results)
#plt.title('Confusion Matrix')
#plt.colorbar()
#plt.ylabel('Actual')
#plt.xlabel('Predicted')
#plt.show()
