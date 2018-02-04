import numpy as np
import pandas as pd

from pandas import read_csv
#The Machine learning alogorithm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt 
# Test train split
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
# Just to switch off pandas warning
pd.options.mode.chained_assignment = None

# Used to write our model to a file
from sklearn.externals import joblib

data = read_csv("data.csv")
test_input = data[["Duration", "packet", "byte length"]]
y_true = data[["result"]]
rf = joblib.load("test_model")
y_pred = rf.predict(test_input)
print y_pred
#op = pred
print len(y_pred)
#accuracy = rf.score(test_input, op)
accuracy = accuracy_score(y_true, y_pred)
print "Accuracy = {}%".format(accuracy * 100)
recall = recall_score(y_true, y_pred, average= 'macro')
print 'recall', recall
precision = precision_score(y_true, y_pred, average= 'micro')
print 'Precision' , precision
f1 = f1_score(y_true, y_pred, average='macro')
print 'F1 Score', f1
results = confusion_matrix(y_pred, y_true)
print "----Confusion Matrix-----"

print results

plt.matshow(results)
plt.title('Confusion Matrix')
plt.colorbar()
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()
y= np.array(y_pred)
if(np.count_nonzero(y==1))>10:
    print "Attack Detected"
else:
    print "No Attack"
    

